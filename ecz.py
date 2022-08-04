import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world!!")
class ESPhandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world ESP please")
    def post(self):
       if self.request.headers['Content-Type'] == 'image/jpg':
           self.write("Got img wild")
           print('got img cats')
           img = self.request.body
           file = open('imgtest1.jpg', 'wb')
           file.write(bytearray(img))
           file.close


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/ESP", ESPhandler)
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

