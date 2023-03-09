from numpy import inf
import numpy as np
data = [
    {'A': {'B': 2, 'C': 4, 'D':2}},  

    {'B': {'E': 7, 'F': 4, 'G':6},
    'C': {'E': 3, 'F': 2, 'G':4},
    'D': {'E': 4, 'F': 1, 'G':5}},

    {'E': {'H': 1, 'I': 4},
    'F': {'H': 6, 'I': 3},
    'G': {'H': 3, 'I': 3}},

    {'H': {'J': 3},
    'I': {'J': 4}}
]

def DPA_dis(data): #遍歷
    append_lst = []
    for i in data:   # A, {BCD}, {EFG}, {HI} 
        if len(append_lst) == 0:
            for key, val in i.items():
                for key1, val1 in val.items():
                    lst_key = str(key) + str(key1)
                    append_lst.append({lst_key:val1})
        else:
            new_lst = []
            for j in append_lst:
                for key2, val2 in j.items():
                    k = str(key2[-1])
                    
                    i_dict = i[str(k)]
                    for key3, val3 in i_dict.items(): 
                        lst_key = key2 + key3
                        new_lst.append({lst_key: val2 + val3})
            append_lst = new_lst
    return append_lst


def find_best_dis():
    result_lst = DPA_dis(data)
    k_lst = []
    v_lst = []
    for i in result_lst:
        for k, v in i.items():
            k_lst.append(k)
            v_lst.append(v)

    v_min = min(v_lst)
    v_min_idx = v_lst.index(v_min)
    k_min = list(k_lst[v_min_idx])
    

    for j in k_min:
        print(j,end='')
        print('->',end='')

    print(v_min)
find_best_dis()
                
#DPA_floyd(data)
#  A B C D E H G H I J
#A   2 4 2
#B          7 4 6
#C          3 2 4
#D          4 1 5
#E                1 4
#F                6 3
#G                3 3
#H                    3  
#I                    4