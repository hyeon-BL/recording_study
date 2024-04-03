import pandas as pd
s = input()
siz = pd.Series((i for i in s), index=range(1, len(s)+1))
siz[3] = 'datascience'
print(siz)