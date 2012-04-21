int ledpin = 13;
int val = 0;

void setup() {
 pinMode(ledpin,OUTPUT);
  Serial.begin(9600); 
}
void loop() {
	if(Serial.available()) {
		val = Serial.read();
		if(val > '0' && val <= '9') {
			Serial.println(val);
			val = val - '0';
			for(int i = 0; i < val; ++i) {
				Serial.println("Blink!");
				digitalWrite(ledpin, HIGH);
				delay(150);
				digitalWrite(ledpin, LOW);
				delay(150);
			}
		}
	}
}
