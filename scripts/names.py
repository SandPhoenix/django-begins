import django
django.setup()
from facemash.models import User
import requests
import json

ulist = json.loads(open('members.txt').read())['data']

def makeUser(u):
	print ulist.index(u)
	a = User()
	a.user_name = u['name']
	a.user_id = u['id']
	a.save()

def getGender(u):
	name = u['name'].split(' ')[0].encode('utf-8')
	payload = {'name':name,'country_id':'it'}
	result = requests.get('https://api.genderize.io',data=payload)
	if len(result.text) > 0:
		result = json.loads(result.text)
		print result
		if result['gender']:
			return result['gender']
		else:
			return ''
	else:
		return ''

glist = []

for u in ulist:
	makeUser(u)
	# g = getGender(u)
	# u['gender'] = g
	# glist.append(u)

# f = open('g.txt','w')
# f.write(json.dumps(glist))
# f.close()
