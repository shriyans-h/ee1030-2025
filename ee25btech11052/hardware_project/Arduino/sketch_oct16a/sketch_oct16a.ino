#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup()
{
    lcd.begin(16, 2);
    Serial.begin(9600);
}
// V=n0 + n1 t + n2 t^2
// n0=1.248211
// n1 = 4.139786 x 10^-3
// n2= -7.0832954 x 10^-6
void loop()
{

    int reading = analogRead(A0);
    float voltage = 5.0 * reading / 1023.0;

    // --- Display on LCD ---
    lcd.setCursor(0, 1);   // Move to second row

    // --- Print to Serial Monitor ---
    Serial.print("Voltage: ");
    Serial.print(voltage, 3);
    Serial.println(" V");
    float temp = (voltage - 1.248211) * 1000 / (4.139786);
    Serial.println(temp, 2);
    lcd.print(temp,2);

    delay(1000); // Wait 1 second between updates
}
