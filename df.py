a = []
i=0
for elem in range (int(input('дай снюс \n'))):
     a.append(str(input()))
     if i%2 == 1:
        a.remove(elem)
        i +=1
        print(a)
