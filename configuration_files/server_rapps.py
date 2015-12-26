import SocketServer
from parser import Parser

class AlfaTCPHandler(SocketServer.BaseRequestHandler):

  # Handle the AndroidApp request
  def handle(self):
    self.data = self.request.recv(1024).strip()
    print "REQUEST RECEIVED"
    # Parse the Json file
    parser = Parser()
    parser.parseJson(self.data)

# Stablish connections with the AndroidApp
if __name__ == "__main__":
  # TODO define HOST/PORT
  HOST, PORT = "10.0.0.1", 7394
  server = SocketServer.TCPServer((HOST,PORT),AlfaTCPHandler)
  server.serve_forever()
