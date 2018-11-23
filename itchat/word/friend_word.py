import itchat
import re
import os
import jieba
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import PIL.Image as Image

# 登录
itchat.login()
#获取好友列表
friends=itchat.get_friends(update=True)[0:]
tlist=[]
for i in friends:
    signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    rep=re.compile('1f\d.+')
    signature=rep.sub('',signature)
    tlist.append(signature)
#拼接字符串
text=''.join(tlist)

#jieba分词
wordlist=jieba.cut(text,cut_all=True)
wl_split=' '.join(wordlist)

#wordcloud 词云
color=np.array(Image.open(os.path.join('C:\\','timg.jpg')))

my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=color,
                         max_font_size=40, random_state=42,
                         font_path='C:/Windows/Fonts/simhei.ttf')\
    .generate(wl_split)
image_color=ImageColorGenerator(color)
plt.imshow(my_wordcloud.recolor(color_func=image_color))
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()

#保存图片，并发送到微信手机助手里
my_wordcloud.to_file(os.path.join('C:\\','python.png'))
itchat.send_image('C:\\python.png','filehelper')