son = int(input("Uch xonali butun sonni kiriting: "))

birinchi_xona = son // 100
ikkinchi_xona = (son // 10) % 10
uchinchi_xona = son % 10

o_ng_raqam = uchinchi_xona
uchinchi_xona = birinchi_xona
birinchi_xona = o_ng_raqam

yangi_son = birinchi_xona * 100 + ikkinchi_xona * 10 + uchinchi_xona
yangi_son2=yangi_son//100
print(f"Natija: {yangi_son},{yangi_son2}")