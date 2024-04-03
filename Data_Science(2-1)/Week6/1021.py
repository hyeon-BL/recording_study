import sys
import pandas as pd

lst = []
while True:
    ss = sys.stdin.readline().rstrip()
    lst.append(ss)
    if ss == '':
        break
for i, v in enumerate(lst):
    lst[i] = v.split()
del lst[-1]
df = pd.DataFrame(lst).T
df.columns = ['Name','Age', 'Gender','Occupation']
df['Age'] = df['Age'].apply(int)
df.index = df.pop('Name')
df.index.name = 'Name'
df = df.replace('nodata','Unemployed')
print(df.sort_values('Age', ascending=False))