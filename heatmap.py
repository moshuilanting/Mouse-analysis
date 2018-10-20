import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation



def section_count(pose,n):
    m=len(pose)
    unit=int(m/n)
    section_pose=[]
    for i in range(n):
        section=pose.iloc[i*unit:i*unit+unit]

        stand=np.sum(section==labels[0])
        stretch=np.sum(section==labels[1])
        sit=np.sum(section==labels[2])
        turn=np.sum(section==labels[3])
        sleep=np.sum(section==labels[4])
        section_pose.append([stand,stretch,sit,turn,sleep])
    return np.transpose(section_pose)

#绘制热图
def draw_heatmap(pose,min):
    count=section_count(pose,min)
    #print(count)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)
    im = ax.imshow(count, cmap=plt.cm.hot_r)
    plt.title("blank_group heatmap")
    plt.colorbar(im)
    plt.show()



def Statistical_chart(pose):

    stand = np.sum(pose == labels[0])
    stretch = np.sum(pose == labels[1])
    sit = np.sum(pose == labels[2])
    turn = np.sum(pose == labels[3])
    sleep =np.sum(pose==labels[4])
    print(stand,stretch,sit,turn,sleep)
    #画饼图
    sizes=[stand,stretch,sit,turn,sleep]
    colors=["yellowgreen","gold","lightskyblue","red","lightcoral"]
    plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=0)
    plt.axis('equal')
    plt.show()

    #列表形势统计直方图比较快
    pose = list(pose)
    #二维条形直方图
    plt.hist(pose)
    plt.show()

    #时间维度的姿态
    plt.plot(pose)
    plt.show()

    # 姿态变化统计
    change_matrix = np.zeros([5, 5])
    for i in range(0, len(pose) - 1):
        for j in range(0,len(labels)):
            for k in range(0, len(labels)):
                if pose[i] == labels[j] and pose[i + 1] == labels[k]:
                    change_matrix[j][k] += 1

    print(change_matrix)

#轨迹图
def trajectory(x,y):
    plt.xlim(140,550)
    plt.ylim(200,420)
    plt.title('blank_group')
    plt.plot(x,y)
    plt.show()


    def update(n):
        xdata=x[:n]
        ydata=y[:n]
        ln.set_data(list(xdata),list(ydata))
        return ln,
    def init():
        ln.set_data([],[])
        return ln,

    fig = plt.figure()
    ax =fig.add_subplot(111)
    ln, = ax.plot(x,y)
    ani=FuncAnimation(fig,update,init_func=init,frames=len(x),interval=1,blit=False)
    plt.show()


if __name__=='__main__':
    min = 30
    data = pd.read_csv('top_mouse_blank_group_9.27_deal.csv')

    x = data['df_x']
    y = data['df_y']
    pose = data['pose']

    labels = ["stand", "stretch", "sit", "turn", "sleep"]

    draw_heatmap(pose, min)
    Statistical_chart(pose)
    trajectory(x, y)









