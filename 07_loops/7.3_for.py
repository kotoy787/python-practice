# Как работает FLAG
flag = True   # флажок поднят

while flag:   # пока флажок True, цикл работает
    text = input("Введите слово (или 'стоп'): ")
    if text == "стоп":
        flag = False   # опускаем флажок → цикл остановится
    else:
        print("Вы ввели:", text)