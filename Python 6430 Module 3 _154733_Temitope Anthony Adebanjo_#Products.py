

class Product:
    def __init__(self, name: str, description: str, status="Available"):
        """Name includes the type of insurance, Description contains details about the insurance"""
        self.name = name
        self.description = description
        self.status = status

    def remove_product(self):
        try:
            self.status = "Removed"
            print(f"Product status has been set to {self.status}")
        except Exception as e:
            print(f"An unexpected error occurred while removing the product: {e}")

    def update_product(self, name, description):
        try:
            self.name = name
            self.description = description
            print(f"""Product has been updated with the following details:
            name: {self.name}
            description: {self.description}   
            """)
        except Exception as e:
            print(f"An unexpected error occurred while updating the product: {e}")
