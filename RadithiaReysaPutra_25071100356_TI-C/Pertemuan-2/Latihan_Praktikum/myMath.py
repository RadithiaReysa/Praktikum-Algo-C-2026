#tambah
def penambahan(a, b):
    return a+b

#kurang
def pengurangan(a, b):
    return a-b

#kali
def perkalian(a, b):
    return a*b

#bagi
def pembagian(a, b):
    if b == 0:
        print("Pembagian tidak dapat dilakukan karena pembagi bernilai 0")
    return a/b

#modulus
def modulus(a, b):
    return a%b

#fibonacci
n = 7
def fibonacci(n):
    
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
for i in range(n):
    print(fibonacci(n-i))
    

