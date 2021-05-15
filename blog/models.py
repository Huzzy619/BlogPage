from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.

# This helps to create the info in a database. with the class name acting as a Table Name 
class Post (models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete= models.CASCADE)



	def __str__(self):
		return self.title


	def get_absolute_url (self):
		return reverse('post-detail', kwargs= {'pk': self.pk} )
		