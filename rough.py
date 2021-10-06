import mimetypes
import requests
import urllib

# headers = {'Content-type': 'content_type_value'}
url = 'https://api.twilio.com/2010-04-01/Accounts/AC6e84689f46a1ce7f6498d55302f67319/Messages/MM4b5146de8db8a97c2376ab291e3f2a8e/Media/ME221d05fed36f4bc420c6c115d6f1a421'
req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
r = urllib.request.urlopen(req)
h = r.getheader('Content-Type')
# print(h)
type = h.split('/')
content_type = type[1]

# print(mimetypes.MimeTypes().guess_extension(''))