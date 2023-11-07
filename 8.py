n1 = int(input('qual o preço do primeiro produto'))
n2 = float(input('qual o preço do segundo produto'))
n3 = float(input('qual o preço do terceiro produto'))
if n1 < n3 <= n2 or n1 < n2<=n3:
    print("recomendo comprar o primeiro produto pois é mais barato")
elif n2 < n1<=n3 or n2 < n3<=n1:
    print("recomendo comprar o segundo produto pois é mais barato")
elif n3 < n1<=n2 or n3 < n2<=n1:
    print('recomendo comprar o terceiro produto pois é mais barato')
else:
    print('existe produtos com o mesmo valor! nesse caso você deve optar por escolher um desses produtos')