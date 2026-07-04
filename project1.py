#w,a,r,x
import json

with open('products.json', 'r') as file:
    products = json.load(file) #-> jab json file mai se main file mai data lana hota hai.


#Create a new product or a new dictionary

def create_product():
    new_product = {
        'id': 4,
        'name': 'Bhangda',
        'price': 100
    }
    products.append(new_product)

create_product()   # <-- Call the function

with open('products.json', 'w') as file:
    json.dump(products, file, indent = 4)  # dump -> jab main file mai se json file mai data dalna hota hai.


#Reading dictionary for specific id.

def product_id():
    userId = int(input('Enter your id to find: '))
    for i in products:
        if i['id'] == userId: #1==1
            print(i)
            break

product_id()

#Update product for a specific id.

def update_product():
    userID = int(input("Enter your ID: "))

    new_product = {
        'id': userID,
        'name': 'Mbappe',
        'price': 100
    }

    for i in products:
        if i['id'] == userID:
            i.update(new_product)
            break

    with open('products.json', 'w') as file:
        json.dump(products, file, indent=4)

update_product()



#Deleting a specific product

def delete_product():
    userID = int(input("Enter your ID:"))
    for i in products:
        if i['id'] == userID:
            products.remove(i)


    with open('products.json' , 'w') as file:
        json.dump(products, file)
        print('File deleted successfully....')

delete_product()



while True:
    print('Press 1 for creating new product')
    print('Press 2 for reading a product')
    print('Press 3 for updating a product')
    print('Press 4 for deleting a product')
    print('Press 0 for Exiting.....')

    choice = int(input("Enter your choice:"))

    if choice == 1:
        create_product()

    elif choice == 2:
        product_id()

    elif choice == 3:
        update_product()

    elif choice == 4:
        delete_product()

    elif choice == 0:
        print('Exiting.....')
        break







# # a = {'Ronald':25, 'Messi':30, 'Neymar':35} #purani dic
# # print(a)
# # b = {'Ronald':30, 'Messi':35, 'Neymar':40} #nayi dic
# # a.update(b) 
# # print(a)