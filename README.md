# weibo_analysis
python爬虫自动爬取指定用户的原创微博和图片，并对微博进行归类分析，最后以html图表的形式展示。

首先得到你要爬取的user_id和你的cookie，填入到weibo.py中。（获取方法见我的博客园博客）http://www.cnblogs.com/dmyu/ 

运行weibo.py，即可生成你要爬取的user_id为名字的原创微博内容文档和存有所有图片链接的文件，之后会对所有图片链接进行爬取，图片存到weibo_image文件夹中。

之后运行analysis.py，填入user_id，即可对刚才爬到的微博内容进行分析。（要去掉前两行微博名字和简介）

分析的内容有微博分类、最常使用表情和次数、最常使用词语和次数、微博中的人名及出现次数。

之后用xita.html的h5格式即可生成饼状图，可以很直观的观看了。（调用了google的api，可能要翻墙才看得到）
