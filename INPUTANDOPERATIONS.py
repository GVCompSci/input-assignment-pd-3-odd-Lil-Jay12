
fullname = input('Please input your name:')
print()
phonenumber = input('Please input your phone number:')
print()
product = input('Please enter the name of the  product you would like to purchase:')
print()
price = float(input('Price of the item:'))
print()
quantity = int(input('Please enter the quantity for purchase:'))
subtotal = (price*quantity)
tax = (6/100 *  price)
total = (subtotal + tax)
print()
print(fullname)
print()
print(phonenumber)
print()
print('Purchase Information:')
print(product, '      ', 'Qty:', quantity, '      ', 'Price: $', price)
print()
print ('Subtotal: $',subtotal, '    Tax: $', tax, '    Total:$', total)