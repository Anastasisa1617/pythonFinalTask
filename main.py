print ('Вы очнулись в начале апреля 6 семестра бакалавриата. Дедлайн курсача через месяц, у вас нет даже названия')

answer = input ("Что вы хотите делать? (работать блин/плакать/отчисляться): ")
print("Вы выбрали: " + answer)

if answer == "работать блин":
    print('У вас депривация сна, иммунная недостаточность и закрытый дедлайн')

elif answer == "плакать":
    print('Вы улетели на пересдачу, мама расстроилась')

elif answer == "отчисляться":
    print('Последний раз вы были так счастливы в 5 классе')

else:
    print ('Вы умерли от отчаянья')

print("конец игры")