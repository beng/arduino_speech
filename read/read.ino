int ledPin = 9;
int val = 0;
char msg = '  ';

void setup() {
  pinMode(ledPin, OUTPUT);      // declare LED as output
  Serial.begin(9600);
  Serial.print("launch sequence success\n");
}

void loop(){        
	while (Serial.available()>0){
		msg=Serial.read();
	}

  // use 'Y' or 'N' to dictate status of light
  // using lowercase seems to make it crash, why?
  if (msg=='Y') {  // comapring ASCII value, cant use .equals on char :/
    digitalWrite(ledPin, HIGH);
    Serial.print("Houston, we are lit!\n");
    msg=' ';
  } else if (msg=='N') {
    digitalWrite(ledPin, LOW);
  }
}

