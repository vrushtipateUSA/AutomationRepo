# When two class have same method name, then preferences will be given to class which object is being created.

class vrushti:
    def __init__(self, num1 ,num2 ):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def multiplication(self):
        return self.num1*self.num2
class jigar:

    def __init__(self,num1, num2, str1, str2):
        super().__init__(num1, num2)
        self.str1 = str1
        self.str2 = str2

    def addition(self):
        return self.str1 + self.str2

objjigar = jigar(20, 80, "good", "morning")
objvrushti = vrushti(40,50)

print(objjigar.addition())

# how to create a object of particular class


#













