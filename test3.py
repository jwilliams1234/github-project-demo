def fib(end):
    lst = [0,1]
    for i in range(end):
        lst.append(lst[i]+lst[i+1])
    for i in lst:
        print(i)
