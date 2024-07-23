#The script below is to demonstrate two PolicyHolder who have paid for one of the products
# and display their account details.

# For case study like this it is important to first create a products

product1 = Product(name="Life Insurance", description="Covers the family and provides financial support to beneficiaries upon the policyholder's death.")
product2 = Product(name="Health Insurance", description="Provides coverage for medical expenses.")

# Demonstarting Creating a Policy holders
policy_holder1 = PolicyHolder(policyholder_number=1, first_name="Anthony", last_name="Adebanjo", 
                              address="10 Belgrave Street Bryanston, Johannesburg, South Africa", 
                              phone="+27681462946", email="tonybanjo2001@gmail.com")

policy_holder2 = PolicyHolder(policyholder_number=2, first_name="Thabo", last_name="Mthembu", 
                              address="165 West Street Sandton, Johannesburg, South Africa", 
                              phone="+27641546946", email="Mthembu2001@gmail.com")

# Product is being Register with Policy Holders
policy_holder1.register_policyholder(product1)
policy_holder2.register_policyholder(product2)

# Payment is being process for the Policy Holders
payment1 = Payment(policy_holder_id=1)
payment2 = Payment(policy_holder_id=2)

payment1.payment_processing("Visa")
payment2.payment_processing("Mastercard")

# Display Policy Holder Account Details
policy_holder1.get_details()
policy_holder2.get_details()