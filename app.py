from tornado import websocket, web, ioloop
import json
import redis

cl = []

config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}

r = redis.StrictRedis(**config)
pubsub = r.pubsub()

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")

class SocketHandler(websocket.WebSocketHandler):

    def check_origin(self, origin):
        print cl
        print "check_origin"
        return True

    def open(self):
        pubsub.subscribe("ch1")
        if self not in cl:
            print "open inside if"
            cl.append(self)
            print cl
        for item in pubsub.listen():
            print "item", item
            data = {"id": 1, "value" : item['data']}
            data = json.dumps(data)
            for c in cl:
                c.write_message(data)


    def on_message(self, message):
        print "GOt IT", message

    def on_close(self):
        if self in cl:
            print "on_close inside if"
            cl.remove(self)
            print cl

class ApiHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        self.finish()
        id = self.get_argument("id")
        value = self.get_argument("value")
        data = {"id": id, "value" : value}
        data = json.dumps(data)
        for c in cl:
            c.write_message(data)

    @web.asynchronous
    def post(self):
        pass

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    (r'/api', ApiHandler),
    (r'/(favicon.ico)', web.StaticFileHandler, {'path': '../'}),
    (r'/(rest_api_example.png)', web.StaticFileHandler, {'path': './'}),
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()
