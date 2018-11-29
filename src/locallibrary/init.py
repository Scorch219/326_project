from django.contrib.auth.models import User
from umarket.models import Profile, ProfileStruct, Product, ProductCategory
from faker import Faker
from datetime import timedelta
import textwrap
import random

fake = Faker()

# Create Users
users = []
for i in range(1,10):
	u_email = fake.ascii_email()
	u_first_name = fake.first_name()
	u_last_name = fake.last_name()
	u_rating = fake.random_int(0, 5)
	# u_profile_picture = fake.file_name(category=None, extension=".png")
	u_userID = fake.uuid4()
	# user = User(email=u_email, password=u_password, name=u_name, rating=u_rating, profile_picture=u_profile_picture, userID=u_userID)
	profile = ProfileStruct(first_name=u_first_name, last_name=u_last_name, rating=u_rating, userID=u_userID)
	profile.save()
	users.append(profile)


# Create Categories
categories = [
	ProductCategory(name='Animal Care'),
	ProductCategory(name='Arts and Crafts'),
	ProductCategory(name='Automotive and Tansportation'),
	ProductCategory(name='Beauty and personal products'),
	ProductCategory(name='Books'),
	ProductCategory(name='Class Materials'),
	ProductCategory(name='Clothing'),
	ProductCategory(name='Electronics'),
	ProductCategory(name='Entertainment'),
	ProductCategory(name='Hardware'),
	ProductCategory(name='Houseware'),
	ProductCategory(name='Healthcare'),
	ProductCategory(name='Kitchenware'),
	ProductCategory(name='Music'),
	ProductCategory(name='Miscellaneous'),
	ProductCategory(name='Office supplies'),
	ProductCategory(name='Sports'),
	ProductCategory(name='Umass')
]

# Save the categories to the database
for category in categories:
    category.save()

# Create Products
products = []
for i in range(1, 10):
	p_productID = fake.pystr(min_chars=5, max_chars=20)
	# p_userID = fake.uuid4()
	p_seller = users[fake.random_int(0, len(users)) - 1]
	p_name = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
	p_description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
	p_price = fake.pydecimal(left_digits=2, right_digits=2, positive=True)
	# p_picture = fake.file_name(category=None, extension=".png")
	p_seller_rating = fake.random_int(0, 5)
	p_category = categories[fake.random_int(0, len(categories)) - 1]
	product = Product(productID=p_productID, seller=p_seller, name=p_name, description=p_description, price=p_price, seller_rating=p_seller_rating, category=p_category)
	product.save()
	products.append(product)


username = "admin326"
password = "admin326"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
=
The database has been setup with the following credentials:

  username: {username}
  password: {password}
  email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080"
=
"""
print(message)


# auth_users = []
# print("Generated users:")
# for u in users:
#     username = u.first_name.lower()[0] + u.last_name.lower()
#     email = f"{username}@326.edu"
#     password = u.last_name
#     user = User.objects.create_user(username, email, password)
#     user.first_name = u.first_name
#     user.last_name = u.last_name
# 	user.save()
# 	auth_users.append(user)
# 	print(f" username: {username}, password: {password}")

auth_users = []
print("Generating Users:")
for u in users:
	username = u.first_name.lower()[0] + u.last_name.lower()
	email = f"{username}@326.edu"
	password = u.last_name
	user = User.objects.create_user(username, email, password)
	profile = Profile(user=user, first_name=u.first_name, last_name=u.last_name, rating=u.rating, userID=u.userID)
	profile.save()
	auth_users.append(profile)
	print(f" username: {username}, password: {password} ")
