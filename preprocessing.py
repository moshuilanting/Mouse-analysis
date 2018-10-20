import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt



#计算小鼠中心位置
def position(a,b):
    return (a+b)/2
#姿态滤波 增加sleep类型
def pose_shakeoff(x):
    for i in range(1,len(x)-1):
        if x[i]!=x[i-1]:
            flag=0
            if x[i]!=x[i+1]:
                x.iat[i]=x[i-1]
        #增加sleep类型
        if x[i]==x[i-1] and x[i]=='turn':
            flag += 1
            if flag >300:
                x.iat[i-2]= 'sleep'

def remove_errordetect(pose,precent):
    for i in range(1,len(pose)):
        if precent[i]<90:
            pose.iat[i]=np.nan


#除去突变
def remove_mutation(x):
    for i in range(1,len(x)):
        if x[i]-x[i-1]>50 or x[i]-x[i-1]==np.nan:
            x[i]=np.nan
#差分计算速度
def diff_xy(x):
    v=[]
    for i in range(len(x)-1):
        v.append(x[i+1]-x[i])
    return v

header=['x_min','y_min','x_max','y_max','pose','precent']
data = pd.read_csv('top_mouse_blank_group_9.27%.csv',names=header)
data=data[:90000]
x=list(map(position,data.iloc[:,0],data.iloc[:,2]))
y=list(map(position,data.iloc[:,1],data.iloc[:,3]))


#计算在y轴上的最小值
print(y.index(min(y)))

pose = data.iloc[:,4]
precent=data.iloc[:,5]

#识别姿态滤波
pose_shakeoff(pose)
#除去位置突变
remove_mutation(x)
remove_mutation(y)
#除去识别正确率低的点
remove_errordetect(pose,precent)
#计算速度
v_x=diff_xy(x)
v_y=diff_xy(y)
v=list(map(lambda x,y:sqrt(x**2+y**2),v_x,v_y))

#整合
df_x=pd.DataFrame(x,columns=['df_x'])
df_y=pd.DataFrame(y,columns=['df_y'])
df_v=pd.DataFrame(v,columns=['df_v'])
df=df_x.join(df_y)
df=df.join(pose)
df=df.join(df_v)
#除去存在缺失值的数据
df=df.dropna(how='any')

#print(df_v)
#print(pose)

print(df[:71000])
df[20:71000].to_csv('top_mouse_blank_group_9.27_deal.csv',index=False)

