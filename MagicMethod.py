class bike:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def __str__(self):
        return (f"name = {self.name},color = {self.color}")
    def display(self):
        print(f"name = {self.name},color = {self.color}")

bike1 = bike("Bhimcharan Bhakta","red")
bike2 = bike("Mahakal2001","black")

print(bike1)
print(bike2)