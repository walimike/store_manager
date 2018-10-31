from .. models.products import my_products

class Validator:
    """
    Makes sure that only valid data is passed.
    """
    def empty_list(self):
        list = my_products.product_list
        if len(list) == 0:
            return
        return list

is_valid = Validator()
