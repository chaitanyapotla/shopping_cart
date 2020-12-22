import argparse
import sys


def display_bill(items):
    sub_total = 0
    t_shirts = 0
    jackets = 0
    shoes = 0
    shoes_discount = 0
    jackets_discount = 0

    for item in items:
        if item == "T-shirt":
            sub_total += 500
            t_shirts += 1
        elif item == "Trousers":
            sub_total += 1500
        elif item == "Jacket":
            sub_total += 2500
            jackets += 1
        elif item == "Shoes":
            sub_total += 5000
            shoes += 1

    total_tax = int(0.18 * sub_total)

    if shoes > 0:
        shoes_discount = int(shoes * 0.1 * 5000)

    if jackets > 0:
        if 2 * jackets <= t_shirts:
            jackets_discount = int(jackets * 0.5 * 2500)

    final_total = sub_total + total_tax

    if shoes_discount > 0:
        final_total -= shoes_discount

    if jackets_discount > 0:
        final_total -= jackets_discount

    print("========================  Cart Summary  ============================")
    print("Subtotal: Rs. {}".format(sub_total))
    print("Tax: Rs. {}".format(total_tax))
    if shoes_discount > 0 or jackets_discount > 0:
        print("Discounts:")
        if shoes_discount > 0:
            print("10% off on shoes: -Rs. {}".format(shoes_discount))
        if jackets_discount > 0:
            print("50% off on jacket: -Rs. {}".format(jackets_discount))
    print("Total: Rs. {}".format(final_total))
    print("====================================================================")


def add_to_cart():
    parser = argparse.ArgumentParser(
        description="Please list the items one after the other to add to the cart"
    )
    parser.add_argument("items", nargs='*',
                        help='Item could be T-shirt, Trousers, Jacket or Shoes')
    items = parser.parse_args().items
    display_bill(items)


def main():
    try:
        add_to_cart()
    except Exception as e:
        print("Error: {}".format(e.message))
        sys.exit(1)


if __name__ == '__main__':
    main()
