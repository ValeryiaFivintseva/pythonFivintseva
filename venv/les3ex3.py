def my_func(a, b, c):
        if b > a < c:
            n = b + c
            return n
        elif a > b < c:
            n2 = a + c
            return n2
        elif b > c < a:
            n3 = a + b
            return n3
print(my_func(12, 5, 9))
