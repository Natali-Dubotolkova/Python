def Celsius_to_Farenheit(deg):
    return deg*1.8+32
def Farenheit_to_Celsius(deg):
    return (deg - 32)/1.8
def Ml_to_km(x):
    return x*1.609
def km_to_Ml(x):
    return x/1.609
def oz_to_g(x):
    return x*28.35
def g_to_oz(x):
    return x/28.35
def Convert_degrees():
    print("Конвертируем градусы.\n"
          "Введите 1, если хотите перевести градусы Фаренгейта в градусы Цельсия.\n"
          "Введите 2, если хотите перевести градусы Цельсия в градусы Фаренгейта")
    variant = input()
    try:
        variant = int(variant)
    except:
        print("Введите число")
    variant = int(variant)
    if (variant != 1) and (variant != 2):
        raise print("Введите 1 или 2")
    print("Введите градусы")
    deg = input()
    try:
        deg = float(deg)
        if variant == 1:
            print("Ответ:",Farenheit_to_Celsius(deg))
        elif variant == 2:
            print("Ответ:",Celsius_to_Farenheit(deg))
    except:
        try:
            deg = int(deg)
            if variant == 1:
                print("Ответ:",Farenheit_to_Celsius(deg))
            elif variant == 2:
                print("Ответ:",Celsius_to_Farenheit(deg))
        except:
            print("Введите число")
def Convert_distance():
    print("Конвертируем расстояние.\n"
          "Введите 1, если хотите перевести мили в километры.\n"
          "Введите 2, если хотите перевести километры в мили")
    variant = input()
    try:
        variant = int(variant)
    except:
        print("Введите число")
    variant = int(variant)
    if (variant != 1) and (variant != 2):
        raise print("Введите 1 или 2")
    print("Введите расстояние")
    dict = input()
    try:
        dict = float(dict)
        if variant == 1:
            print("Ответ:",Ml_to_km(dict))
        elif variant == 2:
            print("Ответ:",km_to_Ml(dict))
    except:
        try:
            dict = int(dict)
            if variant == 1:
                print("Ответ:",Ml_to_km(dict))
            elif variant == 2:
                print("Ответ:",km_to_Ml(dict))
        except:
            print("Введите число")
def Convert_weight():
    print("Конвертируем вес.\n"
          "Введите 1, если хотите перевести унции в граммы.\n"
          "Введите 2, если хотите перевести граммы в унции")
    variant = input()
    try:
        variant = int(variant)
    except:
        print("Введите число")
    variant = int(variant)
    if (variant != 1) and (variant != 2):
        raise print("Введите 1 или 2")
    print("Введите вес")
    weig = input()
    try:
        weig = float(weig)
        if variant == 1:
            print("Ответ:",oz_to_g(weig))
        elif variant == 2:
            print("Ответ:",g_to_oz(weig))
    except:
        try:
            weig = int(weig)
            if variant == 1:
                print("Ответ:",oz_to_g(weig))
            elif variant == 2:
                print("Ответ:",g_to_oz(weig))
        except:
            print("Введите число")


if __name__ == '__main__':
    print("Данная программа конвертирует значения из одной системы в другую \n"
          "1: Температура \n"
          "2: Расстояние \n"
          "3: Вес \n"
          "Ваш выбор:")
    var = input()
    try:
        var = int(var)
    except:
        print("Введите число")
    var = int(var)
    if (var != 1) and (var != 2) and (var != 3):
        raise print("Введите 1, 2 или 3")
    if var==1:
        Convert_degrees()
    if var==2:
        Convert_distance()
    if var==3:
        Convert_weight()