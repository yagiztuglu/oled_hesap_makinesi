import machine
import time

zaman = 0
a = 0
yol = 100 #cm
hiz = 0
 
sensor1 = machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)
sensor2= machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_DOWN)
servo = machine.PWM(machine.Pin(19,machine.Pin.OUT))

def mapservo(value, in_min, in_max, out_min, out_max):
  return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def acı(angle):
    servo.duty_u16(mapservo(angle,0,180,20,120))
    
def kontrol():
    if sensor1.value() == 1:
        zaman = zaman + 1
        time.sleep(1)
        a = 1
    if sensor2.value() == 1 and a == 1:
        a = 0
        return zaman

def hizölç():
    hiz = yol / (zaman + 0.1)
    return hiz
    
while True:
    acı(0)
    kontrol()
    hizölç()
    
    if hiz <= 3:
        print("hızınız normal")
    elif hiz > 3 and hiz <= 8:
        print("hızlısınız")
        acı(20)
    elif hiz > 8 :
        print("aşırı hızlısınız")
        acı(40)
    