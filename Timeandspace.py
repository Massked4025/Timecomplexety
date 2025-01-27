def fun1(n):
    return n*(n+1)/2
print(fun1(6)) #Time complexety = 1

def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(sum)
fun2(6) #Time complexety = 6 n

def fun3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum += 1
    return(sum)
print(fun3(6)) #Time complexety = 36 n*i