from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import random
from django.db import IntegrityError, transaction


class Report(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField()
	subject = models.CharField(max_length=200)
	location = models.CharField(max_length = 200)
	message = models.CharField(max_length=5000)
	file = models.ImageField()
	slug = models.SlugField(max_length=50, allow_unicode=True, unique=True, blank='True')
	date_pub = models.DateTimeField(auto_now=True)
	confrimed = models.PositiveIntegerField(default=0)
	pub = models.BooleanField(default=False)
	
	def __str__(self):
		return self.name


	def save(self, *args, **kwargs):
		try:
			with transaction.atomic():
				self.slug = slugify(self.subject)
				super().save(*args, **kwargs)
		except IntegrityError:
			self.slug = slugify(self.subject) + str(random.randint(1,200))
			super().save(*args, **kwargs)
		



	def publish(self):
		self.pub = True
		self.save()


	def get_absolute_url(self):
		return reverse('details', kwargs={'slug':self.slug})