#prim algorithm 

from numpy import inf
import random

graph = [
    [0, 4, 4, 0, 0, 0],#A
    [4, 0, 2, 0, 0, 0],#B
    [4, 2, 0, 3, 2, 4],#C
    [0, 0, 3, 0, 0, 3],#D
    [0, 0, 2, 0, 0, 3],#E
    [0, 0, 4, 3, 3, 0] #F    
]

node = [chr(i) for i in range(65, 71)]

def prim(data):

    def min_edge(select,candidate,data):
        Min = float(inf)          #記錄最小邊權重
        v,u = 0,0                 #記錄最小邊
        for i in select:        #掃描已選vertex和備選vertex，尋找最小邊      
            for j in candidate:
                if data[i][j] < Min and data[i][j]!=0:   
                    Min = data[i][j]
                    v,u = i,j
        return v,u              #返回記錄的最小邊的兩個vertex
    
    def calculate(data):
        vertex_num = len(data) #vertex個數
        select = [0] #初始vertex，默認從第一個點開始
        candidate = list(range(1,vertex_num)) #未選vertex
        edge=[] #儲存每次搜索到的邊
        for i in range(1,vertex_num):  #連接n點需要n-1條邊
            v,u = min_edge(select,candidate,data) #已選vertex的最小邊的兩個頂點
            string=str(node[v])+'-'+str(node[u])+':'+str(data[v][u])
            edge.append(string)
            select.append(u)
            candidate.remove(u)
        return edge

    return calculate(data)

for i in prim(graph):
    print(i)
