from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os,json
import socket
import ssl
import sys, time
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
                    os.popen("ip -6 r add " + prefix + " encap seg6 mode " + encap + " segs "+ segments +" dev " + device)
                    #commandToShell += "ip -6 r add " + prefix + " encap seg6 mode " + encap + " segs "+ segments +" dev " + device+';'

                #os.system(commandToShell)

                #executionTime=time.time() - start_time                                    
                #print("Execution time: " + str(executionTime))                    
                self.send_response(200)
                return

            if self.path.endswith('del'):
                n = int(body['n'])
                commandToShell = ""
                for i in range(1,n+1):
                    prefix = body['prefix'+str(i)]
                    device = body['device'+str(i)]
                    os.popen("ip -6 r del " + prefix +" dev " + device)
                    #commandToShell += "ip -6 r del " + prefix +" dev " + device + ";"
                #os.system(commandToShell)
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



