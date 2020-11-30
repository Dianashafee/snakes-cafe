

menu = ['Wings','Cookies','Spring Rolls','Salmon','Steak','Meat Tornado','A Literal Garden','Ice Cream','Cake','Pie','Coffee','Tea','Unicorn Tears']
order =[] 

welcomeContent = """
**************************************
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
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
"""
print(welcomeContent)


i = True
while i:

    if len(menu):
        ordermsg = """
                      ***************      

              """
        print(ordermsg)
    
    urChoice = str(input()).capitalize()

    if urChoice in menu:
        order.append(urChoice)
        orderCount = order.count(urChoice)
            
        print(f"** {orderCount} order of {urChoice} have been added to your meal **")
        print('If you have anothr order type it or type quit to exit ???')



    elif urChoice == 'Quit':
        break


    else:
        print('Your Order in Not in our menu ,try another thing  ')    

    #  if __name__ == '__main__':
    #  print('Thanks for Visiting us ^.^')   