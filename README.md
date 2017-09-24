# Tornado WebSocket example

This is a websocket example written in python.

## Installation

1. `git clone https://github.com/shafayeatsumit/tornado-redis-pubsub-example`

2. `cd tornado-websocket-example`

3. `pip install -r requirements.txt`

4. `python app.py`

5. http://localhost:8888/


6. Send a REST call:


## REST API examples

Set the "id 1" value to 100 :
- `curl "localhost:8888/api?id=1&value=100"`

Set the "id 1" value to 300( The row No 1 will change to yellow ) :
- `curl "localhost:8888/api?id=1&value=300"`

Set The "id 1" value to 600( The row No 1 will change to red ):
- `curl "localhost:8888/api?id=1&value=600"`

- value 201 - 500 : change to yellow
- value 501 - : change to red

## PUBSUB Example.
1. run pub.py in another terminal

2. Write message 

3. See changes in localhost:8888
## License

MIT
