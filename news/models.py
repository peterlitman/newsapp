import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Story(models.Model):
	headline = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	story_text = models.CharField(max_length=4000)
	
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def __str__(self):
		return self.headline + "\n" + str(self.pub_date) + "\n" + self.story_text
		
	
	