import csv

def load_cookies(filename='cookies.csv'):
    cookies = []
    file = None

    try:
        file = open(filename, 'r')
        reader = csv.DictReader(file)
        for row in reader:
            cookie = {
                'id': int(row['id']),
                'title': row['title'],
                'description': row['description'],
                'price': float(row['price']),
                'sugar_free': row['sugar_free'].lower() == 'true',
                'gluten_free': row['gluten_free'].lower() == 'true',
                'contains_nuts': row['contains_nuts'].lower() == 'true'
            }
            cookies.append(cookie)
    except Exception as e:
        print(f"Error reading the file: {e}")
    finally:
        if file:
            file.close()

    return cookies


def welcome_message():
    print("Welcome to the Python Cookie Shop!")
    print("We feed each according to their need.\n")
    print("We'd hate to trigger an allergic reaction in your body. So please answer the following questions:")

    valid_responses = ['yes', 'y', 'no', 'n']

    nuts_allergy = input("Are you allergic to nuts? (yes/no): ").strip().lower()
    if nuts_allergy not in valid_responses:
        print("Invalid response. Defaulting to 'no'.")
        nuts_allergy = 'no'

    gluten_allergy = input("Are you allergic to gluten? (yes/no): ").strip().lower()
    if gluten_allergy not in valid_responses:
        print("Invalid response. Defaulting to 'no'.")
        gluten_allergy = 'no'

    diabetes = input("Do you suffer from diabetes? (yes/no): ").strip().lower()
    if diabetes not in valid_responses:
        print("Invalid response. Defaulting to 'no'.")
        diabetes = 'no'

    return nuts_allergy
    return gluten_allergy
    return diabetes


def filter_cookies(cookies, nuts_allergy, gluten_allergy, diabetes):
    filtered_cookies = []
    for cookie in cookies:
        if nuts_allergy and cookie['contains_nuts']:
            continue
        if gluten_allergy and not cookie['gluten_free']:
            continue
        if diabetes and not cookie['sugar_free']:
            continue
        filtered_cookies.append(cookie)
    return filtered_cookies

def display_cookies(cookies):
    print("\nHere are the cookies we have in the shop for you:\n")
    for cookie in cookies:
        print(f"#{cookie['id']} - {cookie['title']}")
        print(cookie['description'])
        print(f"Price: ${cookie['price']:.2f}\n")

def take_order(cookies):
    order = []
    while True:
        cookie_id = input("Please enter the number of any cookie you would like to purchase (type 'finished' if finished with your order): ").strip().lower()
        if cookie_id in ['finished', 'done', 'quit', 'exit']:
            break
        try:
            cookie_id = int(cookie_id)
            selected_cookie = next((cookie for cookie in cookies if cookie['id'] == cookie_id), None)
            if not selected_cookie:
                print("Invalid cookie ID. Please try again.")
                continue
            quantity = int(input(f"My favorite! How many {selected_cookie['title']} would you like? ").strip())
            order.append((selected_cookie, quantity))
            print(f"Your subtotal for {quantity} {selected_cookie['title']} is ${selected_cookie['price'] * quantity:.2f}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    return order

def display_order_summary(order):
    if not order:
        print("\nNo items ordered.")
        return
    
    print("\nThank you for your order. You have ordered:\n")
    total_price = 0
    for cookie, quantity in order:
        print(f"-{quantity} {cookie['title']}")
        total_price += cookie['price'] * quantity
    print(f"\nYour total is ${total_price:.2f}.")
    print("Please pay with Bitcoin before picking-up.")
    print("\nThank you!\n-The Python Cookie Shop Robot.")