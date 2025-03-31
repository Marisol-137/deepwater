volatile int pulseCount = 0;
unsigned long previousMillis = 0;
float flowRate;

// Pin where the sensor is connected
const int sensorPin = 4;

void IRAM_ATTR pulseCounter() {
  pulseCount++;
}

void setup() {
  Serial.begin(115200);
  pinMode(sensorPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(sensorPin), pulseCounter, RISING);
  previousMillis = millis();
}

void loop() {
  if (millis() - previousMillis >= 1000) { // Update every 1 second
    detachInterrupt(digitalPinToInterrupt(sensorPin));

    // The YF-S401 sensor outputs approximately 98 pulses per liter
    flowRate = (pulseCount / 98.0); // liters per second
    flowRate = flowRate * 60; // Convert to liters per minute

    Serial.print("Flow Rate: ");
    Serial.print(flowRate);
    Serial.println(" L/min");

    pulseCount = 0;
    previousMillis = millis();

    attachInterrupt(digitalPinToInterrupt(sensorPin), pulseCounter, RISING);
  }
}