A=int(input()) # Uch xonali butun son berilgan. Uning oxirgi raqamini (birlik raqamini) va keyin o'rta raqamini (o'nlik raqamini) chiqaring.
birlik_raqam = A % 10  # Oxirgi raqam (birlik raqami)
onlik_raqam = (A // 10) % 10  # O'rta raqam (o'nlik raqami)
print("Oxirgi raqam (birlik):", birlik_raqam)
print("O'rta raqam (o'nlik):", onlik_raqam)
