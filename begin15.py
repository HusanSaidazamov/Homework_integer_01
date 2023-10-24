son = int(input("Uch xonali butun sonni kiriting: "))

birinchi_xona = son // 100
ikkinchi_xona = (son // 10) % 10
uchinchi_xona = son % 10

yangi_son = ikkinchi_xona * 100 + birinchi_xona * 10 + uchinchi_xona

print(f"Natija: {yangi_son}")