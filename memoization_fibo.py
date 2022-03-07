def fibo(k,memo={}):
    if k in memo:
        return memo[k]
    elif k<=2:
        return 1
    memo[k]=fibo(k-1,memo)+fibo(k-2,memo)
    return memo[k]


n=int(input("Enter a Number"))



print(fibo(n))