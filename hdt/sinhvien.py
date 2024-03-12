class Student:
    # Hàm thiết lập
    def __init__(self,id,name,grade) :
        self.id=id
        self.name=name
        self.grade=grade
    #in thông tin
    def print_info(self):
        print("ID: "+self.id)
        print("Name: "+self.name)
        print("Grade: "+str(self.grade))

sv1 = Student("63132204","Nguyễn Tấn Lập",8.9)

sv1.print_info()