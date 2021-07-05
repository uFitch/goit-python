def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print('Какой член ряда Фибоначчи хотите узнать?')
n = int(input())
print (fibonacci(n))

if __name__ == '__main__':
    print("Файл fibo.py запускается напрямую")
else:
    print("Файл fibo.py импортируется в другой модуль")

