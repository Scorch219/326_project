from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

# Create your models here.

class ProfileStruct(models.Model):
	first_name = models.CharField(max_length=20, help_text="First name", blank=True, null=True)
	last_name = models.CharField(max_length=20, help_text="Last name", blank=True, null=True)
	rating = models.IntegerField(default=0, blank=True, null=True)
	userID = models.UUIDField(default=uuid.uuid4, unique=True)
	def __str__(self):
		return self.first_name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=20, help_text="First name", blank=True, null=True)
	last_name = models.CharField(max_length=20, help_text="Last name", blank=True, null=True)
	rating = models.IntegerField(default=0, blank=True, null=True)
	userID = models.UUIDField(default=uuid.uuid4, unique=True)
	#profile_picture = models.ImageField(upload_to="where are we putting these", height_field=100, width_field=100, max_length=100)

	def __str__(self):
		return "%s - %s" % (self.first_name, self.last_name )

	def get_absolute_url(self):
		return reverse("user-detail", args=[str(self.id)] )



#class UserProfile(models.Model):
#	email = models.EmailField(max_length=254, help_text="Enter email address")
#	name = models.CharField(max_length=20, help_text="Full name")
#	rating = models.IntegerField()
#	profile_picture = models.ImageField(upload_to="where are we putting these", height_field=100, width_field=100, max_length=100)

class Product(models.Model):
	productID = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
	seller = models.ForeignKey("ProfileStruct", on_delete=models.SET_NULL, null=True)
	name=models.CharField(max_length=100, help_text="Product")
	description = models.TextField()
	price = models.DecimalField(max_digits=4, decimal_places=2)
	#picture = models.ImageField(upload_to="where are we putting these", height_field=100, width_field=100, max_length=100)
	seller_rating = models.IntegerField()
	category = models.CharField(max_length=100, help_text="Category", default="Some Category")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("product-detail", args=[str(self.id)])
		
		
class Category(models.Model):
	name = models.CharField(max_length=100, unique=True, help_text="Category")
	
	def __str__(self):
		return self.name

#class MeetUpLocation(models.Model):
#	location = models.CharField(max_length=100, help_text="Location meetup")
#class Category(models.Model):
#	name = models.CharField(max_length=100, help_text="Product category")
