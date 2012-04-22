int ledPin = 9;  // choose the pin for the LED
int val = 0;      // variable for reading the pin status
char msg = '  ';   // variable to hold data from serial

void setup() {
  pinMode(ledPin, OUTPUT);      // declare LED as output
  Serial.begin(9600);
  Serial.print("launch sequence success!\n");
}

void loop(){       
	while (Serial.available()>0){
		msg=Serial.read();
	}

  // use 'on' or 'off' to dictate status of light
  if (msg.equals("ON") || msg.equals("on") {	// cant find an ignorecase
    digitalWrite(ledPin, HIGH);
    Serial.print("Houston, we are lit!");
    Serial.print("LED Activated\n");
    msg=' ';
  } else if (msg.equals("OFF") || msg.equals("off")) {
    digitalWrite(ledPin, LOW); 
  }
}

