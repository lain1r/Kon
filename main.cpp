#include <Arduino.h>

// структура передаваемых данных
struct Data {
  int32_t num1 = 0;
  int32_t num2 = 0;
};

// данные
Data data;
// указатель на данные
uint8_t *dataP;

void setup() {
  // Говорим что пины в режиме ввода
  pinMode(10, INPUT);
  pinMode(11, INPUT);

  // Иницируем подключение по сериал порту
  Serial.begin(9600);
  
  // Получаем адрес в памяти для переменной data
  dataP = (uint8_t *)&data;
}

void loop() {
  data.num1 = analogRead(A0);
  
  if((digitalRead(10) != 1)||(digitalRead(11) != 1)){
    Serial.write(dataP, sizeof(Data));
  }
    // Serial.println(analogRead(A0));

  //Wait for a bit to keep serial data from saturating
  delay(1);
}

// void setup() {
//   // initialize the serial communication:
//   Serial.begin(9600);
//   pinMode(10, INPUT); // Setup for leads off detection LO +
//   pinMode(11, INPUT); // Setup for leads off detection LO -

// }

// void loop() {
  
  
//     // send the value of analog input 0:
//       Serial.println(analogRead(A0));
//   //Wait for a bit to keep serial data from saturating
//   delay(1);
// }