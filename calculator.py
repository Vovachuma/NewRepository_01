a = int(input('enter a'))
dija = input('enter dija:')
b= int(input('enter b:'))
if dija == '+':
    print(a+b)
elif dija == '-':
    print(a-b)
elif dija == '*':
    print(a*b)
elif dija =='/' and b!=0:
    print(a/b)
else:
    print('Ділення на 0 неможливе')