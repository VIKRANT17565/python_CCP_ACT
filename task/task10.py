# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:

# Cost price (in Rs) Tax

# > 1,00,000 15 %

# > 50,000 and <= 1,00,000 10%

# <= 50000 5%

cpOfBike = int(input("Enter the Cost price of your bike : "))

# roadTax = 
if cpOfBike > 100000:
    roadTax = cpOfBike*0.15

elif cpOfBike > 50000 and cpOfBike <= 100000:
    roadTax = cpOfBike*0.1

elif cpOfBike <= 50000:
    roadTax = cpOfBike*0.05


print("Your road tax :", roadTax)