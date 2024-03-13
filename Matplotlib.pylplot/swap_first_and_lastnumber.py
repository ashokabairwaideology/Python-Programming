def swaplist(newlist):
     size = len(newlist)


     #swap
     temp = newlist[0]
     newlist[0] = newlist[size-1]
     newlist[size - 1] = temp

     return newlist



newlist = [9,8,6,2,1,4,7]
print(swaplist(newlist))



#another method

def swaplist1(newlist1):
     newlist1[0] , newlist1[-1] =newlist1[-1] , newlist1[0]
     return newlist1


newlist1 = [6,5,8,2,9,2,69]
print(swaplist1(newlist1))


