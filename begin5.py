A =int(input())
B =int(input())
segments_count = A // B  # A segmentiga joylashtirilgan B segmentlari miqdori a>b dan
unused_length = A % B   # A segmentining foydalanilmagan qismi uzunligi
print("B segmentlari miqdori:", segments_count)
print("Foydalanilmagan qismi uzunligi:", unused_length)