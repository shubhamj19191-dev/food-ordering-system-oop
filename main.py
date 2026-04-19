from customer import Customer 
from customer import PremiumCustomer





per1 = Customer(
    'shubham',
    '9712300356',
    'Ahmedabad',
    'shubham3838@gmail.com',
    1000,
   
)
# per1.order_place("pizza",500)
# per1.get_bill(500)
# per1.rate_restaurant(3)




per2 = PremiumCustomer(
    "rahul",
    "456", 
    "surat", 
    "mail2",
     1000
)
per2.order_place("Burger",250)
per2.get_bill(250)
per2.rate_restaurant(5)

