num = input('Enter a three-digit number: ')
res = 0
if len(num) == 3:
    for i in num:
        res += int(i)
    print(res)
else:
    print('You entered a non-three-digit number')