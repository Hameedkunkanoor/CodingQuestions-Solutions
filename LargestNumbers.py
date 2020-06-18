#to take number of inputs inputs 
totalinputs=int(input())
#to iterate over the number of inputs
for i in range(totalinputs):
    #take two numbers which give total numbers length and top big numbers to be retreived
    totalnumbers,largestnumberrange = map(int, input().split())
    #list to get the numbers
    listtosort = list(map(int, input().split()))
    #sort the list in descending order
    listtosort.sort(reverse=True)
    #print the top most numbers in sorted list
    print(*listtosort[:largestnumberrange], sep=' ')
    # print(listtosort[:largestnumberrange])
    # print(" ".join(str(x) for x in len(listtosort)
    '''

3
4 3
56 94 32 108
4 1
564 732 12 33
7 5
12 8 6 122 33 54 199


    '''

# Enter number 3
# 4 3
# 56 94 32 108
# 108 94 56   output
# 4 1
# 564 732 12 33
# 732 output
# 7 5
# 12 8 6 122 33 54 199
# 199 122 54 33 12