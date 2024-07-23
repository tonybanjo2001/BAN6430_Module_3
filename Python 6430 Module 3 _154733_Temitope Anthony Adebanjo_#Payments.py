#Payment
# Create distinct class
#Implement methods for payment processing, reminders, and penalties

class Payment:
    def __init__(self, policy_holder_id: int, status: str = "Not Paid"):
        self.policy_holder_id = policy_holder_id
        self.status = status

    def payment_processing(self, payment_method: str):
        """Payment Method includes but not limited to Electronic Transfer, Debit Card, Credit Card"""
        try:
            self.status = "Paid"
            print(f"Payment processed using {payment_method}. Status set to {self.status}.")
        except Exception as e:
            print(f"An unexpected error occurred while processing the payment: {e}")

    def remind_policy_holder(self):
        try:
            if self.status == "Not Paid":
                print(f"Reminder! Your payment status is {self.status}. Pay to avoid service interruption!")
            else:
                print(f"Reminder! Your payment status is {self.status}.")
        except Exception as e:
            print(f"An unexpected error occurred while sending a reminder: {e}")

    def apply_penalty(self):
        try:
            assert self.status == "Not Paid", "The policyholder is a paid user, cannot apply penalty"
            print(f"Penalty applied to policyholder {self.policy_holder_id}.")
        except AssertionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while applying the penalty: {e}")
