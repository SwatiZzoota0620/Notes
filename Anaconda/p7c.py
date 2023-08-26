class purchaseBill:   
    bill_details = {}
    bill_id = 101
    def __init__(self):
        bill_amount = 0
        while True:
            bill_amount = bill_amount + int(input("Enter price of the item: "))
            choice = input("Do you want to add more items(y/n): ")
            if choice == "n":
                card = int(input("how would you like to pay? 1. Cash 2. Credit Card: "))
                purchaseBill.calculateBill(bill_amount,card,18.2)
                break
    def calculateBill(bill_amount,card,pro_charge):
        if card == 2:
            bill_amount += pro_charge
        purchaseBill.disp_bill(bill_amount,purchaseBill.bill_id)
        purchaseBill.bill_id += 1
    def disp_bill(bill_amount,bill_id):
        print("Your Bill Id: ",bill_id)
        print("Your total bill: ",bill_amount)
        purchaseBill.bill_details[bill_id] = {"Amount":bill_amount}

choice = "n"
while True:    
    bill = purchaseBill()
    choice = input("Do you want to enter another bill?(y/n)")
    if choice == "n":
        break
print("Total billing data: ",bill.bill_details)
