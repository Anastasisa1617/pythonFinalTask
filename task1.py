number = int(input("Введите число: "))
k = 0

if number <= 1000:
    for i in range(2, number // 2+1):
        if (number % i == 0):
            k = k+1
    if (k <= 0):
        print("True")
    else:
        print("False")

else: print("Ваше число больше 1000")
