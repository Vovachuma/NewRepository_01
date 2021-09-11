number=29
guess=int(input('введіть число:'))
if guess==number:
    print('ви виграли')
elif guess<number:
    print('загадане число більше')
else:
    print('загадане число менше')
    print('завершено')