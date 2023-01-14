import random
products_names=["Computadora","Mouse","Cargador","Pilas","Escritorio","Monitor"]
prices_products=[12000.00,235.00,768.00,345.00,8000.00,3450.00]

def create_payment():
    random_number_product = random.randint(0,5)
    product_name = str(products_names[random_number_product])
    price_product = float(prices_products[random_number_product])
    quantity = random.randint(1,30)
    amount = float(quantity)*price_product
    return product_name,quantity,amount
