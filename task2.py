n = int(input("Сколько чисел в вашем списке? "))
spisok = []

for i in range(n):
    x = int(input("Число = "))
    if (i == 0) or (x > spisok[- 1]):
        spisok.append(x)
    else:
        pos = 0
        while pos < len(spisok):
            if x <= spisok[pos]:
                spisok.insert(pos, x)
                break
            pos = pos + 1

print(f"Ваш отсортированный список: ", spisok)