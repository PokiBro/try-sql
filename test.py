import sqlite3
con = sqlite3.connect('C:\\Users\\Admin\\Desktop\\CTF\\database.db')
curcor = con.cursor()
def new_goods(curcor,id,name,description,price):
    curcor.execute("INSERT INTO goods(id,name,description,price) VALUES({},{},{},{})".format(id,name,description,price))
    curcor.execute("SELECT id,name,description,price FROM goods ")
    return(curcor.fetchall())

def new_user(curcor,id,name,surname,email):
    curcor.execute("INSERT INTO users(id,name,surname,email) VALUES({},{},{},{})".format(id,name,surname,email))
    curcor.execute("SELECT id,name,surname,email FROM users ")
    return(curcor.fetchall())

def new_order(curcor,order_id,good_id,good_count,user_id):
    
    curcor.execute("INSERT INTO goods_in_order(order_id,good_id,good_count,user_id) VALUES({},{},{},{})".format(order_id,good_id,good_count,user_id))
    curcor.execute("SELECT order_id,good_id,good_count,user_id FROM goods_in_order ")
    return(curcor.fetchall())
def take_order_from_USER_ID(curcor,user_id):
    curcor.execute("SELECT order_id,good_id,good_count,user_id FROM goods_in_order WHERE user_id == {}".format(user_id))
    return(curcor.fetchall())

def take_order_from_email(curcor,email):
    curcor.execute("SELECT order_id,good_id,good_count,user_id FROM goods_in_order WHERE user_id IN (SELECT id FROM users WHERE email = {})".format(email))
    return(curcor.fetchall())

print("что вы хотите сделать? добавить товар - 0, добавить пользователя - 1, добавтиь заказ - 2,3 - посмотреть заказы пользователя")
a = int(input())
test = curcor.execute('SELECT order_id,good_id,good_count,user_id FROM goods_in_order')
print(test.fetchall())
test2 = curcor.execute("SELECT id,name,surname,email FROM users ")
print(test2.fetchall())
if a == 0:
    print("введите id товара,имя товара, описание товара,цену товара. ИМЕННО В ЭТОЙ ПОСЛЕДОВАТЕЛЬНОСТИ")
    print(new_goods(curcor,int(input()),"'" +input() + "'","'" + input() + "'", int(input())))
if a == 1:
    print("введите id пользователя,имя пользователя, фамилию и емэил. ИМЕННО В ЭТОЙ ПОСЛЕДОВАТЕЛЬНОСТИ")
    print(new_user(curcor,int(input()),"'" +input() +"'","'" + input() + "'", "'"+ input() + "'"))
if a == 2:
    print("введите id заказа, id товара, количество товара, id пользователя. ИМЕННО В ЭТОЙ ПОСЛЕДОВАТЕЛЬНОСТИ")
    print(new_order(curcor,int(input()),int(input()),int(input()), int(input())))

if a == 3:
    print("введите 1 - если знаете id пользователя, введите 2 если знаете почту пользователя")
    a = int(input())
    if a == 1:
        print('введите id пользователя')
        print(take_order_from_USER_ID(curcor, int(input())))
    if a == 2:
        print("введите email пользователя")
        print(take_order_from_email(curcor, "'" + input() + "'"))


    

con.commit()
