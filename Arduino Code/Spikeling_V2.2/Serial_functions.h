#include "General_settings.h"
#include "Mode_LEDS.h"
#include <SerialCommand.h>   // SerialCommand Library by Steven Cogswell https://github.com/shyd/Arduino-SerialCommand


SerialCommand SCmd;

void NeuronMode(){
  float aNumber;
  char *arg;
  
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atof(arg);
    a_Izhikevich = aNumber;
  }
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atof(arg);
    b_Izhikevich = aNumber;
  }
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atof(arg);
    c_Izhikevich = aNumber;
  }
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atof(arg);
    d_Izhikevich = aNumber;
  }
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atof(arg);
    Mode = aNumber;
    lightOn(Mode);
    if (Mode == 99){
      lightOff();
    }
  }
}


void StimFre_on(){
  StimFre_Flag = false;
  int aNumber;
  char *arg;
  arg = SCmd.next();
  if (arg != NULL){
    aNumber = atoi(arg);
    StimFre= aNumber;
  }
}
void StimFre_off(){
  StimFre_Flag = true;
}


void StimStr_on(){
  StimStr_Flag = false;
  char *arg;
  arg = SCmd.next();
  if (arg != NULL){
    StimStrD = atoi(arg);
    StimStrA = atoi(arg);
  }
}
void StimStr_off(){
  StimStr_Flag = true;
}


void StimCus_on(){
  StimCus_Flag = false;
  char *arg;
  arg = SCmd.next();
  if (arg != NULL){
    StimCus_val = atoi(arg);
  }
}
void StimCus_off(){
  StimCus_Flag = true;
}

void PDGain_on(){
  PDGain_Flag = false;
  char *arg;
  arg = SCmd.next();
  if (arg != NULL){
    PD_Amp = atoi(arg)/10+1;
  }
}
void PDGain_off(){
  PDGain_Flag = true;
}


void PDDecay_on(){
  PDDecay_Flag = false;
  char *arg;
  arg = SCmd.next();
  if (arg != NULL){
    PD_Decay = atof(arg);
  }
}
void PDDecay_off(){
  PDDecay_Flag = true;
}


void PDRecovery_on(){
  PDRecovery_Flag = false;
  char *arg;
  arg = SCmd.next();
  if (arg != NULL){
    PD_Recovery = atof(arg);
  }
}
void PDRecovery_off(){
  PDRecovery_Flag = true;
}


void IC_on(){
  IC_Flag = false;
  char *arg;
  arg = SCmd.next();
  if (arg != NULL){
    I_IC = atoi(arg);
  }
}
void IC_off(){
  IC_Flag = true;
}


void Noise_on(){
  Noise_Flag = false;
  char *arg;
  arg = SCmd.next();
  if (arg != NULL){
    Noise_Amp = atoi(arg);
  }
}
void Noise_off(){
  Noise_Flag = true;
}


void Syn1Gain_on(){
  Syn1Gain_Flag = false;
  char *arg;
  arg = SCmd.next();
  if (arg != NULL){
    Syn1_Amp = atoi(arg)/4;
  }
}
void Syn1Gain_off(){
  Syn1Gain_Flag = true;
}


void Syn1Decay_on(){
  Syn1Decay_Flag = false;
  char *arg;
  arg = SCmd.next();
  if (arg != NULL){
    Synapse1_decay = atoi(arg)/1000;
  }
}
void Syn1Decay_off(){
  Syn1Decay_Flag = true;
}


void Syn2Gain_on(){
  Syn2Gain_Flag = false;
  char *arg;
  arg = SCmd.next();
  if (arg != NULL){
    Syn2_Amp = atoi(arg)/4;
  }
}
void Syn2Gain_off(){
  Syn2Gain_Flag = true;
}


void Syn2Decay_on(){
  Syn2Decay_Flag = false;
  char *arg;
  arg = SCmd.next();
  if (arg != NULL){
    Synapse2_decay = atoi(arg)/1000;
  }
}
void Syn2Decay_off(){
  Syn2Decay_Flag = true;
}


void Buzzer_on(){
  Buzzer_Flag = true;
}

void Buzzer_off(){
  Buzzer_Flag = false;
  digitalWrite(pinSpike, LOW);
}


void LED_on(){
  LED_Flag = true;
}

void LED_off(){
  LED_Flag = false;
  digitalWrite(pinLEDSpike1,HIGH);
  digitalWrite(pinLEDSpike2,HIGH);
  analogWrite(pinLEDVm,0);
}
