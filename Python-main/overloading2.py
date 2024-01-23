class area:
    def find_area(self,x=None,y= None):
        if(x!=None and y!=None):
            print(x*y)

        elif(x!=None):
            print(x*x)

        else:
            print("nothing")


a = area()
a.find_area()
a.find_area(4)
a.find_area(2,3)
