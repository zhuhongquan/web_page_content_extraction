# web_page_content_extraction
简介：用正则表达式去除html源码中的标签，实现网页正文抽取，并按title、body、link分类保存信息<br>


### 使用方法<br>
在主函数def get_content(url, outfile)中输入需要提取的网页url、输出文件名，点击运行即可将网页标题、正文、锚文本及链接保存到文件中。<br>

### 运行效果<br>
测试网页链接为http://hlt.suda.edu.cn/~zhli/teach/ir-2016-spring/assignment-3-web-page-content-extraction/2.html
<br>效果如下
![](https://github.com/zhuhongquan/web_page_content_extraction/raw/master/images/web_page_content_extraction_result.png)


### 注意事项<br>
该程序通过正则表达式匹配HTML标签(例如&lt;table......>&lt;table>&lt;br  ......>&lt;/br>等)并进行剔除，剩下的即为网页上可见的内容，从而实现网页正文抽取。<br>
举例如下：
```Python
note_tag = re.compile(r'<!--.+?-->', re.S)     #匹配注释内容
body_tag = re.compile(r'</*body.*?>', re.S)
div_tag = re.compile(r'</*?div.*?>', re.S)     #匹配div标签
table_tag = re.compile(r'</*?table.*?>', re.S)
br_tag = re.compile(r'</*?br.*?>', re.S)       #匹配br标签

text = note_tag.sub('', text)                  #去掉注释内容
text = body_tag.sub('', text)
text = div_tag.sub('', text)                   #去掉div标签
text = table_tag.sub('', text)
text = br_tag.sub('', text)                    #去掉br标签
```

但程序中只匹配了一些常见的HTML标签，所以对于不同的网页，还需要具体分析。对于代码中未涉及的标签，可以仿照上述代码中的正则表达式进行匹配并剔除。<br>
