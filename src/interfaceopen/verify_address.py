
import urllib, httplib

httpClient = None

try:
    params = urllib.urlencode({'city': 'true', 'area': 'true', 'flag': 'false', 'address_line_1': 'false', 'customer_lat': 'false', 'customer_lng': 'false'})
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    httpClient = httplib.HTTPConnection('localhost', 80, timeout=10)
    httpClient.request('POST', '/python.php', params, headers)
    
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders()

except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
