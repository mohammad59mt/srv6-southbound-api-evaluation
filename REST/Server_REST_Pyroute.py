# !/usr/bin/python


# Copyright (C) 2018 Pier Luigi Ventre, Stefano Salsano, Alessandro Masci - (CNIT and University of Rome "Tor Vergata")
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Python implementation of SRv6 functions over HTTP server side
#
# @author Pier Luigi Ventre <pier.luigi.ventre@uniroma2.it>
# @author Stefano Salsano <stefano.salsano@uniroma2.it>
# @author Alessandro Masci <mascialessandro89@gmail.com>
#

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os,json
import socket
import ssl
import sys, time
from socket import AF_INET
from pyroute2 import IPRoute
#Create custom HTTPRequestHandler class
class SRHTTPRequestHandler(BaseHTTPRequestHandler):
    
    #handle GET command
    def do_GET(self):
        command = "ip -6 r"
        try:
            if self.path.endswith('list'):
                res = os.popen(command).read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(res)
                #self.wfile.close()
               
        except IOError:
            self.send_error(400, 'Bad request')

    #prevent print messages
    def log_message(self, format, *args):
        return

    #handle POST command
    def do_POST(self):
        try:
            content_len = int(self.headers.getheader('content-length', 0))
            post_body = self.rfile.read(content_len)
            body = json.loads(post_body)

            ip = IPRoute()
            
            if self.path.endswith('addsr'):
                commandToShell = ""
                #start_time = time.time()                            
                n = int(body['n'])
                for i in range(1,n+1):
                    prefix = body['prefix'+str(i)]
                    encap = body['encapmode'+str(i)]
                    length = len(body['segments'+str(i)])
                    segments = ""
                    for j in range(0,length):
                        seg = body['segments'+str(i)][j]
                        if j == length-1:
                            segments += seg
                        else:
                            segments += seg+","
                    device = body['device'+str(i)]
                    idx = ip.link_lookup(ifname=device)[0]
                    ip.route('add',
                      dst=prefix+'/128',
                      oif=idx,
                      encap={'type': 'seg6','mode': encap,'segs': segments})
                ip.close()
                #executionTime=time.time() - start_time                                    
                #print("Execution time: " + str(executionTime))                    
                
                self.send_response(200)
                return

            if self.path.endswith('del'):
                n = int(body['n'])
                for i in range(1,n+1):
                    prefix = body['prefix'+str(i)]
                    device = body['device'+str(i)]
                    idx = ip.link_lookup(ifname=device)[0]
                    ip.route('delete',
                      dst=prefix+'/128',
                      oif=idx)
                ip.close()
                self.send_response(200)
                return

        except IOError:
            self.send_error(400, 'Bad request')

class HTTPServerV6(HTTPServer):
  address_family = socket.AF_INET6
    
def run(security_mode):
    server_address_IP = '2002::1'
    print('http server is starting...')
    if security_mode == "secure":
        server_address = (server_address_IP, 443)
        httpd = HTTPServerV6(server_address, SRHTTPRequestHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.pem', server_side=True)
    elif security_mode == "insecure":
        server_address = (server_address_IP, 80)
        httpd = HTTPServerV6(server_address, SRHTTPRequestHandler)
    
    #ip and port of servr
    #by default http server port is 80
    
    print('http server is running...')
    httpd.serve_forever()
    
if __name__ == '__main__':
    if sys.argv[1] is not None:
        security_mode = sys.argv[1]
        run(security_mode)
    else:
        print("select either secure or inscure mode (e.g., sudo python <fileName.py> secure ....)")



