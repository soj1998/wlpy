#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import win32api
import win32event
import win32service
import win32serviceutil
import servicemanager
import win32timezone
import os
import logging
import re
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
from threading import Timer
import requests
import json


def setup_log(log_name):
    # 创建logger对象。传入logger名字
    logger = logging.getLogger(log_name)
    log_path = os.path.join("D:\\tongbudaozhashijian\\", log_name)
    # 设置日志记录等级
    logger.setLevel(logging.INFO)
    # interval 滚动周期，
    # when="MIDNIGHT", interval=1 表示每天0点为更新点，每天生成一个文件
    # backupCount  表示日志保存个数
    # 通过设置TimedRotatingFileHandler进行日志按周(W)、天(D)、时(H)、分(M)、秒(S)切割。
    file_handler = TimedRotatingFileHandler(
        filename=log_path, when="MIDNIGHT", interval=1, backupCount=30
    )
    # filename="mylog" suffix设置，会生成文件名为mylog.2020-02-25.log
    file_handler.suffix = "%Y-%m-%d.log"
    # extMatch是编译好正则表达式，用于匹配日志文件名后缀
    # 需要注意的是suffix和extMatch一定要匹配的上，如果不匹配，过期日志不会被删除。
    file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}:.log$")
    # 定义日志输出格式
    file_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s] [%(process)d] [%(levelname)s] - %(module)s.%(funcName)s (%(filename)s:%(lineno)d) - %(message)s"
        )
    )
    logger.addHandler(file_handler)
    return logger


def task():
    try:
        logger = logging.getLogger("mylog")
        # logger.debug('debug 信息')
        # logger.info('info 信息')
        # logger.warning('warning 信息')
        # logger.error('error 信息')
        # logger.critical('critial 信息')
        now = datetime.now()
        ts = now.strftime("%Y-%m-%d %H:%M:%S")
        url = "http://192.168.0.69/Home/SetSynchronizeTime"
        data = {"key": "EBBD366937FCAD4AF67D7D018DFEF8A8", "channelout": "2", "time": ts}
        logger.info(data)
        ## headers中添加上content-type这个参数，指定为json格式
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        res = requests.post(url=url, headers=headers, data=json.dumps(data), timeout=3)
        logger.info(res.text)
    except Exception as e:
        logger.error(e)


def func():
    task()
    t = Timer(60 * 10, func)
    t.start()


class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "tongbudaozhashijian"
    _svc_display_name_ = "同步道闸时间"
    _svc_description_ = "同步道闸时间"
    logger = logging.getLogger("mylog")

    def __init__(self, args):
        logger.info('init')
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        try:
            self.ReportServiceStatus(win32service.SERVICE_RUNNING)
            logger.info('start')
            self.start()
            logger.info('wait')
            win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)
            logger.info('done')
        except BaseException as e:
            logger.error('Exception : %s' % e)
            self.SvcStop()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        logger.info('stopping')
        self.stop()
        logger.info('stopped')
        win32event.SetEvent(self.stop_event)
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def start(self):
        func()

    def stop(self):
        pass

    def log(self, msg):
        servicemanager.LogInfoMsg(str(msg))

    def sleep(self, minute):
        win32api.Sleep((minute * 1000), True)


if __name__ == "__main__":
    logger = setup_log("mylog")
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MyService)