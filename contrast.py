# coding = utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def bar_graph(contrast_pose,experimental_pose,flag=0):

    labels = ["stand", "stretch", "sit", "turn", "sleep"]

    stand = np.sum(contrast_pose == labels[0])
    stretch = np.sum(contrast_pose == labels[1])
    sit = np.sum(contrast_pose == labels[2])
    turn = np.sum(contrast_pose == labels[3])
    sleep =np.sum(contrast_pose==labels[4])
    contrast_label=[stand,stretch,sit,turn,sleep]

    stand = np.sum(experimental_pose == labels[0])
    stretch = np.sum(experimental_pose == labels[1])
    sit = np.sum(experimental_pose == labels[2])
    turn = np.sum(experimental_pose == labels[3])
    sleep =np.sum(experimental_pose==labels[4])
    experimental_label=[stand,stretch,sit,turn,sleep]

    if flag==1:
        su=sum(contrast_label)
        for i in range(len(contrast_label)):
            contrast_label[i]=contrast_label[i]/su*100
        su=sum(experimental_label)
        for i in range(len(experimental_label)):
            experimental_label[i]=experimental_label[i]/su*100

    width=0.4
    x = list(range(len(labels)))
    plt.bar(x,contrast_label,width=width,label='blank group',fc='y')
    for i in range(len(x)):
        x[i] = x[i] + width
    plt.bar(x,experimental_label,width=width,label='examination',tick_label=labels,fc='r')
    if flag==1:
        plt.ylabel('proportion %')
    plt.title('behavior ratio')
    plt.legend()
    plt.show()

def line_chart(contrast_v,experimental_v):
    plt.plot(contrast_v,label='blank group')
    plt.plot(experimental_v,label='examination')
    plt.title('Speed comparison')
    plt.legend()
    plt.show()





if __name__=='__main__':

    contrast_data=pd.read_csv('top_mouse_blank_group_9.27_deal.csv')
    experimental_data=pd.read_csv('top_mouse_examination_9.27_deal.csv')

    contrast_x=contrast_data['df_x']
    contrast_y=contrast_data['df_y']
    contrast_v= contrast_data['df_v']

    experimental_x=experimental_data['df_x']
    experimental_y=experimental_data['df_y']
    experimental_v= experimental_data['df_v']

    contrast_pose=contrast_data['pose']
    experimental_pose=experimental_data['pose']



    #柱状对比图，flag=1输出占比数据
    bar_graph(contrast_pose, experimental_pose, flag=1)
    line_chart(contrast_v,experimental_v)




