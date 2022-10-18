import gym
import numpy as np
import tensorflow as tf
from collections import deque


class DQN:

    def __init__(self):
        self.env = gym.make('CartPole-v0')
        self.gamma = 0.9
        self.status_dim = 4
        self.actions_dim = 2
        self.hidden_num = 32
        self.train_num = 0
        self.batch_size = 32
        self.lr = 0.001
        self.init_args()
        self.memory_size = 2000
        self.observe = deque(maxlen=self.memory_size)
        self.eplison = 1  # 用于随机获取next_status
        self.eplison_decay = 0.95
        self.eplison_to_decay_num = 500
        self.min_eplison = 0.01
        self.cost = np.array([])

    def init_args(self):
        self.status_input = tf.placeholder(shape=[None, self.status_dim], dtype=tf.float32)  # Q矩阵的状态
        self.q_target = tf.placeholder(shape=[None, self.actions_dim], dtype=tf.float32)  # 目前q状态，q_status 与 q_target

        self.W1 = tf.Variable(tf.truncated_normal([self.status_dim, self.hidden_num], mean=0, stddev=0.01),
                              dtype=tf.float32)
        b1 = tf.Variable(tf.zeros([1, self.hidden_num]) + 0.1)  # 如果偏置设置成tf.Variable(0.1)会不利于收敛

        fnn1 = tf.nn.relu(tf.matmul(self.status_input, self.W1) + b1)

        W2 = tf.Variable(tf.truncated_normal([self.hidden_num, self.actions_dim], mean=0, stddev=0.01),
                         dtype=tf.float32)
        b2 = tf.Variable(tf.zeros([1, self.actions_dim]) + 0.1)

        self.q_status = tf.matmul(fnn1, W2) + b2  # 相当于Q矩阵下对应的一行数据

        self.loss = tf.reduce_mean(tf.reduce_sum(tf.square(self.q_target - self.q_status), axis=1))
        self.train_op = tf.train.GradientDescentOptimizer(self.lr).minimize(self.loss)
        init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(init)

    def get_action(self, status):
        status = status.reshape(1, -1)
        if np.random.uniform() <= self.eplison:  # 提升模型的泛化能力
            action = self.env.action_space.sample()
        else:
            q_status = self.sess.run(self.q_status, feed_dict={self.status_input: status})
            action = np.argmax(q_status)
        if (self.eplison > self.min_eplison) and (self.train_num >= self.eplison_to_decay_num):
            self.eplison *= self.eplison_decay
        return action

    def experiment_replay(self):
        random_index = np.random.choice(len(self.observe), self.batch_size)
        content = np.array(self.observe)[random_index]
        batch_status = np.array(list(content[:, 0]))
        action_list = content[:, 1]
        batch_next_status = np.array(list(content[:, 2]))
        reward_list = content[:, 3]
        done_list = content[:, 4]
        # 构造成可用于tensorflow训练的模型
        q_next_status = self.sess.run(self.q_status, feed_dict={self.status_input: batch_next_status})
        q_prev_status = self.sess.run(self.q_status, feed_dict={self.status_input: batch_status})
        next_max_q = np.max(q_next_status, axis=1)
        for i in range(len(reward_list)):
            next_max_q_val = next_max_q[i]
            action = action_list[i]
            done = done_list[i]
            if not done:
                q_prev_status[i][action] = reward_list[i] + self.gamma * next_max_q_val  # Q = R + gamma * max(Q_next)
            else:
                q_prev_status[i][action] = reward_list[i]  # 不能到达的状态 Q = R
        batch_q_target = np.array(q_prev_status).reshape(-1, self.actions_dim)
        _, loss = self.sess.run([self.train_op, self.loss], feed_dict={self.status_input: batch_status,
                                                                       self.q_target: batch_q_target}
                                )
        self.train_num += 1
        loss = loss.reshape(-1, )
        return loss

    def train(self):
        for i in range(8000):
            # 先观察到一定的次数，才开始训练
            # 预先给定一个初始状态
            status = self.env.reset()
            done = False
            reward_sum = 0
            loss = 'inf'
            while not done:
                # 利用一个队列self.observe保存之前的尝试过程，当达到一定数目的时候则开始训练
                action = self.get_action(status)
                next_status, reward, done, info = self.env.step(action)
                x, x_dot, theta, theta_dot = next_status
                r1 = (self.env.x_threshold - abs(
                    x)) / self.env.x_threshold - 0.8  # 0.8是一个偏置，abs(x)=2.4时，r1=-0.8,abs(x)=0时，r1=0.2
                r2 = (self.env.theta_threshold_radians - abs(
                    theta)) / self.env.theta_threshold_radians - 0.5  # 同上，# 0.5是一个偏置，r2=(-0.5,0.5)
                # 偏置的设置主要是为了体现角度与位置的重要性，可以调整成其他值也可以收敛
                reward = r1 + r2  # 位置与倾斜角度的结合,可以收敛的比较快
                self.observe.append([status, action, next_status, reward * 10, done])  # reward * 10加速收敛
                if len(self.observe) >= self.batch_size:
                    loss = self.experiment_replay()  # 经验回放同时训练神经网络
                status = next_status
                reward_sum += 1
            if i % 5 == 0:
                print(i, reward_sum, loss, self.eplison)

    def predict(self):
        for i in range(10):
            status = self.env.reset()
            rew_sum = 0
            while True:
                self.env.render()
                status = status.reshape(1, -1)
                q_val = self.sess.run(self.q_status, feed_dict={self.status_input: status})
                action = np.argmax(q_val, axis=1)[0]
                next_status, reward, done, info = self.env.step(action)
                status = next_status
                rew_sum += reward
                if done:
                    print(rew_sum)
                    self.env.close()
                    break


if __name__ == '__main__':
    dqn = DQN()
    dqn.train()
    dqn.predict()