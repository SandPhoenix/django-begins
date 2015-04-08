from django.db import models
from django.utils import timezone
import math

class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=50)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)

	def __str__(self):
		return self.username

	def action_post(self,text):
		p = Post(post_user=self,post_date=timezone.now(),post_text=text)
		p.save()
		return p

	def kudos(self):
		posts = self.post_set.all()
		return int(math.fsum([p.post_kudos for p in posts]))


class Post(models.Model):
	post_date = models.DateTimeField()
	post_text = models.CharField(max_length=200)
	post_user = models.ForeignKey(User)
	post_kudos = models.IntegerField(default=0)

	def __str__(self):
		return self.post_text[:10] + '...'