read = True 
array = []
while read:
    number = int(input())
    if number >= 0 :

        K = 0
        array.clear()

        array.append(number) 
        for i in range(999) :
            n = int(input())
            array.append(n)

        N = int(input())
        for num in array :
            if num == N : 
                K+=1

        print(str(N) + " appeared " + str(K) + " times")
    else: read = False
