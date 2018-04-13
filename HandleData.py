import jieba.analyse
import numpy as np
from wordcloud import WordCloud
from PIL import Image


# 读取保存的文件，生成词云图
def handle(filename, stopword):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    # jieba 分词
    wordlist = jieba.analyse.extract_tags(data, topK=70)
    wordStr = " ".join(wordlist)
    # 读取图片
    hand = np.array(Image.open('hand.jpg'))
    # 创建wordcloud对象
    my_cloudword = WordCloud(
        background_color = 'black',   # 设置背景颜色
        mask = hand,                  # 设置背景图片
        max_words = 300,              # 设置最大显示的字数
        stopwords = stopword,         # 设置停用词
        max_font_size = 60,            # 设置字体最大值
    )
    # 生成图片
    my_cloudword.generate(wordStr)
    my_cloudword.to_file(filename[:-3] + 'png')
