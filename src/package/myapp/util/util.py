# This creates an HTTP message
# with the content of BODY as the enclosed representation
# for the resource http://localhost:8080/file
import http.client

BODY = ""
conn = http.client.HTTPConnection("ec2-18-188-30-68.us-east-2.compute.amazonaws.com", 8080)
conn.request("GET", "/")
response = conn.getresponse()
print(response.status, response.reason)
print(response.read())


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