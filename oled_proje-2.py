from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)

oled = SSD1306_I2C(128, 64, i2c)

bt1 = Pin(14,Pin.IN,Pin.PULL_DOWN)
bt2 = Pin(13,Pin.IN,Pin.PULL_DOWN)
bt3 = Pin(12,Pin.IN,Pin.PULL_DOWN)
bt4 = Pin(11,Pin.IN,Pin.PULL_DOWN)

a = 0
x1 = 15
x2 = 15
sayilar = 0
x_ekseni = 8
y_ekseni = 38
kontrol = 0
sayi1 = " "
sayi2 = " "
durum = 0
sonuc = " "
operatör = " "
op = 0

def standartgorunum():
    oled.text("Hesap Makinesi",14,0)
    oled.hline(0, 16, 127, 1)
    oled.hline(0, 30, 127, 1)
    oled.show()
    
def buttonolustur():
    x1 = 5
    x2 = 5
    sayilar = 0
    for i in range (0,5):
        oled.rect(x2,33,15,15,1)
        oled.text(str(sayilar),(x2 + 3),36)
        sayilar = sayilar + 1
        i= 1 + i
        x2 = 20 + x2
        
    for n in range (0,5):
        oled.rect(x1,50,15,14,1)
        oled.text(str(sayilar),(x1 + 3),53)
        sayilar = sayilar + 1
        n= 1 + n
        x1 = 20 + x1

    oled.show()
    
    
        
    

def işlemler():
    oled.rect(103,33,15,15,1)
    oled.text("+",107,37)
    oled.rect(103,50,15,14,1)
    oled.text("-",107,54)



while True:
    buttonolustur()
    standartgorunum()
    işlemler()
    
    if bt1.value() == 1:
        x_ekseni = x_ekseni + 20
        if x_ekseni > 108:
            x_ekseni = 108
        time.sleep(0.5)
        oled.fill(0)
        oled.text("_",x_ekseni,y_ekseni)
        
    if bt2.value() == 1:
        x_ekseni = x_ekseni - 20
        if x_ekseni < 8:
            x_ekseni = 8
        time.sleep(0.5)
        oled.fill(0)
        oled.text("_",x_ekseni,y_ekseni)
    
    if bt3.value() == 1:
        a = 1
        y_ekseni = y_ekseni + 17
        if y_ekseni > 55:
            y_ekseni = 55
        time.sleep(0.5)
        oled.fill(0)
        oled.text("_",x_ekseni,y_ekseni)
        
    if bt3.value() and a == 1:
        a = 0
        y_ekseni = y_ekseni - 17
        if y_ekseni < 17:
            y_ekseni = 17
        time.sleep(0.5)
        oled.fill(0)
        oled.text("_",x_ekseni,y_ekseni)
    
    if bt4.value() == 1:
        durum = durum + 1
        oled.fill(0)
        if x_ekseni == 8 and y_ekseni == 38:
            kontrol = "0"
        if x_ekseni == 28 and y_ekseni == 38:
            kontrol = "1"
        if x_ekseni == 48 and y_ekseni == 38:
            kontrol = "2"
        if x_ekseni == 68 and y_ekseni == 38:
            kontrol = "3"
        if x_ekseni == 88 and y_ekseni == 38:
            kontrol = "4"        
        if x_ekseni == 108 and y_ekseni == 38:
            operatör = "+"
            op = op + 1
            sonuc = int(sayi1) + int(sayi2)
         
        if x_ekseni == 8 and y_ekseni == 55:
            kontrol = "5"
        if x_ekseni == 28 and y_ekseni == 55:
            kontrol = "6"
        if x_ekseni == 48 and y_ekseni == 55:
            kontrol = "7"
        if x_ekseni == 68 and y_ekseni == 55:
            kontrol = "8"
        if x_ekseni == 88 and y_ekseni == 55:
            kontrol = "9"
        if x_ekseni == 108 and y_ekseni == 55:
            operatör = "-"
            sonuc = int(sayi1) - int(sayi2)
                    
    if durum == 1:
        time.sleep(0.1)
        sayi1 = kontrol
    if durum == 2:
        time.sleep(0.1)
        sayi2 = kontrol
    if durum > 2:
        time.sleep(0.1)
        durum = 0
    
    if op > 1:
        if operatör == "+":
            sayi1 = sonuc

    """print("durum = ",durum)
    print("sayı1 = ",sayi1)
    print("sayı2 = ",sayi2)
    print("x = ",sonuc)"""
        
    oled.text(str(sayi1),0,20)
    oled.text(str(operatör),10,20)
    oled.text(str(sayi2), 20,20)
    oled.text("=",30,20)
    oled.text(str(sonuc),40,20)

    oled.show()