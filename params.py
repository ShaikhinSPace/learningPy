## the {amount} in the funciton below is a parameter
def getmilk(amount):
    vat = amount + 13/100 *amount
    print(f'the original amount is {amount}')
    print(f'the amount with vat is {vat}')
getmilk(1200)