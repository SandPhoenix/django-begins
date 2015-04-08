from django.db import models

class Story(models.Model):

	TYPE_CHOICES = 	(
		('story','Story'),
		('comment','Comment'),
		('poll','Poll'),
		('pollopt','Poll Option')

	)

	story_by = models.CharField(max_length=20)
	story_id = models.IntegerField(default=0)
	story_score = models.IntegerField(default=0)
	story_time = models.IntegerField(default=0)
	story_title = models.CharField(max_length=100)
	story_type = models.
	story_url = models.CharField(max_length=100)

