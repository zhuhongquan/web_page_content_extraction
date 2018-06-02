import requests
import re

def get_content(url, outfile):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    html = str(res.text)
    outfile = open(outfile, "a", encoding="utf-8")

    # 获取网页title
    re_title = re.compile(r'<title>(.+?)</title>')
    title = re.findall(re_title, html)
    outfile.write("title:" + "\n")
    for i in title:
        outfile.write(i+"\n")

    # 获取网页body
    re_body = re.compile(r'<body.+</body>', re.S)
    body = re.findall(re_body, html)
    outfile.write("\n" + "body:" + "\n")
    text = body[0]

    # 去除HTML标签
    note_tag = re.compile(r'<!--.+?-->', re.S)  #去掉注释内容
    body_tag = re.compile(r'</*body.*?>', re.S)
    div_tag = re.compile(r'</*?div.*?>', re.S)
    p_tag = re.compile(r'</*?p.*?>', re.S)
    hr_tag = re.compile(r'</*?hr.*?>', re.S)
    a_tag = re.compile(r'</*?a.*?>', re.S)
    b_tag = re.compile(r'</*?b.*?>', re.S)
    ul_tag = re.compile(r'</*?ul.*?>', re.S)
    li_tag = re.compile(r'</*?li.*?>', re.S)
    script_tag = re.compile(r'</*?script.*?>', re.S|re.I)
    table_tag = re.compile(r'</*?table.*?>', re.S)
    br_tag = re.compile(r'</*?br.*?>', re.S)

    text = note_tag.sub('', text)
    text = body_tag.sub('', text)
    text = div_tag.sub('', text)
    text = p_tag.sub('', text)
    text = hr_tag.sub('', text)
    text = a_tag.sub('', text)
    text = b_tag.sub('', text)
    text = ul_tag.sub('', text)
    text = li_tag.sub('', text)
    text = script_tag.sub('', text)
    text = table_tag.sub('', text)
    text = br_tag.sub('', text)

    # 将文本进行格式化处理
    tab = re.compile(r'\t', re.S)
    text = tab.sub('', text)  # 用正则表达式删除制表符
    blank_line = re.compile(r'[\n]{3,}', re.S)
    text = blank_line.sub('\n\n', text)  # 用正则表达式将多余空行压缩，但正则表达式无法处理开头空行

    while text[0:1] == "\n":  # 通过片选删除开头空行
        text = text[2:]
    outfile.write(text)

    # 获取网页link
    re_href = re.compile(r'href=.+?</a>')
    href_list = re.findall(re_href, html)
    outfile.write("link:" + "\n")
    for i in href_list:
        anchor_text = re.findall(r'>(.+?)</a>', i)
        link = re.findall(r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')', i)
        outfile.write(anchor_text[0]+" "+link[0]+"\n")
    outfile.close()


def main():
    get_content('http://hlt.suda.edu.cn/~zhli/teach/ir-2016-spring/assignment-3-web-page-content-extraction/2.html', 'Content.txt')


main()
