# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :

# Unit Price First 100 units 3.5 rs per unit

# Next 100 units Rs 5 per unit

# After 200 units Rs 10 per unit

# after that 15rs per unit

# 1000< meter charge= costing 10%

# tax = costing 9%

# 1000> meter charge= costing 20%

# tax = costing 18%



unit = int(input("Enter number of unit consumed: "))

if unit <= 100:
    # price = 3.5 per unit
    pass
