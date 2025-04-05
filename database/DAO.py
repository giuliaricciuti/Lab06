from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.sales import Sales


class DAO():
    #tutti metodi static

    @staticmethod
    def getAllAnni():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor()
            query = """SELECT COALESCE(YEAR(gds.`Date`), 0) AS Anno
                        FROM go_daily_sales gds 
                        GROUP BY COALESCE(YEAR(gds.`Date`), 0)"""
            cursor.execute(query)
            for row in cursor:
                res.append(row[0])
            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getAllBrand():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor()
            query = """SELECT COALESCE(gp.Product_brand) AS Brand
                        FROM go_products gp  
                        GROUP BY COALESCE(gp.Product_brand)"""
            cursor.execute(query)
            for row in cursor:
                res.append(row[0])
            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getAllRetailer():
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                        FROM go_retailers"""
            cursor.execute(query)
            for row in cursor:
                res.append(Retailer(**row))
            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def handle_topVendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT gds.Retailer_code, 
                            gds.Product_number, 
                            gds.Order_method_code, 
                            gds.`Date` , 
                            gds.Quantity, 
                            gds.Unit_price, 
                            gds.Unit_sale_price
                        FROM go_daily_sales gds, go_products gp
                        WHERE YEAR(gds.`Date`)= COALESCE(%s , YEAR(gds.`Date`))
                        AND gds.Retailer_code = COALESCE (%s , gds.Retailer_code)
                        AND gp.Product_brand = COALESCE (%s, gp.Product_brand)
                        AND gp.Product_number = gds.Product_number """
            if retailer is None:
                cursor.execute(query, (anno, retailer, brand))
            else:
                cursor.execute(query, (anno, retailer.Retailer_code, brand))
            for row in cursor:
                res.append(Sales(**row))

            cursor.close()
            cnx.close()
            return res

    def handle_analizzaVendite(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        res = None
        if cnx is None:
            return res
        else:
            cursor = cnx.cursor()
            query = """SELECT  SUM(COALESCE(gds.Quantity, 0) * COALESCE(gds.Unit_sale_price, 0)),
                                COUNT(gds.Product_number),
                                COUNT(DISTINCT gds.Retailer_code),
                                COUNT(DISTINCT gds.Product_number)		
                    FROM go_daily_sales gds
                    JOIN go_products gp ON gp.Product_number = gds.Product_number
                    WHERE YEAR(gds.`Date`)= COALESCE(%s , YEAR(gds.`Date`))
                    AND gds.Retailer_code = COALESCE (%s , gds.Retailer_code)
                    AND gp.Product_brand = COALESCE (%s, gp.Product_brand)"""
            if retailer is None:
                cursor.execute(query, (anno, retailer, brand))
            else:
                cursor.execute(query, (anno, retailer.Retailer_code, brand))

            res = cursor.fetchone()

            cursor.close()
            cnx.close()
            return res

if __name__ == '__main__':
    res = DAO.handle_analizzaVendite(None, None, None)
    print(res[3])

