N = int(input())
cont = 0
for i in range(0,20): # 0 <= i < 20 
    num = int(input())
    if num != -1 :
        if num == N : cont += 1
    else: break
print(str(N) + " aparece " + str(cont) + " vezes")