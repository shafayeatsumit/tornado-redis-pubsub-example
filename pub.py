import redis
import sys

config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}

r = redis.StrictRedis(**config)

if __name__ == '__main__':
    name = sys.argv[1]
    channel = sys.argv[2]

    print 'Welcome to {channel}'.format(**locals())

    while True:
        message = raw_input('Enter a message: ')

        if message.lower() == 'exit':
            break

        message = '{name} says: {message}'.format(**locals())

        r.publish(channel, message)