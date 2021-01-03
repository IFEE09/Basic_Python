#This is our first programm and this is a USD To MXN converter

setup = """
    Welcome to the currency converter $ 
    1 - Mexican Pesos
    2 - Colombian pesos

    - Choose one please:
"""
option = int(input(setup))

valueMxInDollars = 20
valueColInDollars = 3400

if option == 1:
    currencyMX = input("how many Mexican Pesos do you have?: ")
    currencyMX = float(currencyMX)
    currencyUSD = currencyMX/valueMxInDollars
    currencyUSD = round(currencyUSD,2)
    currencyUSD = str(currencyUSD)
    print("You have " + currencyUSD + " US Dollars") #Here currencyUSD is a String
elif option == 2:
    currencyCol = input("how many Colombian Pesos do you have?: ")
    currencyCol = float(currencyCol)
    currencyUSD = currencyCol/valueColInDollars
    currencyUSD = round(currencyUSD,2)
    print("You have " , currencyUSD , " US Dollars") #Here currencyUSD is a float
else:
    print("invalid option, restart and try again")