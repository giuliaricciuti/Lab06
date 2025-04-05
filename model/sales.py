import datetime
from dataclasses import dataclass


@dataclass
class Sales:
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: datetime.datetime
    Quantity: int
    Unit_price: float
    Unit_sale_price: float

    ricavo = None

    def __eq__(self, other):
        return (self.Retailer_code == other.Retailer_code
                and self.Product_number == other.Product_number)

    def __hash__(self):
        return hash((self.Retailer_code, self.Product_number))

    def __str__(self):
        return str(f"Prodotto {self.Product_number} ordinato da {self.Retailer_code} con ricavo {self.ricavo()}")

    def ricavo(self):
        return self.Unit_sale_price*self.Quantity