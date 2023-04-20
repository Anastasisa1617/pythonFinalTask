name = "Валера"
result = [1,0,2,1,2,0,1,0,1,1]
fr = 0
i = 0

#print(f"Количество элементов в списке result: {len(result)}")

while i < len(result):
    ng = result[i] / len(result)
    fr += ng

    i = i +1



n = 5
i = 1
fact = 1
per = fact + 1

while i < n:
    fact = fact * (per)
    i = i + 1
    per = per + 1

#print(fact)

name = "Валера"
results = [2,3,4,5,6,7,8,9,3,4]

#for item in range(5):
    #print(name)

s = "In the hole in the ground there lived a hobbit"

#Заменить все h на H, кроме первого и последнего вхождения (кроме самой левой и самой правой)
#find, rfind, replace

first = s.find("h")
#print(first)

last = s.rfind("h")
#print(last)

new = s[first:last]
new = new.replace('h','H')
s = s.replace(s[first:last],new)

#print(s)

#print(new)

#x = input("Введите число: ")

#print(f"Ваше число: {x}. Спасибо")

name = input ("Введите свое имя: ")

print (f"Привет, {name}!")
if name == "Валера":
    print("Эй, это же тот мужик из прошлой темы")
elif name == "Настя" or name == "Анастасия":
    print("Эй, это же мое имя!")

