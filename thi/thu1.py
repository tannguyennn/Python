def tinh_tien_dien(so_kw):
    tien_dien = 0
    kw_con_lai = so_kw

    if so_kw <=100:
        tien_dien += so_kw*1500
    elif so_kw <=200:
        tien_dien += (so_kw-100)*1750 + 100*1500
    else:
        tien_dien += (so_kw-200)*2000 + 100*1750 + 100*1500

    return tien_dien

while(True):
    so_kw =int(input("Nhập số điện tiêu thụ (kWh, số nguyên dương): ")) 
    if so_kw>0:
        break

tien = tinh_tien_dien(so_kw)
print(f"Số tiền điện phải trả là: {tien} đồng")
