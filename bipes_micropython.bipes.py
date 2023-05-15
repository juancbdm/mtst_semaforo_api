import network
import urequests as requests
import ujson
import time
from machine import Pin

def gpio_set(pin, value):
    if value >= 1:
        Pin(pin, Pin.OUT).on()
    else:
        Pin(pin, Pin.OUT).off()

def wifi_conn(ssid, passwd):
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(True)
    ap_if.active(False)
    sta_if.connect(ssid, passwd)
    if sta_if.isconnected():
        print("Conectado! :)")

wifi_conn("SABAZERA_EXT", "00112233445566778899")

while True:
    res = requests.get('http://ec2-3-237-106-251.compute-1.amazonaws.com/')
    print(res.text)
    parsed = ujson.loads(""+res.text+"")
    parseds = ujson.loads(""+parsed+"")
    parsedVal = parseds["valueS"]

    if (res.status_code == 200):
        if parsedVal == '0':
            print('0')
            gpio_set((0), False)
            gpio_set((4), False)
            gpio_set((5), True)  # vermelho
        elif parsedVal == '1':
            print('1')
            gpio_set((0), True)  # verde
            gpio_set((4), False)
            gpio_set((5), False)
        elif parsedVal == '2':
            print('2')
            gpio_set((0), False)
            gpio_set((4), True)  # amarelo
            gpio_set((5), False)
        else:
            print('else')
            gpio_set((0), True)
            gpio_set((4), True)
            gpio_set((5), True)

        time.sleep(1)

    else:
        res.close()
        break ;
