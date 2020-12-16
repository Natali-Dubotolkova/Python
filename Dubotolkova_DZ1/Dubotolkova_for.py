def Fib(n):
    a = 1
    b = 0
    A = 0
    for _ in range (n):
        A = a + b
        a = b
        b = A
    return A

def Fib3(N):
    a = 1
    b = 1
    c = 1
    if N == 1 or N == 2 or N == 3:
        return 1
    for i in range(4, N + 1):
        n = a + b + c
        a = b
        b = c
        c = n
    return n

    return A

def square_odd(n):
    l = [(i*2+1)**2 for i in range (n)]
    return l

def sum_mult_A_to_B(a,b):
    sum = 0
    mult = 1
    for i in range(a,b+1):
        sum+=i
        mult*=i
    return sum, mult

def even_odd_A_to_B(a,b):
    even = [i for i in range(a,b+1) if i%2 == 0]
    odd = [i for i in range(a, b + 1) if i%2 != 0]
    return  even, odd

def sort_numb(l):
    positive = [i for i in l if i > 0]
    negative = [i for i in l if i <= 0]
    return positive, negative

if __name__ == '__main__':
    print("For 1:")
    print(Fib(5))
    print("For 2:")
    print(Fib3(5))
    print("For 3:")
    print(square_odd(10))
    print("For 4:")
    A,B = sum_mult_A_to_B(1,5)
    print("Сумма:", A, "Произведение:", B)
    print("For 5:")
    A, B = even_odd_A_to_B(11, 43)
    print("Чётные:", A)
    print("Нечётные:", B)
    print("For 6:")
    l = [1,5,9,10,-11,-56,-9, 65, 15, -87,-98,3,8,-2]
    A, B = sort_numb(l)
    print("Положительные:", A)
    print("Отрицательные:", B)