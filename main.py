import random 

class Freelancer:
    def __init__(self,name,money,time,orders):
        self.name = name
        self.money = money
        self.time = time
        self.orders = {}
        
    def show_status(self):
        return f"Фрилансер: {self.name}, Бюджет: ${self.money},Время: {self.time},Заказы: {self.orders} "
    
freelans = Freelancer("Andrey",50,10,"No")
print(freelans.show_status())
        