
class Personel:
    def __init__(self,name,age) :
        self.Name =name
        self.Age=age
        self.__Salary=None

    def printInfo(self):
        print("Name:{}, Age:{}".format(self.Name,self.Age))
    
if __name__ =='__main__':
    p1=Personel('Tony',35)
    p1.printInfo()
    print(p1.Name)
    print(p1._Personel__Salary)