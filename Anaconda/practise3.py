from datetime import datetime
class CUSTOMER:
    cust_data = {}
    cust_id = 1001
    count = 1
    def __init__(self,orig = None):
        if orig == None:
            while True:
                self.first_name = input("Enter the first name: ")
                self.last_name = input("Enter the last name: ")
                self.name = self.first_name+" "+self.last_name
                if CUSTOMER.nameValidator(self) == True:
                    break
            self.mob_num = input("Enter the mobile number: ")
            CUSTOMER.store_data(self)
        else:
            self.copy_constructor(orig)
    def copy_constructor(self,orig):
        return orig
    def store_data(self):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M")
        CUSTOMER.cust_data[CUSTOMER.cust_id] = [{"Name":self.name},{"Mobile number":self.mob_num},{"Entry time":date_time}]
        CUSTOMER.cust_id +=1
        self.count+=1
    def nameValidator(self):
        if len(self.name)-1 < 3:
            print("Name too short")
            return False
        elif len(self.name)-1 > 20:
            print("Name too long")
            return False
        else:
            return True
    def no_of_changes(self):
        print(self.count," customer(s) added to the database.")
while True:
    obj = CUSTOMER() 
    if input("want to add new customer(y/n): ") == "n":
        break
obj.no_of_changes()
for item,value in obj.cust_data.items():
    print("customer ID: ",item)
    print("Data: ",value) 
ob = CUSTOMER(obj)

