import sys
from time import sleep
import usocket
from car_wheels import Car


def get_page():
    with open('index.html', 'rb') as _page:
        return _page.read()


car = Car()
cmd_list = {
    "forward": car.move_forward,
    "backward": car.move_backward,
    "forward_right": car.move_forward_right,
    "forward_left": car.move_forward_left,
    "backward_right": car.move_backward_right,
    "backward_left": car.move_backward_left,
    "stop": car.stop,
    "cleanup": car.cleanup,
    "index.html": get_page
}


def init_srv():
    server = usocket.socket()
    server.bind(('', 8989))
    server.listen(5)
    print('Started local web server')
    while True:
        (socket, sockaddr) = server.accept()
        try:
            handle(socket)
        except TypeError:
            print("Exception - TypeError: can't convert 'str' object to bytes "
                  "implicitly")
        finally:
            print('Close socket connection')
            socket.close()


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
    socket.write(get_page())
    sleep(0.2)


def err_msg(socket, err_code, er_msg):
    socket.write("HTTP/1.1 400 NOK" + err_code + ": " + er_msg + "\n")


def handle(socket):
    (method, url, version) = socket.readline().split(b" ")
    url = str(url.decode('utf-8'))
    print("Url: {}".format(url))
    method = str(method.decode('utf-8'))
    print("Method: {}".format(method))
    if "/" in url:
        (path, query) = url.split("/", 2)
    else:
        (path, query) = (url, "")
    query = query.replace('?', '')
    print("Path: {}\nQuery: {}".format(path, query))
    while True:
        header = str(socket.readline().decode('utf-8'))
        if header == "":
            return
        if header == "\r\n":
            break
    if method == "GET":
        if path == "":
            resp(socket)
            if '=' in query:
                (qry, param) = query.split('=', 1)
            else:
                qry = query
                param = None
            print("Qry: {}\tParam: {}".format(qry, param))

            # if qry in cmd_list:
            #     snd_confirm(socket)
            #     cmd_list[qry](param)
            # else:
            #     car.stop()
            #     print("unknown_command")
            #     err_msg(socket, b"404", b"Unknown command!")
        else:
            car.stop()
            print("unknown_command")
            err_msg(socket, b"404", b"Unknown command!")
    elif method == "POST":
        print("unknown_command")
        err_msg(socket, b"501", b"POST Not Implemented")


def check_time():
    yr = int(utime.localtime()[0])
    if yr != 2020:
        try:
            ntptime.settime()
            print("Time updated")
        except OSError:
            print("NTP update time exception")
        finally:
            ntptime.settime()
