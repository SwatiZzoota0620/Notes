class CUSTOMER:
    cust_data = {}
    cust_id = 1001
    def __init__(self):   
        while True:
            self.name = input("Enter the name: ")
            if CUSTOMER.nameValidator(self) == True:
                   break
        self.mob_num = input("Enter the mobile number: ")
        CUSTOMER.store_data(self)
    def store_data(self):
        CUSTOMER.cust_data[CUSTOMER.cust_id]=[{"Name":self.name},{"Mobile number":self.mob_num}]
        CUSTOMER.cust_id +=1
    def nameValidator(self):
        if len(self.name) < 3:
            print("Name too short")
            return False
        elif len(self.name) > 20:
            print("Name too long")
            return False
        else:
            return True

while True:
    obj = CUSTOMER() 
    if input("want to add new customer(y/n): ") == "n":
        break
for item,value in obj.cust_data.items():
    print("customer ID: ",item)
    print("Data: ",value)

  
        
    