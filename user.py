class User:
    def __init__(self,name,phone,city,email):

        self.name = name
        self.phone = phone
        self.email = email
        self.city = city


    def get_info(self):
        print(f'Name: {self.name} | Phone : {self.phone} | City : {self.city} | Email : {self.email}')    



class Customer(User):

    
    def __init__(self,name,phone,city,email,wallet_balance):

     super().__init__(name,phone,city,email)

     self.wallet_balance = wallet_balance
     self.order_history = []  
     
    def add_money(self,money):
       
       self.wallet_balance += money
       print("Money added ! New balance:",self.wallet_balance)

    
    def order_place(self,order,price):
       
       
       
       if self.wallet_balance >=price:
          self.wallet_balance -=price
          self.order_history.append(order)
          print("Order Placed :",order)

       else:
          print("Not enough balance")

    def get_bill(self,amount,del_charge = 30):
        print(f'Total Bill is : {amount} | Delivery charge is : {del_charge}')

        return  amount + del_charge  

    def rate_restaurant(self,rate):
       print("You rated:",rate,"⭐")        





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






