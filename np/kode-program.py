import urllib.error
import gzip
import datetime
import requests
from urllib.request import urlopen, Request, build_opener, HTTPCookieProcessor
from http.cookiejar import CookieJar
from urllib.parse import urlparse, urljoin , parse_qs, quote, urlencode, urlunparse

def daftar_isi():
    print ("[1. Request with urllib]")
    print ("[2. Response objects]")
    print ("[3. Status code]")
    print ("[4. Handling Problems]")
    print ("[5. Http headers]")
    print ("[6. Customizing request]")
    print ("[7. Content Compression]")
    print ("[8. Multiple Values]")
    print ("[9. Content types]")
    print ("[10. User Agents]")
    print ("[11. Cookies]") 
    print ("[12. Redirects]")
    print ("[13. URLs]")
    print ("[14. Paths and relative URLs]")
    print ("[15. Query strings]")
    print ("[16. URL Encoding]")
    print ("[17. HTTP method]") 
    print ("[18. Request Library]")
    print ("[19. Handling Errors with request]")
#-------------------------------------------------------------------
def Cookies():
    print("-----COOKIES-----")
    print ("[a. Cookies Handling]")
    print ("[b. Know your Cookies]")
    x = input("masukkan pilihan = ")
    if x == 'a':
        cookie_jar = CookieJar() 
        opener = build_opener(HTTPCookieProcessor(cookie_jar))
        opener.open('http://www.github.com')
        print(len(cookie_jar))
#-------------------------------------------------------------------
    elif x == 'b':
        cookie_jar = CookieJar()
        opener = build_opener(HTTPCookieProcessor(cookie_jar))
        opener.open('http://www.github.com')
        cookies = list(cookie_jar)
        print(cookies,"\n")
        print(cookies[0].name,"\n")
        print(cookies[0].value,"\n")
        print(cookies[0].domain,"\n")
        print(cookies[0].path,"\n")
        print(cookies[0].expires,"\n")
        print(datetime.datetime.fromtimestamp(cookies[0].expires),"\n")
        print(cookies[0].get_nonstandard_attr('HttpOnly'),"\n")
        print(cookies[0].secure)
#-------------------------------------------------------------------
def Methods():
    print("-----HTTP METHOD-----")
    print ("[a. Head Methods]")
    print ("[b. Post Methods)")
    y = input("masukan pilihan = ")
    if y == 'a':
        req = Request('http://www.google.com', method='HEAD')
        response = urlopen(req)
        print(response.status,"\n")
        print(response.read(),"\n")
    elif y == 'b':
        data_dict = {'P': 'Python'}
        data = urlencode(data_dict).encode('utf-8')
        req = Request('http://search.debian.org/cgi-bin/omega',data=data)
        req.add_header('Content-Type', 'application/x-www-form-urlencode;charset=UTF-8')
        response = urlopen(req)
        print(response.read(100))
#-------------------------------------------------------------------
daftar_isi()
pilihan = input("Masukan Pilihan = ")
if pilihan == '1':
    print("-----REQUEST WITH URLLIB-----")
    response = urlopen('https://www.debian.org')
    print(response,"\n")
    print(response.readline())
#-------------------------------------------------------------------
elif pilihan == '2':
    print("-----RESPONSE OBJECTS-----")
    response = urlopen('https://www.debian.org')
    print(response.url)
    response = urlopen('http://www.debian.org')
    print(response.read(50),"\n")
    print(response.read(),"\n")
    print(response.read())
#-------------------------------------------------------------------
elif pilihan == '3':
    print("-----STATUS CODE-----")
    response = urlopen('https://www.debian.org')
    print(response.status)
#-------------------------------------------------------------------
elif pilihan == '4': 
    print("-----HANDLING PROBLEMS-----")
    try:
        urlopen('http://www.ietf.org/rfc/rfc0.txt')
    except urllib.error.HTTPError as e:
        print('status', e.code)
        print('reason', e.reason)
        print('url', e.url,"\n")
    print(urlopen('http://192.0.2.1/index.html'))
#-------------------------------------------------------------------
elif pilihan == '5':
    print("-----HTTP HEADERS-----")
    response = urlopen('http://www.debian.org')
    print(response.getheaders())
#-------------------------------------------------------------------
elif pilihan == '6':
    print("-----CUSTOMIZING REQUEST-----")
    req = Request('http://www.debian.org')
    req.add_header('Accept-Language', 'sv')
    response = urlopen(req)
    print(response.readlines()[:5],"\n")
    req = Request('http://www.debian.org')
    req.add_header('Accept-Language', 'sv')
    print(req.header_items(),"\n")
    response = urlopen(req)
    print(req.header_items(),"\n")
    headers = {'Accept-Language': 'sv'}
    req = Request('http://www.debian.org', headers=headers)
    print(req.header_items())
#-------------------------------------------------------------------
elif pilihan == '7':
    print("-----CONTENT COMPRESSION-----")
    req = Request('http://www.debian.org')
    req.add_header('Accept-Encoding', 'gzip')
    response = urlopen(req)
    print(response.getheader('Content-Encoding'),"\n")
    content = gzip.decompress(response.read())
    print(content.splitlines()[:5],"\n")
    req = Request('http://www.debian.org')
    req.add_header('Accept-Encoding', 'identity')
    response = urlopen(req)
    print(response.getheader('Content-Encoding'))
