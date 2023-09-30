#--------- Data -----
#creating a list of dictionaries (products)
productsList = [
    {'product_id':1,
    'product_name': 'Cereal',
    'price': 20,
    'discount_percentage':20},
    {'product_id':2,
    'product_name': 'Pizza',
    'price': 40,
    'discount_percentage':2},
    {'product_id':3,
    'product_name': 'Milk',
    'price': 5,
    'discount_percentage':0},
    {'product_id':4,
    'product_name': 'Apple',
    'price': 5,
    'discount_percentage':5},
    {'product_id':5,
    'product_name': 'Ice cream',
    'price': 10,
    'discount_percentage':50},
    {'product_id':6,
    'product_name': 'Tacos',
    'price': 10,
    'discount_percentage':10},
    ]

#initialize useful lists
cartList=[
    {'product_id':0,
     'quantity':0}
]

soldList=[
    {'product_id':1,
     'quantity':10
    },
    {'product_id':5,
     'quantity':29
    }
]

# ----- Functions -----

def productSearchByName(name):
    for i in productsList:
        if i['product_name'] == str(name):
            print(f'Product: {name}  Price: {i["price"]}')
            return
    print('Sorry, Product not found')

def getProductPrice(product_id):
    for i in productsList:
        if(i['product_id']==int(product_id)):
            return i['price'] #found
    return 0 #not found

def getProductDiscount(product_id):
    for i in productsList:
        if(i['product_id']==int(product_id)):
            return i['discount_percentage']/100 # return float value 
    return 0 #not found


def getCartTotal():
    #counter
    total = 0
    for product in cartList:
        total += getProductPrice(product['product_id']) * int(product['quantity'])
    return total

def getDiscountCalculation():
    #counter
    totalAfterDiscount = 0
    for product in cartList:
        totalAfterDiscount += getProductPrice(product['product_id']) * int(product['quantity']) * (1.00 - getProductDiscount(product['product_id']))
    return totalAfterDiscount

def getTopSellingProducts(top_n):
    topList = sorted(soldList,key=lambda x: x['quantity'], reverse=True)
    return topList[:top_n]


def addItemToCart(product_id, quantity):
    cartList.append({'product_id': int(product_id), 'quantity': int(quantity)}) #adding to Cart
    soldList.append({'product_id': int(product_id), 'quantity': int(quantity)}) #adding to Sold List




