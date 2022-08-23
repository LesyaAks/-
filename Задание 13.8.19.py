tickets_number = int(input('Введите необходимое количество билетов: '))
price = 0

for i in range(tickets_number):
    age = int(input('Введите возраст посетителя: '))
    if age < 18:
        print('Посетителям младше 18 лет вход бесплатный')
    elif 18 <= age < 25:
        price += 990
    else:
        price += 1390
    print(f'Общая стоимость билетов: {price} руб.' )

if tickets_number > 3:
    price -= price * 10 // 100
    print(f'При оформлении больше 3-х билетов предоставляется скидка 10%\n'
          f'Сумма к оплате (со скидкой): {price} руб.')
else:
    print(f'Сумма к оплате: {price} руб.')