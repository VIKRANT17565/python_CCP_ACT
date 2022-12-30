# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user

quant = int(input("Enter count of products : "))
totalCost = 100*quant
    
finalCost = totalCost
if totalCost > 1000:
    finalCost -= totalCost*0.1


print(finalCost)