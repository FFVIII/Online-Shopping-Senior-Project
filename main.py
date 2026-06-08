from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql
import pymysql.cursors
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

#######################MySQL###################################
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-key')

def get_db_connection():
	"""Create and return a database connection"""
	return pymysql.connect(
		host=os.getenv('MYSQL_HOST', 'localhost'),
		user=os.getenv('MYSQL_USER', 'root'),
		password=os.getenv('MYSQL_PASSWORD'),
		database=os.getenv('MYSQL_DB', 'online'),
		cursorclass=pymysql.cursors.DictCursor
	)
#######################products################################
@app.route('/')
def products():
	cursor = None
	conn = None
	try:
		conn = get_db_connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM product")
		rows = cursor.fetchall()
		return render_template('products.html', products=rows)
	except Exception as e:
		print(e)
		return 'Error loading products', 500
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()
 
#################################################################
@app.route('/alldetail/<id>')
def alldetail(id):
	cursor = None
	conn = None
	try:
		conn = get_db_connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM product where id="+id)
		rows = cursor.fetchall()
		return render_template('alldetail.html', products=rows)
	except Exception as e:
		print(e)
		return 'Error loading product details', 500
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()
#################################################################

@app.route('/desktop')
def desktop():
	cursor = None
	conn = None
	try:
		conn = get_db_connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM product where id <= 8")
		rows = cursor.fetchall()  		
		return render_template('desktop.html', products=rows)
	except Exception as e:
		print(e)
		return 'Error loading desktop products', 500
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()

@app.route('/laptop')
def Laptop():
	cursor = None
	conn = None
	try:
		conn = get_db_connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM product where id >= 9 and id <= 16")
		rows = cursor.fetchall()
		return render_template('laptop.html', products=rows)
	except Exception as e:
		print(e)
		return 'Error loading laptop products', 500
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()

@app.route('/cellphone')
def cellphone():
	cursor = None
	conn = None
	try:
		conn = get_db_connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM product where id >= 17 and id <= 24")
		rows = cursor.fetchall()
		return render_template('cellphone.html', products=rows)
	except Exception as e:
		print(e)
		return 'Error loading cellphone products', 500
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()
#########################info#########################
#pcdetail
@app.route('/pcdetail/<id>')
def pcdetail(id):
	cursor = None
	conn = None
	try:
		conn = get_db_connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM product where id =" + id)
		rows = cursor.fetchall()
		return render_template('pcdetail.html', products=rows)

	except Exception as e:
		print(e)
		return 'Error loading PC details', 500
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()
		
#laptopdetail
@app.route('/laptopdetail/<id>')
def laptopdetail(id):
	cursor = None
	conn = None
	try:
		conn = get_db_connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM product where id =" + id)
		rows = cursor.fetchall()
		return render_template('laptopdetail.html', products=rows)
	except Exception as e:
		print(e)
		return 'Error loading laptop details', 500
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()

 #cellphonedetail
@app.route('/cellphonedetail/<id>')
def cellphonedetail(id):
	cursor = None
	conn = None
	try:
		conn = get_db_connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM product where id =" + id)
		rows = cursor.fetchall()
		return render_template('cellphonedetail.html', products=rows)
	except Exception as e:
		print(e)
		return 'Error loading cellphone details', 500
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()

#######################shopping cart#########################
#shopping cart
@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/empty')
def empty_cart():
	try:
		session.clear()
		return redirect(url_for('.products'))
	except Exception as e:
		print(e)

@app.route('/delete/<string:code>')
def delete_product(code):
	try:
		all_total_price = 0
		all_total_quantity = 0
		session.modified = True
		
		for item in session['cart_item'].items():
			if item[0] == code:				
				session['cart_item'].pop(item[0], None)
				if 'cart_item' in session:
					for key, value in session['cart_item'].items():
						individual_quantity = int(session['cart_item'][key]['quantity'])
						individual_price = float(session['cart_item'][key]['total_price'])
						all_total_quantity = all_total_quantity + individual_quantity
						all_total_price = all_total_price + individual_price
				break
		
		if all_total_quantity == 0:
			session.clear()
		else:
			session['all_total_quantity'] = all_total_quantity
			session['all_total_price'] = all_total_price
		return redirect(url_for('.cart'))
	except Exception as e:
		print(e)
