from datetime import datetime

class NhanVien:
    def __init__(self, maso, nam_sinh):
        self.maso = maso
        self.nam_sinh = nam_sinh

    def tinh_tuoi(self):
        nam_hien_tai = datetime.now().year
        return nam_hien_tai - self.nam_sinh

    def hien_thi_thong_tin(self):
        tuoi = self.tinh_tuoi()
        print("Mã số: {}, Năm sinh: {}, Tuổi: {}".format(self.maso,self.nam_sinh,tuoi))
    
def nhap_danh_sach_nhan_vien(n):
    danh_sach_nhan_vien = []
    for i in range(n):
        maso = input(f"Nhập mã số nhân viên thứ {i + 1}: ")
        nam_sinh = int(input(f"Nhập năm sinh của nhân viên thứ {i + 1}: "))
        nhan_vien = NhanVien(maso, nam_sinh)
        danh_sach_nhan_vien.append(nhan_vien)
    return danh_sach_nhan_vien

def in_danh_sach_nhan_vien(danh_sach_nhan_vien):
    for nhan_vien in danh_sach_nhan_vien:
        nhan_vien.hien_thi_thong_tin()

def sap_xep_theo_tuoi_giam_dan(danh_sach_nhan_vien):
    danh_sach_nhan_vien.sort(key=lambda nv: nv.tinh_tuoi(), reverse=True)
    
def main():
    n = int(input("Nhập số lượng nhân viên: "))
    danh_sach_nhan_vien = nhap_danh_sach_nhan_vien(n)
    print("\nDanh sách nhân viên:")
    in_danh_sach_nhan_vien(danh_sach_nhan_vien)
    
    sap_xep_theo_tuoi_giam_dan(danh_sach_nhan_vien)
    print("\nDanh sách nhân viên theo thứ tự tuổi giảm dần:")
    in_danh_sach_nhan_vien(danh_sach_nhan_vien)

if __name__ == "__main__":
    main()
