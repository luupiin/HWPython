S = int(input("Введите общее количество журавликов: "))
if not S % 6:
     a = S // 6
     print(f'Катя {a * 4} ')
     print(f'Сережа {a} ')
     print(f'Петя {a}')