#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void youtubeIcon() {
  byte bot_0[] = {B00011, B00100, B01000, B10000, B10000, B10000, B10000, B10000};
  byte bot_1[] = {B11111, B00000, B00000, B00100, B00110, B00111, B00111, B00111};
  byte bot_2[] = {B11111, B00000, B00000, B00000, B00000, B00000, B10000, B11000};
  byte bot_3[] = {B11000, B00100, B00010, B00001, B00001, B00001, B00001, B00001};

  byte top_0[] = {B10000, B10000, B10000, B10000, B10000, B01000, B00100, B00011};
  byte top_1[] = {B00111, B00111, B00111, B00110, B00100, B00000, B00000, B11111};
  byte top_2[] = {B11000, B10000, B00000, B00000, B00000, B00000, B00000, B11111};
  byte top_3[] = {B00001, B00001, B00001, B00001, B00001, B00010, B00100, B11000};

  lcd.createChar(0, bot_0); // bottom
  lcd.createChar(1, bot_1);
  lcd.createChar(2, bot_2);
  lcd.createChar(3, bot_3);

  lcd.createChar(4, top_0); // top
  lcd.createChar(5, top_1);
  lcd.createChar(6, top_2);
  lcd.createChar(7, top_3);
}
void youtubeIconDraw() {
  youtubeIcon();
  
  lcd.setCursor(0, 0); // bottom
  lcd.write(byte(0));
  lcd.setCursor(1, 0);
  lcd.write(byte(1));
  lcd.setCursor(2, 0);
  lcd.write(byte(2));
  lcd.setCursor(3, 0);
  lcd.write(byte(3));

  lcd.setCursor(0, 1); // top
  lcd.write(byte(4));
  lcd.setCursor(1, 1);
  lcd.write(byte(5));
  lcd.setCursor(2, 1);
  lcd.write(byte(6));
  lcd.setCursor(3, 1);
  lcd.write(byte(7));
}

String subData = "?";

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
}

void loop() {

  if (Serial.available()) {
    subData = Serial.readString();
    lcd.clear();
  }

  youtubeIconDraw();

  lcd.setCursor(5, 0);
  lcd.print("SubsCounter");
  lcd.setCursor(5, 1);
  lcd.print(subData); // subscribers data

  delay(50);
}

