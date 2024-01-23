class Math:
    def __init__(self , num1 , num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        # return self.num1 + self.num2
        print(self.num1 + self.num2)


    def sub(self):
        print(self.num1 - self.num2)




obj1 = Math(10,90)
obj1.add()


obj2 = Math(40,50)
obj2.sub()

