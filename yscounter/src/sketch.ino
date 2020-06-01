#include <LiquidCrystal.h>


/*

 YSCounter - Arduino code

 YouTube Subscriber Counter with Arduino and Python (Without API key).

 The circuit:
 * LCD RS pin to digital pin 12
 * LCD Enable pin to digital pin 11
 * LCD D4 pin to digital pin 5
 * LCD D5 pin to digital pin 4
 * LCD D6 pin to digital pin 3
 * LCD D7 pin to digital pin 2
 * LCD R/W pin to ground
 * 10K resistor
 * ends to +5V and ground
 * wiper to LCD VO pin (pin 3)
 
 Version: 1.3.0
 Author: Adil Gürbüz
 Contact: adlgrbz@tutamail.com
 Source: https://github.com/adlgrbz/yscounter
 
 Thank you "GizliProfesor" and "youtube.com/nepercos" !

*/


LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

String subscriber_data = "?";

void icon() {
  byte bot_0[] = {
    B00011, B00100, B01000, B10000, B10000, B10000, B10000, B10000
  };
  byte bot_1[] = {
    B11111, B00000, B00000, B00100, B00110, B00111, B00111, B00111
  };
  byte bot_2[] = {
    B11111, B00000, B00000, B00000, B00000, B00000, B10000, B11000
  };
  byte bot_3[] = {
    B11000, B00100, B00010, B00001, B00001, B00001, B00001, B00001
  };

  byte top_0[] = {
    B10000, B10000, B10000, B10000, B10000, B01000, B00100, B00011
  };
  byte top_1[] = {
    B00111, B00111, B00111, B00110, B00100, B00000, B00000, B11111
  };
  byte top_2[] = {
    B11000, B10000, B00000, B00000, B00000, B00000, B00000, B11111
  };
  byte top_3[] = {
    B00001, B00001, B00001, B00001, B00001, B00010, B00100, B11000
  };

  lcd.createChar(0, bot_0);
  lcd.createChar(1, bot_1);
  lcd.createChar(2, bot_2);
  lcd.createChar(3, bot_3);

  lcd.createChar(4, top_0);
  lcd.createChar(5, top_1);
  lcd.createChar(6, top_2);
  lcd.createChar(7, top_3);
}

void icon_draw() {
  icon();

  lcd.setCursor(0, 0);
  lcd.write(byte(0));
  lcd.setCursor(1, 0);
  lcd.write(byte(1));
  lcd.setCursor(2, 0);
  lcd.write(byte(2));
  lcd.setCursor(3, 0);
  lcd.write(byte(3));

  lcd.setCursor(0, 1);
  lcd.write(byte(4));
  lcd.setCursor(1, 1);
  lcd.write(byte(5));
  lcd.setCursor(2, 1);
  lcd.write(byte(6));
  lcd.setCursor(3, 1);
  lcd.write(byte(7));
}

void setup() {
  Serial.begin(9600);

  lcd.begin(16, 2);
}

void loop() {
  if (Serial.available()) {
    subscriber_data = Serial.readString();

    lcd.clear();
  }

  icon_draw();

  lcd.setCursor(5, 0);
  lcd.print("YSCounter");
  lcd.setCursor(5, 1);
  lcd.print(subscriber_data);

  delay(500);
}
