# This creates an HTTP message
# with the content of BODY as the enclosed representation
# for the resource http://localhost:8080/file
import http.client

# for https conn = http.client.HTTPSConnection("www.python.org") and normally... module urllib.request
# # HTTP Error
#
# import urllib.request
# import urllib.parse
#
# # trying to read the URL
# try:
#     x = urllib.request.urlopen('https://www.google.com / search?q = test')
#     print(x.read())
#
# # Catching the exception generated
# except Exception as e :
#     print(str(e))
# # importing robot parser class
# import urllib.robotparser as rb
#
# bot = rb.RobotFileParser()
#
# # checks where the website's robot.txt file reside
# x = bot.set_url('https://www.geeksforgeeks.org / robot.txt')
# print(x)
#
# # reads the files
# y = bot.read()
# print(y)
#
# # we can crawl the main site
# z = bot.can_fetch('*', 'https://www.geeksforgeeks.org/')
# print(z)
#
# # but can not crawl the disallowed url
# w = bot.can_fetch('*', 'https://www.geeksforgeeks.org / wp-admin/')
# print(w)




# case1
BODY = ""
conn = http.client.HTTPConnection("ec2-18-188-30-68.us-east-2.compute.amazonaws.com", 8080)
conn.request("GET", "/")
response = conn.getresponse()
print(response.status, response.reason)
print(response.read())

# case2
# import http.client, urllib.parse
# params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
# headers = {"Content-type": "application/x-www-form-urlencoded",
#                ...            "Accept": "text/plain"}
# conn = http.client.HTTPConnection("bugs.python.org")
# conn.request("POST", "", params, headers)
# response = conn.getresponse()
# print(response.status, response.reason)
# data = response.read()
# data
# b'Redirecting to <a href="http://bugs.python.org/issue12524">http://bugs.python.org/issue12524</a>'
# conn.close()