

# outer class
class LapTop:
    def __init__(self,model):
        self.Model = model
        self.Bat = self.Battery('LG','BT12345','55kwh')
    def printInfo(self):
        print(self.Model)
        self.Bat.printInfo()
    # định nghĩa lớp Battery(inner class)
    class Battery:
        def __init__(self,mf,model,capacity) :
            self.Manufacture=mf
            self.Model=model
            self.Capacity = capacity
        def printInfo(self):
            print('Manufacture: {}, Capacity: {}'.format(self.Manufacture,self.Capacity))

if __name__ == '__main__':
    lap1 = LapTop('Dell')
    lap1.printInfo()