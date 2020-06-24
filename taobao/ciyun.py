from wordcloud import WordCloud

import codecs

import jieba

# from scipy.misc import imread
import imageio
import os

from os import path

import matplotlib.pyplot as plt

from PIL import Image,ImageDraw,ImageFont

def daw_wordclod():
    # 读入一个txt 文件
    comment_text = open(r'./content.txt','r',encoding='UTF-8').read()

    # jieba 分词过滤

    cut_text= " ".join(jieba.cut(comment_text))

    # print(cut_text)
    # 当前所在目录
    d = path.dirname(__file__)
    color_mark = imageio.imread(r"C:\Users\13265\Desktop\tt.png")
    # 设置字体，不指定会乱码
    cloud = WordCloud(
        font_path=os.environ.get('FONT_PATH',os.path.join(os.path.dirname(__file__),"simkai.ttf")),
        prefer_horizontal=1.0,
        background_color= 'black',
        # relative_scaling=0.8,#词频和字体大小的关联性
        max_words=1000,
        min_font_size=10,
        max_font_size=45
    )
    word_cloud = cloud.generate(cut_text)  # 产生词云
    word_cloud.to_file('cy_pl2.jpg')
    # 显示词云图片
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()

    plt.close()

if __name__ == '__main__':
    daw_wordclod()

