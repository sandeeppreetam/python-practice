def dig(n):
    digits = []
    temp = n
    while temp > 0:
        digits.append(temp%10)
        temp = temp//10
    return digits


def fact(n):
    mul = 1
    while n > 0 :
        mul = mul * n
        n = n-1
    return mul

def f(n):
    sum = 0
    for i in dig(n):
        sum = sum + fact(i)
    return sum

def sf(n):
    sum = 0
    for i in dig(f(n)):
        sum = sum + i
    return sum

print(sf(342))
