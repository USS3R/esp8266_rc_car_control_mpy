import machine
import usocket
from time import sleep
from wheels import Car


car = Car()


def get_page():
    with open('index.html', 'rb') as _page:
        return _page.read()


_car_cmd = {
    "index.html": get_page,
    "forward": car.forward,
    "backward": car.backward,
    "left": car.left,
    "right": car.right,
    "forward_right": car.forward_right,
    "forward_left": car.forward_left,
    "backward_right": car.backward_right,
    "backward_left": car.backward_left,
    "stop": car.stop,
    "favicon.ico": car.skip,
    "cleanup": car.cleanup
}


def get_header():
    return b"""HTTP/1.0 200 OK
    Content-Type: text/html; charset=utf-8
    Access-Control-Allow-Origin: *
    \r\n
    """


def snd_confirm(socket):
    socket.send(get_header())


def resp(socket):
    socket.send(get_header())
    socket.write(get_page().decode("utf-8"))
    sleep(0.2)


def err_msg(socket, err_code, er_msg):
    socket.write("HTTP/1.1 400 NOK - " + err_code + ": " + er_msg + "\n")


def handle(socket):
    (method, url, version) = socket.readline().split(b" ")
    method = str(method.decode('utf-8'))
    url = str(url.decode('utf-8'))
    if "/" in url:
        (path, query) = url.split("/", 1)
    else:
        (path, query) = (url, "")
    while True:
        header = str(socket.readline().decode('utf-8'))
        if header == "":
            return
        if header == "\r\n":
            break
    if method == "GET":
        if path == "":
            query = query.replace('?', '')
            if '=' in query:
                qry = query.split('=', 1)[0]
                param = query.split('=', 1)[1]
                if qry in _car_cmd:
                    print('Received request %s' % qry)
                    snd_confirm(socket)
                    _car_cmd[qry](param)
                    sleep(1)
                    car.stop()
                else:
                    car.stop()
                    err_msg(socket, "404", "Unknown command!")
            else:
                qry = query
                if qry in _car_cmd:
                    print('Received request %s' % qry)
                    snd_confirm(socket)
                    _car_cmd[qry]()
                    sleep(1)
                    car.stop()
                else:
                    car.stop()
                    err_msg(socket, "404", "Unknown command!")
        else:
            car.stop()
            err_msg(socket, "404", "Unknown command!")
    elif method == "POST":
        err_msg(socket, "501", "POST Not Implemented")


def init_srv():
    server = usocket.socket()
    _port = 8989
    server.bind(('', _port))
    server.listen(5)
    print('Starting local web server on: {}'.format(_port))
    while True:
        (socket, sockaddr) = server.accept()
        try:
            handle(socket)
        except KeyboardInterrupt:
            print("Terminating ...")
            socket.close()
            sys.exit()
        finally:
            print('Close socket connection...')
            socket.close()


init_srv()
