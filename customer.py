from user import User


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

