from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getAllAnni(self):
        return DAO.getAllAnni()

    def getAllBrand(self):
        return DAO.getAllBrand()

    def getAllRetailer(self):
        return DAO.getAllRetailer()

    def handle_topVendite(self, anno, brand, retailer):
        vendite = DAO.handle_topVendite(anno, brand, retailer)
        vendite.sort(key=lambda v: (v.Unit_sale_price*v.Quantity), reverse=True)
        return vendite[:5]

    def handle_analizzaVendite(self, anno, brand, retailer):
        return DAO.handle_analizzaVendite(anno, brand, retailer)

