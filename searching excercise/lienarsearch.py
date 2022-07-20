def linsea (list, x):
    for i in list:
        if i == x:
            return list.index(i)
    return 'noexist'

list = [10,20,30,40,50,60,70,80]
x = 30

print (linsea(list, x))
    
