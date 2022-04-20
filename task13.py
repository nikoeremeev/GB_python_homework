# Задача №13: Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.


str1 = input("Введите первую строку для проверки:")
str2 = input("Введите вторую строку для поиска в первой строке:")

# первый способ
print(f"Вторая строка входит в первую {str1.count(str2)} раз(а).")

# второй способ
count = 0
for i in range(len(str1) - len(str2)):
    if str2 in str1[i:i+len(str2)]:
        count += 1
print(f"Вторая строка входит в первуюф {count} раз(а).")