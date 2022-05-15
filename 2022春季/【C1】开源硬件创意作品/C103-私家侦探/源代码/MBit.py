
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


sX,sY=[],[]
destine=r''+input('Input the absolute route of \'position.txt\' file: ')

with open(destine, 'r') as source:
    head=True
    for line in source:
        if head:
            head=False
        else:
            lineinfo = line.split('/')
            print(lineinfo)
            sX.append(float(lineinfo[1][:-1]))
            sY.append(float(lineinfo[0]))


fig = plt.figure()  # 创建图
yGap=max(sY)-min(sY)
xGap=max(sX)-min(sX)
plt.ylim(min(sY)-0.1*yGap, max(sY)+0.1*yGap)  # Y轴取值范围
#plt.yticks([-12 + 2 * i for i in range(13)], [-12 + 2 * i for i in range(13)])  # Y轴刻度
plt.xlim(min(sX)-0.1*xGap,max(sX)+0.1*xGap)  # X轴取值范围
#plt.xticks([0.5 * i for i in range(14)], [0.5 * i for i in range(14)])  # X轴刻度

plt.title("Track")   # 标题
plt.xlabel("EAST-->")  # X轴标签
plt.ylabel("NORTH-->")  # Y轴标签
x, y = [], []  # 用于保存绘图数据，最开始时什么都没有，默认为空


def update(n):  # 更新函数
    x.append(sX[n])  # 添加X轴坐标
    y.append(sY[n])  # 添加Y轴坐标
    plt.plot(x, y, linestyle="--",color='forestgreen')  # 绘制折线图
    #plt.scatter(sX[n],sY[n],marker='>')


ani = FuncAnimation(fig, update, frames=np.arange(len(sX)), interval=5, blit=False, repeat=False)  # 创建动画效果
plt.show()  # 显示图片
savepath=input('Input the saving path: ')
ani.save(r''+savepath+'track.gif')
