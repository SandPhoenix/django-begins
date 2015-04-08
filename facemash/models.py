from django.db import models

class User(models.Model):

	gender_chioces = (('m','Male'),('f','Female'))

	user_rating = models.FloatField(default=1500)
	user_name = models.CharField(max_length=100)
	user_id = models.BigIntegerField(default=0)
	user_gender = models.CharField(choices=gender_chioces,max_length=1)
	user_picture = models.CharField(max_length=200,default='https://pbs.twimg.com/profile_images/3700906677/620e0c1391e55d928f4a7d34efd19e89.png')

	def user_id_string(self):
		return str(self.user_id)