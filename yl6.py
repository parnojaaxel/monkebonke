
a = int(input("Lisa esimene number:"))
b = int(input("Lisa teine number:"))
c = int(input("Lisa kolmas number:"))

def loli(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
  
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
          
    return largest

print(loli(a, b, c))