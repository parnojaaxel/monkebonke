a = int(input ("Esimene number : "))
b = int(input ("Teine number: "))

def bonke(a, b):
      
    if a <= b:
        return a
    else:
        return b
      
print(bonke(a, b))