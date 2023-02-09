I = input()
num = []
sinal = 1

for i in I :
    if i == '-':
        sinal = -1
    elif i != ' ':
        num.append(int(i)*sinal)
        sinal = 1

if num[0] > num[1]:
    print(str(num[1]) + ' ' + str(num[0]))
else:
    print(str(num[0]) + ' ' + str(num[1]))