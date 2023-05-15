import network
import time
import urequests
from machine import Pin

request = None

def gpio_set(pin,value):
  if value >= 1:
    Pin(pin, Pin.OUT).on()
  else:
    Pin(pin, Pin.OUT).off()


sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()
#sta_if.connect('SABAZERA_EXT','00112233445566778899')
print("Esperando conexao Wifi")
while not sta_if.isconnected(): time.sleep(1)
print("Conectado! :)")
while True:
  request = urequests.get('http://35.223.182.128/')

  if (request.status_code) == 200:
    if (request.content.decode('UTF-8')) == '0':
      gpio_set((4), True)
      gpio_set((2), False)
      gpio_set((16), False)
    elif (request.content.decode('UTF-8')) == '1':
      gpio_set((4), False)
      gpio_set((2), True)
      gpio_set((16), False)
    elif (request.content.decode('UTF-8')) == '2':
      gpio_set((4), False)
      gpio_set((2), False)
      gpio_set((16), True)
    else:
      gpio_set((4), True)
      gpio_set((2), True)
      gpio_set((16), True)
    print('Success. Response content: ' + str(request.content.decode('UTF-8')))
  else:
    print('Request Error. Status code = ' + str(request.status_code))



#####################


import network
import time
import urequests
from machine import Pin

request = None

def gpio_set(pin,value):
  if value >= 1:
    Pin(pin, Pin.OUT).on()
  else:
    Pin(pin, Pin.OUT).off()


sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()
sta_if.connect('SABAZERA_EXT','00112233445566778899')
print("Waiting for Wifi connection")
while not sta_if.isconnected(): time.sleep(1)
print("Connected")
while True:
  request = urequests.get('http://34.70.208.229')

  if (request.status_code) == 200:
    if (str(request.content)) == "b'0'":
      gpio_set((15), True)
      gpio_set((2), False)
      gpio_set((4), False)
    elif (str(request.content)) == "b'1'":
      gpio_set((15), False)
      gpio_set((2), True)
      gpio_set((4), False)
    elif (str(request.content)) == "b'2'":
      gpio_set((15), False)
      gpio_set((2), False)
      gpio_set((4), True)
    else:
      for count in range(5):
        time.sleep(1)
        gpio_set((15), False)
        gpio_set((2), False)
        gpio_set((4), False)
        time.sleep(1)
        gpio_set((15), True)
        gpio_set((2), True)
        gpio_set((4), True)
    print('Success. Response content: ' + str(str(request.content)))
  else:
    print('Request Error. Status code = ' + str(request.status_code))
