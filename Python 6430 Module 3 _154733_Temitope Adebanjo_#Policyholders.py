#Policyholders
# Create a class
#Implement methods to register, suspend, and reactivate policyholders.
#Create at least two policyholders who have paid for one of the 
#products and display their account details

class PolicyHolder:
    """Class representing a policyholder"""

    def __init__(self, policyholder_number, first_name, last_name, address, phone, email):
        self.policyholder_number = policyholder_number
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email
        self.status = "Active"
        self.policies = []

    def register_policyholder(self, product):
        if self.status == "Active":
            self.policies.append(product)
            print(f"Policy {product.product_id} added for a active policyholder {self.policyholder_number}.")
        else:
            print(f"Policyholder {self.policyholder_number} is not active.")

    def suspend_policyholder(self):
        self.status = "Suspended"
        print(f"Policyholder {self.policyholder_number} has been suspended.")

    def reactivate_policyholder(self):
        self.status = "Active"
        print(f"Policyholder {self.policyholder_number} has been reactivated.")
        
    def get_details(self):
        return {
            "Policyholder_ID_Number": self.policyholder_number,
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Address": self.address,
            "Phone": self.phone,
            "Email": self.email,
            "Status": self.status,
            "Policies": [policy.product_id for policy in self.policies]
        }
    def print_details(self):
        print(self.get_details())