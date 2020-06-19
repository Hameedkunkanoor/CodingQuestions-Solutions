#to take number of inputs inputs 
totalinputs=int(input())
#to iterate over the number of inputs
for i in range(totalinputs):
    #size of list
    totalnumbers=int(input())
    #list to get the numbers
    listtosort = list(map(int, input().split()))
    #sort the list in ascending order
    listtosort.sort()
    for i in range(0,len(listtosort)-2):
       if(listtosort[i]**2+listtosort[i+1]**2==listtosort[i+2]**2):
           print("YES")
           exit(0)
    print("NO")
    exit(0)
   
    #print the top most numbers in sorted list
    # print(*listtosort[:largestnumberrange], sep=' ')
    # print(listtosort[:largestnumberrange])
    # print(" ".join(str(x) for x in len(listtosort)



'''
2
4
4 3 5 6   #Yes
3
3 5 1    #No
'''