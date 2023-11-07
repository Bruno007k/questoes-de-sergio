#faça um programa que leia três números e mostre o maior e o menor deles.
n1 = int(input('digite o primeiro número'))
n2 = int(input('digite o segundo número'))
n3 = int(input('digite o terceiro número'))
if n1 > n3 >= n2 or n1 > n2>=n3:
    print("o primeiro é o numero maior entre eles")
elif n2 > n1>=n3 or n2 > n3>=n1:
    print("o segundo é o maior numero")
elif n3 > n1>=n2 or n3 > n2>=n1:
    print('o terceiro é o maior numero')
else:
    print('erro! existe numeros com o mesmo valor')
if n1 < n3 <= n2 or n1 < n2<=n3:
    print("o primeiro é o numero menor entre eles")
elif n2 < n1<=n3 or n2 < n3<=n1:
    print("o segundo é o menor numero")
elif n3 < n1<=n2 or n3 < n2<=n1:
    print('o terceiro é o menor numero')
else:
    print('erro! existe numeros com o mesmo valor')