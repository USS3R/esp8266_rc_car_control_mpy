import machine
import usocket
from time import sleep
from wheels import Car
import sys

car = Car()
_car_cmd = {
    "forward": car.move_forward,
    "backward": car.move_backward,
    "forward_right": car.move_forward_right,
    "forward_left": car.move_forward_left,
    "backward_right": car.move_backward_right,
    "backward_left": car.move_backward_left,
    "stop": car.stop,
    "cleanup": car.cleanup
}


def get_header():
    return b"""HTTP/1.0 200 OK
    Content-Type: text/html; charset=utf-8
    Access-Control-Allow-Origin: *
    \r\n
    """


def get_page():
    with open('index.html', 'rb') as _page:
        return _page.read()


def snd_confirm(socket):
    socket.send(get_header())


def resp(socket):
    socket.send(get_header())
    socket.write(get_page().decode("utf-8"))
    sleep(0.2)


def err_msg(socket, err_code, er_msg):
    socket.write("HTTP/1.1 400 NOK - " + err_code + ": " + er_msg + "\n")


def handle(socket):
    car = Wheels(machine)
    (method, url, version) = socket.readline().split(b" ")
    url = str(url.decode('utf-8'))
    method = str(method.decode('utf-8'))
    if "?" in url:
        (path, query) = url.split("?", 2)
    else:
        (path, query) = (url, "")
    while True:
        header = str(socket.readline().decode('utf-8'))
        if header == "":
            return
        if header == "\r\n":
            break
    if method == "GET":
        if path == "/":
            if query == "":
                print('Received request %s' % query)
                print(get_page())
                resp(socket)
            elif query == "index.html":
                print(get_page())
                resp(socket)

        elif path == "/favicon.ico":
            pass
        else:
            car.stop()
            err_msg(socket, "404", "Unknown command!")
    elif method == "POST":
        err_msg(socket, "501", "POST Not Implemented")


def init_srv():
    server = usocket.socket()
    server.bind(('', 80))
    server.listen(5)
    (socket, sockaddr) = server.accept()
    print('Started local web server')
    while True:
        try:
            handle(socket)
        except KeyboardInterrupt:
            print("Terminating ...")
            sys.exit()
        finally:
            print('Close socket connection')
            socket.close()


init_srv()
