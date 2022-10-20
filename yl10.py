name = input("Mis su nimi on?: ")

print("Tere",name,)

elukoht = input("Kus sa elad?: ")

if elukoht == "Saaremaa":
    print("Imagine sa oled saarlane")

age = int(input("Kui vana sa oled?: "))

if age < 18:
    print("Keri nahhuj tatt")
elif age == 18:
    print("Näe vaata kes viimaks 18 sai!")
elif age > 18:
    print("Noh mine sõitma nüüd")