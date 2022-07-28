#include <Servo.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
#define Buton 8
#define Led 10
#define sensor1 13
#define sensor2 12


Servo servo;

unsigned long b;
int a = 0;
int gecen_sure;

float hiz;


void setup() {
  Serial.begin(9600);
  pinMode(Buton, INPUT);
  pinMode(Led, OUTPUT);
  pinMode(2, INPUT);
  servo.attach(9);
}

void loop() {
  delay(100);
  servo.write(0);
  delay(100);
  int sensor1dur = digitalRead(sensor1);
  int sensor2dur = digitalRead(sensor2);
  Serial.println(sensor1dur);
  Serial.println(sensor2dur);
  delay(300);

  if (sensor1dur == 0) {
    Serial.println("birinci durum bekleniyor");
    delay(500);
  }
  else if (sensor2dur == 0) {
    lcd.clear();
    b = millis();
    Serial.print("Başlangıçtan beri geçen zaman:");
    Serial.println(b);
    delay(200);
    gecen_sure = b / 1000 - a;
    a = a + 2 + gecen_sure;
    //biz yolu 10 metre olarak yaptık siz kendi ölçüm alanınıza burayaı değiştirebilirsiniz (birim cm)
    hiz = 1000 / gecen_sure;
    delay(100);
    Serial.println("Alınan yol : 10 metre");
    Serial.print("geçen süre");
    Serial.println(gecen_sure);
    hizolc();
    kasis(hiz);
    delay(5000);
  }
}
void kasis(int hizi) {
  if (hizi > 10) {
    delay(500);
    servo.write(50);
    Serial.println("Aşırı hızlısın");
    delay(10000);
    lcd_yaz("Asiri hizlisiniz");
  }
  else if (hizi > 3) {
    delay(500);
    servo.write(120);
    lcd_yaz("hizlisin");

  }
  else {
    Serial.println("Hızınız normal.");
    delay(2000);
    lcd_yaz("hizini normal");
  }
}



void hizolc() {
  hiz = 10000 / gecen_sure;
  hiz = hiz / 100;
  Serial.print("Hızınız");
  Serial.println(hiz);
  delay(200);
  return hiz;
}

void lcd_yaz(String msg) {
  lcd.setCursor(0, 0);
  lcd.print(msg);
  delay(1000);
  lcd.setCursor(1, 0);
  lcd.print("kasis kalkiyor");
}
