import itchat
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

itchat.login()#登录

friends = itchat.get_friends(update=True)[0:]#获得微信好友列表

man=0#初始化计数器
woman=0
other=0

for friend in friends[1:]:#判断男女
    sex=friend["Sex"]
    if sex==1:
        man+=1
    elif sex==2:
        woman+=1
    else:
        other+=1

#sum=len(friends[1:])#获得总的好友数

#man_proportion=man/sum*100#获得男生的比例
#woman_proportion=woman/sum*100#获得女生的比例
#other_proportion=other/sum*100#h获得没有标注性别的人的比例

#print(round(man_proportion,2))#因为头一次执行时候发现小数点后面余数太多，所以使用round()保留后两位
#print(round(woman_proportion,2))
#print(round(other_proportion,2))

#我在使用饼状图更直观的展示一下

label=['man','woman','other']
x=[man,woman,other]

f=plt.figure()#Create a new figure
plt.pie(x,labels=label,autopct='%1.2f%%')#数据，数据对应的标签，保留两位小数
plt.title('friend proportion')#图片题头

plt.show()#展示图片