#######################Add###################################
@app.route('/add', methods=['POST'])
def add_product_to_cart():
	cursor = None
	conn = None
	try:
		_quantity = int(request.form['quantity'])
		_code = request.form['code']
	
		if _quantity and _code and request.method == 'POST':
			conn = get_db_connection()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute("SELECT * FROM product WHERE code=%s", _code)
			row = cursor.fetchone()
			
			itemArray = { row['code'] : {'name' : row['name'], 'code' : row['code'], 'quantity' : _quantity, 'price' : row['price'], 'image' : row['image'], 'total_price': _quantity * row['price']}}
			
			all_total_price = 0
			all_total_quantity = 0
			
			session.modified = True
			if 'cart_item' in session:
				if row['code'] in session['cart_item']:
					for key, value in session['cart_item'].items():
						if row['code'] == key:
							old_quantity = session['cart_item'][key]['quantity']
							total_quantity = old_quantity + _quantity
							session['cart_item'][key]['quantity'] = total_quantity
							session['cart_item'][key]['total_price'] = total_quantity * row['price']
				else:
					session['cart_item'] = array_merge(session['cart_item'], itemArray)

				for key, value in session['cart_item'].items():
					individual_quantity = int(session['cart_item'][key]['quantity'])
					individual_price = float(session['cart_item'][key]['total_price'])
					all_total_quantity = all_total_quantity + individual_quantity
					all_total_price = all_total_price + individual_price
			else:
				session['cart_item'] = itemArray
				all_total_quantity = all_total_quantity + _quantity
				all_total_price = all_total_price + _quantity * row['price']
			
			session['all_total_quantity'] = all_total_quantity
			session['all_total_price'] = all_total_price
			
			return redirect(request.referrer)

		else:			
			return 'Error while adding item to cart'
	except Exception as e:
		print(e)
		return 'Error adding item to cart', 500
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()

####################################calculate###################################	
def array_merge( first_array , second_array ):
	if isinstance( first_array , list ) and isinstance( second_array , list ):
		return first_array + second_array
	elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
		return dict( list( first_array.items() ) + list( second_array.items() ) )
	elif isinstance( first_array , set ) and isinstance( second_array , set ):
		return first_array.union( second_array )
	return False	

#######################Search#########################
@app.route('/result', methods=['POST'])
def result():
	cursor = None
	conn = None
	try:
		conn = get_db_connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		name = request.form.get('search_text')
		cursor.execute("SELECT * FROM `product` WHERE `name` Like '%"+name+"%'")
		data = cursor.fetchall()
		return render_template('result.html', results=data)
	except Exception as e:
		print(e)
		return 'Error searching products', 500
	finally:
		if cursor:
			cursor.close()
		if conn:
			conn.close()

#######################Login and Logout#########################
@app.route('/login',methods=["GET","POST"])
def login():
    if  request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = cursor.fetchone()
        cursor.close()

        if len(user) > 0:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']
                return redirect(url_for('products'))
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("login.html")

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect(url_for('products'))

@app.route('/register', methods=["GET", "POST"])
def register():
	if request.method == 'GET':
		return render_template("register.html")
	else:
		name = request.form['name']
		email = request.form['email']
		password = request.form['password'].encode('utf-8')
		hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

		conn = get_db_connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",(name,email,hash_password,))
		conn.commit()
		session['name'] = request.form['name']
		session['email'] = request.form['email']
	
		return redirect(url_for('products'))

@app.route('/')
def index():
    return render_template('products.html')

@app.route('/pay')
def pay():
    return render_template('pay.html')

if __name__ == '__main__':
    app.run(debug=True)
