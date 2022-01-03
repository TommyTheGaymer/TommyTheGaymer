

#Taxes Calculator

income = input("How much money did you earn? (please do not use a coma) ")
income = int(income)

standardDeduction = "12500"
standardDeduction = int(standardDeduction)

taxableIncome = (income - standardDeduction)
print("Your taxable income is " , taxableIncome)

taxableIncome = int(taxableIncome)

if taxableIncome > 0 and taxableIncome < 9950:
    tierOneOwed = 0 + 0.10 * (taxableIncome - 0)
    print("This year you will be in tax tier 40one, and you will owe " , tierOneOwed)
elif taxableIncome > 9950 and taxableIncome < 40525:
    tierTwoOwed = 995.00 + 0.12 * (taxableIncome -  9950)
    print("This year you will be in tax tier two, and you will owe " , tierTwoOwed)
elif taxableIncome > 40525 and taxableIncome < 86375:
    tierThreeOwed = 4664 + 0.22 * (taxableIncome - 40525)
    print("This year you will be in tax tier three, and you will owe" , tierThreeOwed)
elif taxableIncome > 86375 and taxableIncome < 164925:
    tierFourOwed = 14741 + 0.24 * (taxableIncome - 86375)
    print("This year you will be in tax tier four, and you will owe " , tierFourOwed)
elif taxableIncome > 164925 and taxableIncome < 209425:
    tierFiveOwed = 33603 + 0.32 * (taxableIncome - 164925 )
    print("This year you will be in tax tier five, and you will owe " , tierFiveOwed)
elif taxableIncome > 209425 and taxableIncome < 523600:
    tierSixOwed = 47843 + 0.35 * (taxableIncome - 209425)
    print("This year you will be in tax tier six, and you will owe " , tierSixOwed)
elif taxableIncome >= 523600:
    tierSevenOwed = 157804.25 + 0.37 * (taxableIncome - 523600)
    print("This year you will be in tax tier seven, and you will owe " , tierSevenOwed)

#Refund, Still Owe, or Exact Amount calculator


calc = input("Would you like to calculate if you will recieve a refund or if you still owe money? (Respond with Y or N) ")


def calculatorTwo(calc):
    taxesPaid = input("How much did you pay in taxes? (This question is asking how much you actually paid, not how much you owed, and do not use a coma) ")
    taxesPaid = int(taxesPaid)
    taxesOwed = input("Using the calculation from before, how much did you owe in taxes? (Do not use a coma) ")
    taxesOwed = int(taxesOwed)
    if taxesOwed > taxesPaid:
            stillOwe = taxesOwed - taxesPaid
            print("You still owe money. Specifcally you owe " + stillOwe)
    elif taxesPaid > taxesOwed:
            refund = taxesPaid - taxesOwed
            print("You have overpaid and will recieve a refund. Your refund will be " , refund)
    elif taxesOwed == taxesPaid:
            print("You have paid exactly the correct amount.")




if calc == "Y":
    calculatorTwo(calc)
elif calc == "N":
    exit

