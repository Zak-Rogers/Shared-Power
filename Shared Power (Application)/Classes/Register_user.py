import re

class Register_User:

    
    first_Name = ""
    last_Name = ""
    user_Name = ""
    #password =""
    email = "my@gmail.com"
    phone_Number =""
    address_Line =""
    city =""
    postcode=""
    
    supplier = False #boolen



    def add_user_info(self,First,Last,User,Email,Phone,Address,City,Postcode,Supplier):
        self.first_Name = First
        self.last_Name = Last
        self.user_Name = User
        self.email = Email
        self.phone_Number = Phone
        self.address_Line = Address
        self.city = City
        self.postcode = Postcode
        self.supplier = Supplier
        
   
    def get_name (self):
            Name = self.first_Name +" "+ self.last_Name
            return Name


    


    






    
