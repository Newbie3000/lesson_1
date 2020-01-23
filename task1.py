# Author Kuznetcov Ivan
print("Task 1")
# Поработайте с переменными, создайте несколько, выведите
# на экран, запросите у пользователя несколько чисел и
# строк и сохраните в переменные, выведите на экран.
import datetime

now = datetime.datetime.now()
print("Сейчас:", (now.strftime("%d-%m-%Y %H:%M")))
name = input("Как Вас зовут?: ")
age = int(input("Сколько Вам лет?: "))
print("Ты хочешь стать Devops-инженером?(да/нет):")
answer = input()
if answer == "да":
    if age >= 30:
        print('Где же ты был раньше? Все равно молодец!')
    elif age < 30:
        print('Ну ты просто красавчик!')
elif answer == "нет":
    print('Просто нажми крестик')
123141
