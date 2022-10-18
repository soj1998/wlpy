import sys

import markdown

import codecs

css = '''
<head>
    <style>
         body{   
           /*background-color: red;*/
           font-size: 12px;
         }
    </style>
</head>
'''


def main(argv):

    name = argv[0]

    in_file = '%s.md' % (name)

    out_file = '%s.html' % (name)

    input_file = codecs.open(in_file, mode="r", encoding="utf-8")

    text = input_file.read()

    html = markdown.markdown(text)

    output_file = codecs.open(out_file, "w", encoding="utf-8",errors="xmlcharrefreplace")

    output_file.write(css+html)


if __name__ == "__main__":
    main(['E:\python\pythonwork\wlpy\MdToHtml\ceshi'])

