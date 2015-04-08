#https://www.facebook.com/{0}/about?section=contact-info
# import requests
# from lxml import html

# login_page = requests.get('https://www.facebook.com/')
# data = html.document_fromstring(login_page.text)
# inputs = data.xpath('/html/body/div/div[1]/div/div/div/div/div/div[2]/form//input')
# payload = { i.name : i.value for i in inputs if i.name != None}
# payload['email'] = 'matteo.sandrin@hotmail.it'
# payload['pass'] = 'gattomatto'
# s = requests.Session()
# s.post('https://www.facebook.com/login.php?login_attempt=1',headers=payload)
# p = s.post('https://www.facebook.com/beatrice.bella.5')
# print p.text

import mechanize
import cookielib
import json
from lxml import html
import requests

f = open('g.txt','a')
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
# br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.open('https://facebook.com')
br.form = list(br.forms())[0] 
br['email'] = 'toastedpin@gmail.com'
br['pass'] = 'abduljabbar'
br.submit()

ulist = json.loads(open('members.txt').read())['data']

for u in ulist[100:]:
	a = ''
	i = u['id']
	url = 'https://www.facebook.com/{0}'.format(i)
	print url
	r = br.open(url)
	break



# r = br.open('https://www.facebook.com/beatrice.bella.5')
# print r.read()