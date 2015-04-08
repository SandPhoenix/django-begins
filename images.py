import django
django.setup()
from facemash.models import User
import urllib2

users = list(User.objects.all())

for u in users:
	print users.index(u)
	img = urllib2.urlopen(u.user_picture)
	f = open('facemash/static/facemash/images/{0}.jpg'.format(u.user_id),'w')
	f.write(img.read())
	f.close()