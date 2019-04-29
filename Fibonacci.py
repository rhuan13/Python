#Fibonacci
n = 0
max = 20
t1 = 0
t2 = 1
print t1, t2
while n <= max:
    termo = t1 + t2
    t1 = t2
    t2 = termo
    print termo,
    n = n + 1
    # 0,1,1,2,3,5,8,13...