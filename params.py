## the {amount} in the funciton below is a parameter
def getmilk(amount, vatPercent):
    vat = amount + vatPercent/100 *amount
    print(f'the original amount is {amount}')
    print(f'the amount with vat is {vat}')
getmilk( vatPercent=2, amount=300)