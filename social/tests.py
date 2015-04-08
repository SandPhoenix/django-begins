from django.test import TestCase
from social.models import User,Post

class UserActionsTests(TestCase):

	def test_total_kudos_count(self):
		u = User(username='test',password='test',last_name='test',first_name='test')
		u.save()
		k1 = 123
		k2 = 567
		p1 = u.action_post('Hello, this is a test')
		p1.post_kudos = k1
		p1.save()
		p2 = u.action_post('Hello, this is another test')
		p2.post_kudos = k2
		p2.save()
		self.assertEqual(u.kudos(),k1+k2)

