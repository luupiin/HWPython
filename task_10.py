N = int(input('Введите количество монет '))
orel = reshka = 0
for i in range(N):
    x = int(input('Орел или решка? '))
    if x == 1:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(orel)

else:
    print(reshka)