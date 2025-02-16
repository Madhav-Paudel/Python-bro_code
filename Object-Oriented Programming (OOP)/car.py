class Car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
    def drive(self):
        print(f"You are driving a {self.model}!")
    def stop(self):
        print(f"You are stopped the  {self.model}!")
    def description(self):
        print(f"{self.year}  {self.color} {self.model} {self.for_sale}")
        
