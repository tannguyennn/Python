class Student:
    # Hàm thiết lập
    def __init__(self,id,name,grade) :
        self.id=id
        self.name=name
        self.grade=grade


sv1 = Student("63132204","Nguyễn Tấn Lập",8.9)

print(sv1.id)
print(sv1.name)
print(sv1.grade)