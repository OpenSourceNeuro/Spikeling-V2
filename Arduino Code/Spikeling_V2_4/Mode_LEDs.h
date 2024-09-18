/*       --- Mode LEDs are controled through ChaliePlexing --- 

Charlieplexing not only takes advantage of the two states that are normally changed, HIGH and LOW, but also 
uses a third state by changing between OUTPUT and INPUT modes, which affects internal resistors on the microcontroller
The exact number of LEDs that can be controled with a given number of pins is given by n^2 - n,
where n is the number of pins used (here,  4^2 - 3 = 16 - 3 = 13 LEDs using only n = 4 pins).
*/

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                                    General CharliePlexing settings                                    */
int pinCP1 =  4;                                  // CharliePlexing LED pin 1
int pinCP2 =  5;                                  // CharliePlexing LED pin 2
int pinCP3 =  6;                                  // CharliePlexing LED pin 3
int pinCP4 =  7;                                  // CharliePlexing LED pin 4

int nModes = 12;                                  // Number of mode LEDs (max = 13)

int Opening_delay  = 50;                          // Delay between LED during the powering up sequence 
int Mode_delay     = 500;                         // Delay between two button pushes to avoid multi-pushes


// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                                     Define CharliePlexing Matrix                                      */
#define PIN_CONFIG 0
#define PIN_STATE 1
#define LED_Num 12

int matrix[LED_Num][2][4] = {
/*             PIN_CONFIG                       PIN_STATE
        1       2       3       4          1     2     3     4     */
  { { OUTPUT, OUTPUT, INPUT,  INPUT  }, { HIGH, LOW,  LOW,  LOW  } },  // mode LED 1
  { { OUTPUT, OUTPUT, INPUT,  INPUT  }, { LOW,  HIGH, LOW,  LOW  } },  // mode LED 2 
  { { INPUT,  OUTPUT, OUTPUT, INPUT  }, { LOW,  HIGH, LOW,  LOW  } },  // mode LED 3
  { { INPUT,  OUTPUT, OUTPUT, INPUT  }, { LOW,  LOW,  HIGH, LOW  } },  // mode LED 4 
  { { INPUT,  INPUT,  OUTPUT, OUTPUT }, { LOW,  LOW,  HIGH, LOW  } },  // mode LED 5
  { { INPUT,  INPUT,  OUTPUT, OUTPUT }, { LOW,  LOW,  LOW,  HIGH } },  // mode LED 6 
  { { OUTPUT, INPUT,  OUTPUT, INPUT  }, { HIGH, LOW,  LOW,  LOW  } },  // mode LED 7 
  { { OUTPUT, INPUT,  OUTPUT, INPUT  }, { LOW,  LOW,  HIGH, LOW  } },  // mode LED 8 
  { { INPUT,  OUTPUT, INPUT,  OUTPUT }, { LOW,  HIGH, LOW,  LOW  } },  // mode LED 9 
  { { INPUT,  OUTPUT, INPUT,  OUTPUT }, { LOW,  LOW,  LOW,  HIGH } },  // mode LED 10 
  { { OUTPUT, INPUT,  INPUT,  OUTPUT }, { HIGH, LOW,  LOW,  LOW  } },  // mode LED 11
  { { OUTPUT, INPUT,  INPUT,  OUTPUT }, { LOW,  LOW,  LOW,  HIGH } }   // mode LED 12 

};


// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                    Fucntion that turns on single declared LED and turns off others                    */
void lightOn( int led ) {
  DIO.pinMode( pinCP1, matrix[led][PIN_CONFIG][0] );       // Set CP pin 1 mode for the declared LED
  DIO.pinMode( pinCP2, matrix[led][PIN_CONFIG][1] );       // Set CP pin 2 mode for the declared LED
  DIO.pinMode( pinCP3, matrix[led][PIN_CONFIG][2] );       // Set CP pin 3 mode for the declared LED
  DIO.pinMode( pinCP4, matrix[led][PIN_CONFIG][3] );       // Set CP pin 4 mode for the declared LED
  
  DIO.write( pinCP1, matrix[led][PIN_STATE][0] );   // Set CP pin 1 state for the declared LED
  DIO.write( pinCP2, matrix[led][PIN_STATE][1] );   // Set CP pin 2 state for the declared LED
  DIO.write( pinCP3, matrix[led][PIN_STATE][2] );   // Set CP pin 3 state for the declared LED
  DIO.write( pinCP4, matrix[led][PIN_STATE][3] );   // Set CP pin 4 state for the declared LED
}


// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                     Fucntion that lights up all LEDs in sequence while powering up                    */
void Mode_opening() {
  for( int l = 0; l < nModes; l++ ) {                  // For each LED within the number of total LEDs,
    lightOn( l );                                        // Turn on declared LED while turning off the others
    delay(Opening_delay);                                // Wait for a moment before proceeding to the next one
  }
  
  DIO.pinMode(pinCP1,INPUT);                               // Turn all mode LEDs off
  DIO.pinMode(pinCP2,INPUT);                               // Turn all mode LEDs off
  DIO.pinMode(pinCP3,INPUT);                               // Turn all mode LEDs off
  DIO.pinMode(pinCP4,INPUT);                               // Turn all mode LEDs off
  delay(Mode_delay);                                   // Wait the "time of a push"
  lightOn(0);                                          // Turn on the first mode LEDs
}

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                                   Fucntion that turns off all LEDs                                    */
void lightOff() {
  DIO.pinMode(pinCP1,INPUT);                               // Turn all mode LEDs off
  DIO.pinMode(pinCP2,INPUT);                               // Turn all mode LEDs off
  DIO.pinMode(pinCP3,INPUT);                               // Turn all mode LEDs off
  DIO.pinMode(pinCP4,INPUT);                               // Turn all mode LEDs off
}
