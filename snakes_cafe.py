welcomeMsg = """*************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
----------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts 
----------
Ice Cream
Cake
Pie
Drinks
----------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
"""
food = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado", "A Literal Garden", "Ice Cream", "Cake","Pie","Coffee","Tea","Unicorn Tears"]
print(welcomeMsg)


def orders():
    count = 0
    order = ""
    while order != 'quit':
        print("What would you like to order?")
        order = input(">")
        if order == 'quit':
            break
        count = count + 1
        print(f'** {count} order of {order} have been added to your meal**')


orders()

