import uuid

class Product:
    """
    Class defines all questions received.
    """
    def __init__(self,category,name,price):
        self.category = category
        self.name = name
        self.price = price



class ProductsList:
    """
    Class holds all questions received.
    """
    def __init__(self):
        self.product_list = []

    def get_products(self):
        return self.product_list

my_products = ProductsList()
"""
    def to_dict(self,question,id,account,answer):
        new_question = {"Question":question,"Qn_id":id,"Account":account,'Answer':answer}
        return new_question

    def id_generator(self,list):
        if len(list)==0:
            return 1
        last_item = list[-1]
        try:
            return last_item['Qn_id']+1
        except:
            return last_item['Ans_id']+1
"""
