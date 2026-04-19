from customer import Customer 




per1 = Customer(
    'shubham',
    '9712300356',
    'Ahmedabad',
    'shubham3838@gmail.com',
    1000,
   
)

per1.get_info()

per1.add_money(50)
per1.order_place("pizza",500)
per1.get_bill(500)
per1.rate_restaurant(3)