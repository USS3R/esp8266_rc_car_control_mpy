import esp
import uos
import gc
import webrepl
import network
import ntptime
import utime


_SSID = 'Us3r'
_PWD = '06432409'
_STA = network.WLAN(network.STA_IF)
_AP = network.WLAN(network.AP_IF)
_AP_SSID = "ESP_PLANT"
_AP_PWD = "Nhfdrf_13"


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


def start_sta():
    if not _STA.active():
        _STA.active(True)
    _STA.connect(_SSID, _PWD)
    while not _STA.isconnected():
        pass
    print(_STA.ifconfig())


def stop_ap():
    if _AP.active():
        print("Terminated AP WiFi connection")
        _AP.active(False)
    print("Successfully terminated WiFi AP mode")


check_time()
start_sta()
stop_ap()
print("Starting WebRepl ...")
webrepl.start()
