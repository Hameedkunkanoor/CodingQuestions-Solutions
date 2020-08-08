#  longest substring without repeating characters
# input asddfghjill
# output dfghjil
# input fedoret
# output fedor
def find_longest_substring(inputstring) :
    if inputstring is None :
        return ""
    startindex=0
    movingindex=0
    longestsubstring=""
    stringset=[]
    for i in range(0,len(inputstring)):
        movingindex+=1
        
        if inputstring[i] not in stringset :
            stringset.append(inputstring[i])
            if(len(stringset)>len(longestsubstring)):
             longestsubstring=inputstring[startindex:movingindex]
            continue
        while startindex<movingindex-1 :
            stringset.remove(inputstring[startindex])
            startindex+=1
            print(stringset)
    print(longestsubstring)
Inputstr = str(input("Enter a string: "))
find_longest_substring(Inputstr)