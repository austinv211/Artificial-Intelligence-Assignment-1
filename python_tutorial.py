# writing scripts in python
FRUITS = ['apples', 'oranges', 'pears', 'bananas']
FRUIT_PRICES = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}

def print_fruits(fruit_list):
    for fruit in fruit_list:
        print(f'{fruit} for sale')

def get_cheap_fruits(fruit_dict):
    for fruit, price in fruit_dict.items():
        if price < 2.00:
            print(f'{fruit} cost ${price} per pound.')
        else:
            print(f'{fruit} are too expensive!')