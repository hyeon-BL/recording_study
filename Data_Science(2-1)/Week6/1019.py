import sys
import pandas as pd
import numpy as np

lst = []
while True:
    ss = sys.stdin.readline().rstrip()
    lst.append(ss)
    if ss == '':
        break
for i, v in enumerate(lst):
    lst[i] = v.split()
del lst[-1]
nlst = np.array(lst)
nlst.T
dic = {'Name':nlst[0],'Age':list(map(int,nlst[1])),'Gender':nlst[2]}
df = pd.DataFrame(dic, columns=['Age', 'Gender'])
df.index = dic['Name']
df.index.name = 'Name'
print(df[df['Age']>=30])