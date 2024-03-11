from random import shuffle

lst = [i for i in range(1, 101)]
shuffle(lst)

for i in range(10):
    print(lst[10*i: 10*i+10])