import socket
from os import error
import requests

URL = 'http://web.stanford.edu/dept/its/support/techtraining/techbriefing-media/Intro_Net_91407.ppt'
HOST = URL.split('/')[2]
PATH = URL.split(f'http://{HOST}')[1]
if PATH == '': 
    PATH = '/'
print(PATH)
PORT = 80

info = requests.head(URL)
contentLength = int(info.headers.get('content-length', None))
st = len(info.headers)
print(info.headers)

def _save_file(Name_file, data):
    f = open(Name_file, 'wb+')
    f.write(data)
    f.close()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
    print(f'* Running on http://{HOST}:{PORT}')
except socket.error as e:
    print(f'socket error: {e}')

request = f"GET {PATH} HTTP/1.0\r\nHost: {HOST}\r\n\r\n"

print(info)
client.send(request.encode())

data = client.recv(5000000)


request_line = request.split('\r\n')[0]
request_method = request_line.split(' ')[0]

request_line1 = PATH.split('/')[-1]
print(request_line1)
request_file = request_line1.split('.')[-1]
print(request_file)

if request_method == 'GET':
    if  PATH == '/' or request_file == 'html':
        #index_page
        url = 'index.html'
    elif request_file == 'ppt':
        url = 'Intro_Net_91407.ppt'
    elif request_file == 'pdf':
        url = 'intro.pdf'
print(url)
_save_file(url, data) 

# def mysend(self, msg):
#         totalsent = 0
#         while totalsent < contentLength:
#             sent = self.sock.send(msg[totalsent:])
#             if sent == 0:
#                 raise RuntimeError("socket connection broken")
#             totalsent = totalsent + sent

# def myreceive(self):
#         msg = b''
#         while len(msg) < contentLength:
#             chunk = self.sock.recv(contentLength-len(msg))
#             if chunk == b'':
#                 raise RuntimeError("socket connection broken")
#             msg = msg + chunk
#         return msg


client.close()
