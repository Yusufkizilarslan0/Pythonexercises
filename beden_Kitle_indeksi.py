print("""*************************

Beden Kitle İndeksi Hesaplama (bki)



************************
	""")

kilo = float(input("Lütfen Kilonuzu giriniz:"))
boy = float(input("Lütfen boyunuzu giriniz:"))

bki =  kilo / (boy ** 2)

if (bki < 18.5):
	print("Zayıf")
elif ( 18.5 <= bki < 25):
	print("Normal")
elif (25 <= bki < 30):
	print("Fazla Kilolu")
else:
	print("Obez")