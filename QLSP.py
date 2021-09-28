def info():
    print("""
    1) Show info
    2) Add product
    3) Modify product's name
    4) Delete product""")

info_prod = [
    {"item": "pen", "cost": 100},
    {"item": "ruler", "cost": 50}
]


def get_info(list):
    print(list)

def add_prod(dict, key, value):
    dict1 = {"item": key, "cost": value}
    dict.append(dict1)

def modify(dict, prod, new_pro):
    for i in dict:
        if i["item"] == prod:
            i["item"] = new_pro

def erase(list, pro):
    for j in range(len(list)):
        if list[j].values() == pro:
            del list[j]

while True:
    info()
    choice = int(input('Choose number to execute: '))
    if choice == 1:
        a = get_info(info_prod)

    elif choice == 2:
        sp = str(input('nhap ten sp: '))
        gia = int(input('nhap gia sp: '))
        b = add_prod(info_prod,sp, gia)
    elif choice == 3:
        sp1 = str(input('nhap ten sp: '))
        gia1 = str(input('nhap ten sp moi: '))
        c = modify(info_prod, sp1, gia1)

    elif choice == 4:
        spxoa = str(input('nhap ten sp can xoa: '))

        erase(info_prod,spxoa)