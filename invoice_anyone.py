import SimpleHTTPServer
import SocketServer
import cgitb
import cgi
import smtplib
import os

ms = raw_input("Enter your Text")

cgitb.enable()
PORT = 8000

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print "get"
        FROM = "artemisfowl901@gmail.com"
        TO = "samuelmayerhofer@gmail.com"
        message = ms
        username = "artemisfowl901@gmail.com"
        password = "thelowerelements"

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(FROM, [TO], message)
        server.quit()
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
         
    def do_POST(self):
        FROM = "artemisfowl901@gmail.com"
        TO = "samuelmayerhofer@gmail.com"
        message = ms
        username = "artemisfowl901@gmail.com"
        password = "thelowerelements"

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(FROM, [TO], message)
        server.quit()
                    

Handler = MyHandler
httpd = SocketServer.TCPServer(("", os.getenv(PORT,8080)), Handler)

print "serving at port", PORT
httpd.serve_forever()
   
