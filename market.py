from typing import List, Dict
from time import sleep

from models.product import Product
from utils.helper import format_float_str_coin


products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('========================================================')
    print('==================   WELCOME   =========================')
    print('================   Supermarket  ========================')

    print('Select an option: ')
    print('1 - Register product')
    print('2 - List product')
    print('3 - Buy product')
    print('4 - View cart')
    print('5 - Close order')
    print('6 - Exit system')

    option: int = int(input())

    if option == 1:
        register_product()

    elif option == 2:
        list_product()

    elif option == 3:
        buy_product()

    elif option == 4:
        view_cart()

    elif option == 5:
        close_order()

    elif option == 6:
        print('Check back often!')
        sleep(2)
        exit(0)

    else:
        print('Invalid option!')
        menu()


def register_product() -> None:
    print('Product registration')
    print('====================')

    name: str = input('Enter the product name: ')
    price: float = float(input('Enter the price of the product: '))

    product: Product = Product(name, price)

    products.append(product)

    print(f'The product {product.name} has been successfully registered!')
    sleep(2)
    menu()


def list_product() -> None:
    if len(products) > 0:
        print('Product listing')
        print('---------------')
        for product in products:
            print(product)
            print('------------')
            sleep(1)
    else:
        print(' There are no registered products yet.')
    sleep(2)
    menu()


def buy_product() -> None:
    if len(products) > 0:
        print('Enter the product code you want to add to the cart: ')
        print('----------------------------------------------------')
        print('============== Products available ==================')
        for product in products:
            print(product)
            print('------------------------------------------------')
            sleep(1)
        code: int = int(input())

        product: Product = get_product_by_code(code)

        if product:
            if len(cart) > 0:
                in_the_cart: bool = False
                for item in cart:
                    amount: int = item.get(product)
                    if amount:
                        item[product] = amount + 1
                        print(f'The product {product.name} now has {amount + 1} units in the cart. ')
                        in_the_cart = True
                        sleep(2)
                        menu()
                if not in_the_cart:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'The product {product.name} has been added to the cart. ')
                    sleep(2)
                    menu()

            else:
                item = {product: 1}
                cart.append(item)
                print(f'The product {product.name} has been added to the cart.')
                sleep(2)
                menu()
        else:
            print(f'The product with the code {code} was not found.')
            sleep(2)
            menu()

    else:
        print('There are no products to sell yet.')
    sleep(2)
    menu()


def view_cart() -> None:
    if len(cart) > 0:
        print('Products in the cart: ')

        for item in cart:
            for dados in item.items():
                print(dados[0])
                print(f'Amount: {dados[1]}')
                print('-------------------')
                sleep(1)
    else:
        print('THere are no products in the cart yet.')
    sleep(2)
    menu()


def close_order() -> None:
    if len(cart) > 0:
        value_total: float = 0

        print('Cart products')
        for item in cart:
            for dados in item.items():
                print(dados[0])
                print(f'Amount: {dados[1]}')
                value_total += dados[0].price * dados[1]
                print('-------------------------------')
                sleep(1)
        print(f'Your invoice is {format_float_str_coin(value_total)}')
        print('Check back often!')
        cart.clear()
        sleep(5)
    else:
        print('There are no products in the cart yet.')
    sleep(2)
    menu()


def get_product_by_code(code: int) -> Product:
    p: Product = None

    for product in products:
        if product.code == code:
            p = product
    return p


if __name__ == '__main__':
    main()
