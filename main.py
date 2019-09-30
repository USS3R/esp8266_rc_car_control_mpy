import machine
import usocket
from time import sleep
from wheels import Wheels


def get_header():
    return b"""HTTP/1.0 200 OK
    Content-Type: text/html; charset=utf-8
    Access-Control-Allow-Origin: *

"""


def get_page():
    _page = open('index.html', 'rb')
    cntx = _page.read()
    _page.close()
    return cntx


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
    if b"?" in url:
        (path, query) = url.split(b"?", 2)
    else:
        (path, query) = (url, b"")
    while True:
        header = socket.readline()
        if header == b"":
            return
        if header == b"\r\n":
            break
    if method == b"GET":
        if path == b"/":
            if query == b"":
                print('Received request %s' % query)
                print(get_page())
                resp(socket)
            elif query == b"index.html":
                print(get_page())
                resp(socket)
            elif query == b"action=fwd":
                print('Received request %s' % query)
                snd_confirm(socket)
                car.fwd(1000)
                sleep(3)
                car.stop()
            elif query == b"action=lfwd":
                print('Received request %s' % query)
                snd_confirm(socket)
                car.lfwd(1000)
                sleep(3)
                car.stop()
            elif query == b"action=rfwd":
                print('Received request %s' % query)
                snd_confirm(socket)
                car.rfwd(1000)
                sleep(3)
                car.stop()
            elif query == b"action=bwd":
                print('Received request %s' % query)
                snd_confirm(socket)
                car.bwd(1000)
                sleep(3)
                car.stop()
            elif query == b"action=lbwd":
                print('Received request %s' % query)
                snd_confirm(socket)
                car.lbwd(1000)
                sleep(3)
                car.stop()
            elif query == b"action=rbwd":
                print('Received request %s' % query)
                snd_confirm(socket)
                car.rbwd(1000)
                sleep(3)
                car.stop()
            elif query == b"action=lft":
                print('Received request %s' % query)
                snd_confirm(socket)
                car.lft(1000)
                sleep(3)
                car.stop()
            elif query == b"action=rght":
                print('Received request %s' % query)
                snd_confirm(socket)
                car.rght(1000)
                sleep(3)
                car.stop()
            elif query == b"action=stop":
                print('Received request %s' % query)
                snd_confirm(socket)
                car.stop()
            elif query == b"action=cleanup":
                print('Received request %s' % query)
                car.cleanup()
                snd_confirm(socket)
        elif path == b"/favicon.ico":
            pass
        else:
            car.stop()
            err_msg(socket, "404", "Unknown command!")
    elif method == b"POST":
        err_msg(socket, "501", "POST Not Implemented")


def init_srv():
    server = usocket.socket()
    server.bind(('', 80))
    server.listen(5)
    print('Started local web server')
    while True:
        try:
            (socket, sockaddr) = server.accept()
            handle(socket)
        finally:
            print('Close socket connection')
            socket.close()


init_srv()
