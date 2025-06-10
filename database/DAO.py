from database.DB_connect import DBConnect
from model.method import Method
from model.product import Product


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getAllMethods():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    from go_methods gm """
        cursor.execute(query)

        for row in cursor:
            result.append(Method(**row))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllProducts(anno, metodo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary = True)
        query = """SELECT DISTINCT gp.*, SUM(gds.Quantity*gds.Unit_sale_price) as tot_vendite
                   from go_daily_sales gds , go_products gp 
                    WHERE gds.Product_number = gp.Product_number 
                    AND YEAR(gds.`Date`)=%s
                    AND gds.Order_method_code = %s
                    GROUP BY gp.Product_number """
        cursor.execute(query, (anno, metodo))

        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        conn.close()
        return result

