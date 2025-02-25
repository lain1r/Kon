void setup() {
  Serial.begin(9600); // Настройка скорости передачи
}

void loop() {
  // Чтение данных с аналоговых пинов A0 и A1
  int sensor1 = analogRead(A0);
  int sensor2 = analogRead(A1);
  
  // Отправка данных в формате: "значение1,значение2\n"
  Serial.print(sensor1);
  Serial.print(",");
  Serial.println(sensor2); // println добавляет символ новой строки
  
  delay(50); // Задержка для стабильности передачи
}