#-------------------------------------------------------------------
elif pilihan == '8':
    print("-----MULTIPLE VALUES-----")
    req = Request('http://www.debian.org')
    encodings = 'deflate, gzip, identity'
    req.add_header('Accept-Encoding', encodings)
    response = urlopen(req)
    print(response.getheader('Content-Encoding'))
    encodings = 'gzip, deflate;q=0.8, identity;q=0.0'
#-------------------------------------------------------------------
elif pilihan == '9':
    print("-----CONTENT TYPES-----")
    response = urlopen('http://www.python.org')
    format, params = response.getheader('Content-Type').split(';')
    print(params,"\n")
    charset = params.split('=')[1]
    print(charset,"\n")
    content = response.read().decode(charset)

#-------------------------------------------------------------------
elif pilihan == '10':
    print("-----USER AGENTS-----")
    req = Request('http://www.python.org')
    urlopen(req)
    print(req.get_header('User-agent'),"\n")
    req = Request('http://www.debian.org')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64;rv:24.0) Gecko/20140722 Firefox/24.0 Iceweasel/24.7.0')
    response = urlopen(req)
#-------------------------------------------------------------------
elif pilihan == '11':
    Cookies()
#-------------------------------------------------------------------
elif pilihan == '12':
    print("-----REDIRECTS-----")
    req = Request('http://www.gmail.com')
    response = urlopen(req)
    print(response.url,"\n")
    print(req.redirect_dict)
#-------------------------------------------------------------------
elif pilihan == '13':
    print("-----URLs-----")
    result = urlparse('http://www.python.org/dev/peps')
    print(result,"\n")
    print(result.netloc,"\n")
    print(result.path,"\n")
    print(urlparse('http://www.python.org:8080/'),"\n")
#-------------------------------------------------------------------
elif pilihan == '14':
    print("-----PATHS AND RELATIVE URLS-----")
    print(urlparse('http://www.python.org/'),"\n")
    print(urlparse('../images/tux.png'),"\n")
    print(urljoin('http://www.debian.org', 'intro/about'),"\n")
    print(urljoin('http://www.debian.org/intro/', 'about'),"\n")
    print(urljoin('http://www.debian.org/intro', 'about'),"\n")
    print(urljoin('http://www.debian.org/intro/about', '/News'),"\n")
    print(urljoin('http://www.debian.org/intro/about/', '../News'),"\n")
    print(urljoin('http://www.debian.org/intro/about/', '../../News'),"\n")
    print(urljoin('http://www.debian.org/intro/about', '../News'),"\n")
    print(urljoin('http://www.debian.org/about', 'http://www.python.org'))
#-------------------------------------------------------------------
elif pilihan == '15': 
    print("-----QUERY STRINGS-----")
    urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default'),"\n"
    result = urlparse 
    print(parse_qs(result.query))
    result = urlparse 
    print(parse_qs(result.query),"\n")
#-------------------------------------------------------------------
elif pilihan == '16':
    print("-----URL ENCODING-----")
    print(quote('A duck?'),"\n")
    path = 'pypi'
    path_enc = quote(path)
    query_dict = {':action': 'search', 'term': 'Are you quite sure this is a cheese shop?'}
    query_enc = urlencode(query_dict)
    print(query_enc,"\n")
    netloc = 'pypi.python.org'
    print(urlunparse(('http', netloc, path_enc, '', query_enc, '')),"\n")

    path = '/images/users/+Zoot+/'
    print(quote(path),"\n")
    username = '+Zoot/Dingo+'
    path = 'images/users/{}'.format(username)
    print(quote(path),"\n")

    username = '+Zoot/Dingo+'
    user_encoded = quote(username, safe='')
    path = '/'.join(('', 'images', 'users', username))
#-------------------------------------------------------------------
elif pilihan == '17':
    Methods()
#-------------------------------------------------------------------
elif pilihan == '18': 
    print("-----REQUEST LIBRARY-----")
    import requests
    response = requests.get('http://www.debian.org')
    print(response.status_code,"\n")
    print(response.reason,"\n")
    print(response.url,"\n")
    print(response.headers['content-type'],"\n")
    print(response.ok,"\n")
    print(response.is_redirect,"\n")
    print(response.request.headers,"\n")
    print(response.headers['content-encoding'],"\n")
    print(response.content,"\n")
    print(response.text,"\n")
    print(response.encoding,"\n")
    response.encoding = 'utf-8'
    response = requests.get('http://www.github.com')
    print(response.cookies)
    s = requests.Session()
    s.get('http://www.google.com')
    response = s.get('http://google.com/preferences')
    response = requests.head('http://www.google.com')
    print(response.status_code,"\n")
    print(response.text,"\n")
    headers = {'User-Agent': 'Mozilla/5.0 Firefox 24'}
    response = requests.get('http://www.debian.org', headers=headers)
    params = {':action': 'search', 'term': 'Are you quite sure this is a cheese shop?'}
    response = requests.get('http://pypi.python.org/pypi',params=params)
    print(response.url,"\n")
    data = {'P', 'Python'}
    response = requests.post('http://search.debian.org/cgi-bin/omega', data=data)
#-------------------------------------------------------------------
elif pilihan == '19': 
    print("-----HANDLING ERRORS WITH REQUEST-----")
    response = requests.get('http://www.google.com/notawebpage')
    print(response.status_code,"\n")
    print(response.raise_for_status(),"\n")
    r = requests.get('http://www.google.com')
    print(r.status_code,"\n")
    print(r.raise_for_status(),"\n")
    print(r = requests.get('http://192.0.2.1'))
#-------------------------------------------------------------------
