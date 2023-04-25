#include <analogWrite.h>
#include "Izhikevich_parameters.h"
#include "Serial_functions.h"


float v; // voltage in Izhikevich model
float u; // recovery variable in Izhikevich model

void setup() {
  HardwareSettings();
  Mode_opening(); 
  Izhikevich_opening();
  SCmd.addCommand("NEUR",NeuronMode);
  SCmd.addCommand("FR1",StimFre_on);
  SCmd.addCommand("FR0",StimFre_off);
  SCmd.addCommand("ST1",StimStr_on);
  SCmd.addCommand("ST0",StimStr_off);
  SCmd.addCommand("SC1",StimCus_on);
  SCmd.addCommand("SC0",StimCus_off);
  SCmd.addCommand("PG1",PDGain_on);
  SCmd.addCommand("PG0",PDGain_off);
  SCmd.addCommand("PD1",PDDecay_on);
  SCmd.addCommand("PD0",PDDecay_off);
  SCmd.addCommand("PR1",PDRecovery_on);
  SCmd.addCommand("PR0",PDRecovery_off);
  SCmd.addCommand("IC1",IC_on);
  SCmd.addCommand("IC0",IC_off);
  SCmd.addCommand("NO1",Noise_on);
  SCmd.addCommand("NO0",Noise_off);
  SCmd.addCommand("SG11",Syn1Gain_on);
  SCmd.addCommand("SG10",Syn1Gain_off);
  SCmd.addCommand("SD11",Syn1Decay_on);
  SCmd.addCommand("SD10",Syn1Decay_off);
  SCmd.addCommand("SG12",Syn2Gain_on);
  SCmd.addCommand("SG20",Syn2Gain_off);
  SCmd.addCommand("SD21",Syn2Decay_on);
  SCmd.addCommand("SD20",Syn2Decay_off);
  SCmd.addCommand("BZ1",Buzzer_on);
  SCmd.addCommand("BZ0",Buzzer_off);
  SCmd.addCommand("LED1",LED_on);
  SCmd.addCommand("LED0",LED_off);
}

void loop() {
  
  SCmd.readSerial();

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                                     Define Spikeling Mode                                             */
  ModeState = digitalRead(pinModeButton);         // Read the mode button state
  if (ModeState == HIGH){                         // If the mode button is pushed:
    Mode += 1;                                      // Increment the Mode by 1
    lightOn(Mode);                                  // Turn next Mode_LED
    a_Izhikevich = Array_a_Izhikevich[Mode];        // Change Izhikevich parameter a to the new mode
    b_Izhikevich = Array_b_Izhikevich[Mode];        // Change Izhikevich parameter b to the new mode
    c_Izhikevich = Array_c_Izhikevich[Mode];        // Change Izhikevich parameter c to the new mode
    d_Izhikevich = Array_d_Izhikevich[Mode];        // Change Izhikevich parameter d to the new mode

    if (Mode >= nModes){                          // If Mode has reached the maximum number of existing modes:
      Mode = 0;                                     // Reset Mode to 0
      lightOn(Mode);                                // Turn First Mode_LED
      a_Izhikevich = Array_a_Izhikevich[Mode];      // Change Izhikevich parameter a to the first mode
      b_Izhikevich = Array_b_Izhikevich[Mode];      // Change Izhikevich parameter b to the first mode
      c_Izhikevich = Array_c_Izhikevich[Mode];      // Change Izhikevich parameter c to the first mode
      d_Izhikevich = Array_d_Izhikevich[Mode];      // Change Izhikevich parameter d to the first mode
    }
    
    delay(Mode_delay);                            // Set a delay to prevent multi_push from the user
  }


// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                               Setting Voltage membrane clamp value                                    */
  if (IC_Flag == true){
    IC_value = ADC1.readADC(pinICPot) - bits/2;       // Reads IC potentiometer value and scales it to -2048 to 2048
    I_IC = IC_value / IC_PotScaling;                 // Generates "current" value from the reading and scales it from parameters
  }
  

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                                          Noise Generator                                              */
  if (Noise_Flag == true){
    Noise_Gain = ADC1.readADC(pinNoisePot);           // Reads Noise potentiometer value from 0 to 4095
    Noise_Amp = Noise_Gain / NoiseScaling;          // Generates current value from the reading and scales it from parameters
  }
  I_Noise = random( -Noise_Amp/2, Noise_Amp/2 );  // Generates random current value from the reading and scales it from parameters


// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*              Reading PhotoDiode value and setting PhotoDiode gain for generating input current        */
  PD_Value = ADC2.readADC(pinPD);                   // Reads Photodiode value from 0 to ~400
  
  if ( PD_counter < PD_avg ){                     // If, for this void loop, the PD counter has not reached the max count number:
    PD_counter +=1;                                 // Increment the counter by 1
  }
  else{                                           // If the PD counter has reached the max count number:
    PD_counter = 0;                                 // Reset the counter to 0
  }
  PD_Value_Array[PD_counter] = PD_Value;          // For this void loop, assign the current PD value to the PD_Value_Array at the current counter position
  PD_Value_Sum = 0;                               // Reset the previous PD_Value_Sum
  for ( int i = 0; i < PD_avg; i++){              // For all current PD_array values:
    PD_Value_Sum += PD_Value_Array[i];              // Sum up all values within the array...
  }
  PD_Value_Average = PD_Value_Sum / PD_avg;       // ... then average them

  if (PDGain_Flag == true){
    PD_PotValue = ADC1.readADC(pinPDPot) - bits/2; // Reads Photodiode Gain potentiometer value and scales it to -2048 to 2048
    PD_Amp = map(PD_PotValue, -bits/2, bits/2, -PD_PotRange, PD_PotRange)+1;
  }

  if (PD_Amp >= 0){
    PD_Polarity = 1;
  }
  if (PD_Amp < 0){
    PD_Polarity = -1;
  }
  
                   // Generates an amplification value from the reading and scales it from parameters 

  I_PD = (PD_Value_Average * PD_Amp / PD_Scaling) * PD_Gain;  // Finally, generates a current input from the photodiode readings, amplified byt the PD_Gain readings

  if (PDDecay_Flag == true){
    PD_Decay = 0.001;
  }

  if (PD_Gain > PD_gain_mini){                     // When PD_amp is above the minimum value:
    PD_Gain -= PD_Polarity * PD_Decay * I_PD;                      // Adapts proportionally to I_PD
    if (PD_Gain < PD_gain_mini){                     // If PD_amp becames lower than the minimum value:
      PD_Gain = PD_gain_mini;                          // Then PD_amp remains at the minimum value
    }
  }

  if (PDRecovery_Flag == true){
    PD_Recovery = 0.025;
  }

  if (PD_Gain < 1.0){
    PD_Gain +=  PD_Recovery;                        // Recovers by constant % per iteration
  }

     
// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                                             Synapse 1                                                 */
  SpikeIn1State = digitalRead(pinSyn1_D);         // Reads Synapse 1 digital input

  if (Syn1Gain_Flag == true){
    Syn1_Gain = ADC1.readADC(pinSyn1Pot) - bits/2 + Syn1_offset;    // Reads Synaptic Gain 1 potentiometer value and scales it to -2048 to 2048
    Syn1_Amp = Syn1_Gain / Syn1PotScaling;          // Generates current value from the reading and scales it from parameters
  }
  
  if (SpikeIn1State == HIGH){                     // If Spike is detected
    I_Synapse1 += Syn1_Amp;                         // Apply the synaptic current from Syn1 related to the synaptic gain 1
  }
  
  if (Syn1Decay_Flag == true){
    Synapse1_decay = 0.995;
  }
  
  I_Synapse1 *= Synapse1_decay;                   // Decay synaptic current towards zero

  Axon_AnalogInput1 = ADC2.readADC(pinSyn1_A);
  Syn1_Vm = mapfloat(Axon_AnalogInput1,0, bits11, Vm_min, Vm_peak) + Axon_AnalogOffset;
  

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                                             Synapse 2                                                 */
  SpikeIn2State = digitalRead(pinSyn2_D);         // Reads Synapse 2 digital input

  if (Syn2Gain_Flag == true){
    Syn2_Gain = ADC1.readADC(pinSyn2Pot) - bits/2 + Syn2_offset;    // Reads Synaptic Gain 2 potentiometer value and scales it to -2048 to 2048
    Syn2_Amp = Syn2_Gain / Syn2PotScaling ;          // Generates current value from the reading and scales it from parameters
  }

  if (SpikeIn2State == HIGH){                     // If Spike is detected
    I_Synapse2 += Syn2_Amp;                         // Apply the synaptic current from Syn2 related to the synaptic gain 2
  }

  if (Syn2Decay_Flag == true){
    Synapse2_decay = 0.990;
  }
  
  I_Synapse2 *= Synapse2_decay;                   // Decay synaptic current towards zero

  Axon_AnalogInput2 = ADC2.readADC(pinSyn2_A);
  Syn2_Vm = mapfloat(Axon_AnalogInput2,0, bits11, Vm_min, Vm_peak) + Axon_AnalogOffset;
  

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                                        Stimulus generator                                             */


  if ( StimStr_Flag == true && StimCus_Flag == true) {
    StimStr_Value = ADC1.readADC(pinStimStrPot);          // Reads Stimulus Strength potentiometer value
    StimStrD = map(StimStr_Value -bits/2, -bits/2, bits/2, -100 , 100);     // Map this value from 0 to 100 that will correspond to the stimulus strength %
    StimStrA = map(StimStr_Value, 0, bits, -100, 100);
  }

  if (StimCus_Flag == true){
    Stim_val_D = abs((StimStrD * StimLED_scaling + StimLED_offset));             // The stimulus digital output value is proportional to the potentiometer reading and scaled from parameters
    Stim_val_A = abs(StimStrA) * Stim_CurrentScaling;        // The stimulus analog output value is proportional to the potentiometer reading and scaled to parameters
  }
  
  if ( StimFre_Flag == true && StimCus_Flag == true) {
    StimFre_Value = ADC1.readADC(pinStimFrePot);          // Reads Stimulus Frequency potentiometer value
    StimFre = map(StimFre_Value, 0, bits, 100 , -100);  // Map this value from -100 to 100 
  }

  if (StimCus_Flag == true){
    if ( Stim_counter < Stim_steps/2 ){                // If the number of void loops has not reached half the stimulus duty cycle:
      analogWrite(pinStim_D, Stim_val_D);                 // Applies the stimulus digital output value to the stimulating LED
      dacWrite(pinStim_A, Stim_val_A);                    // Applies the stimulus analog output value to the Current in
      Stim_State = StimStrA;                              // Register stimulus ON
    }
    if ( Stim_counter > Stim_steps/2 ){                 // If number of void loops has exceeded half the stimulus duty cycle period:
      analogWrite(pinStim_D, 0);                          // Nothing is sent throught the digital output
      dacWrite(pinStim_A, 0);                             // Nothing is sent throught the analog output
      Stim_State = 0;                                     // Register stimulus OFF
    }

    Stim_counter += 1;                                  // Increment the void loop counter by 1
    if ( Stim_counter >= Stim_steps ){                  // If the void loop counter has reached the stimulus duty cycle period:
      Stim_counter = 0;                                   // Reset the void loop counter
      Stim_steps = round ( Stim_DutyCycle + ( (StimFre * Stim_DutyCycle) / 100 ) ) + Stim_minDutyCycle;  // Define the stimulus duty cycle period proportional to the stimulus frequency potentiometer value
    }
  }

  if (StimCus_Flag == false){
    if (StimCus_val > 0){
      Stim_val_D = (StimCus_val * StimLED_scaling + StimLED_offset);
    }
    if (StimCus_val <= 0){
      Stim_val_D = 0;  
    }
    
    StimStrA = StimCus_val;
    Stim_val_A = abs(StimStrA) * Stim_CurrentScaling;   
    
    analogWrite(pinStim_D, Stim_val_D);
    dacWrite(pinStim_A, Stim_val_A); 
    
    Stim_State = StimCus_val;
  }

  if (StimCus_Flag == true){
    CurrentIn_Value = ADC2.readADC(pinCurrentIn);         // Reads Current in value
    if ( StimStrA > StimStrA_mini){
      I_Stim = CurrentIn_Value * CurrentInScaling;        // Scales this value from parameters and determines Current In current
    }
    else if ( StimStrA < -StimStrA_mini){
      I_Stim = - CurrentIn_Value * CurrentInScaling;
    }
    else{
      I_Stim = CurrentIn_Value * I_Stim_mini; 
    }
  }

    if (StimCus_Flag == false){
    CurrentIn_Value = ADC2.readADC(pinCurrentIn);         // Reads Current in value
    if ( StimStrA >= 0){
      I_Stim = CurrentIn_Value * CurrentInScaling;        // Scales this value from parameters and determines Current In current
    }
    else if ( StimStrA < 0){
      I_Stim = - CurrentIn_Value * CurrentInScaling;
    }
  }
  
  
// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                      Spikeling computation running on Izhikevich mmodel                               */
  I_Total = I_IC + I_PD + I_Stim + I_Synapse1 + I_Synapse2 + I_Noise; // Sum up all input currents
  
  v = v + timestep_ms*(0.04 * sq(v) + 5*v + 140 - u + I_Total);   // Compute the voltage variable
  u = u + timestep_ms*(a_Izhikevich * (b_Izhikevich * v - u));    // Compute the recovery variable

  if (v >= Vm_peak){                                              // If the voltage value is above the peak (30mV by default):
    v = c_Izhikevich;                                               // The voltage variable corresponds to the "after spike reset value"
    u = u + d_Izhikevich;                                           // The recovery variable is incremented by the "after spike reset of recovery variable"
  }
  
  if (v <= Vm_min) {                                              // If voltage goes below the min voltage value (-90mV by default):
    v = Vm_min;                                                     // Keep the voltage at Vm_min : Prevent pinVm going into overdrive - but also means that it will flatline at Vm_min. 
    } 


// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // 
/*                                               Axon                                                    */
  spike = false;                                                 // Reset spike registration 

  if  (v >= Vm_spike) {                                          // If voltage goes above the spike value ( -30mV by default)
    if ( Buzzer_Flag == true ){
      digitalWrite(pinSpike, HIGH);                                  // Activate the spike buzzer
    }
    if ( LED_Flag == true ){
      digitalWrite(pinLEDSpike1,LOW);
      digitalWrite(pinLEDSpike2,LOW);
      digitalWrite(pinLEDVm,LOW);
    }
    spike = true;                                                  // Register the spike
  }  
  else {                                                         // Otherwise,
    digitalWrite(pinSpike, LOW);                                   // Keep buzzer silent
    if ( LED_Flag == true ){
      digitalWrite(pinLEDSpike1,HIGH);
      digitalWrite(pinLEDSpike2,HIGH);
      analogWrite(pinLEDVm,map(v, Vm_min, Vm_peak, 0 , bits9));
    }
  }    

 if (spike == true){                                           // If spike is registered
    digitalWrite(pinAxon_D, HIGH);                                 // Send digital output thourgh the Axon digital pin
  }
  else {                                                         // Otherwise,
    digitalWrite(pinAxon_D, LOW);                                  // Keep the digital pin in a LOW state
  }   

  Axon_AnalogOutput = map(v,Vm_min, Vm_peak, 0,bits8);
  dacWrite(pinAxon_A,Axon_AnalogOutput);


  Serial.print(v);            Serial.print(',');
  Serial.print(Stim_State);   Serial.print(',');
  Serial.print(I_Total);      Serial.print(',');
  Serial.print(Syn1_Vm);      Serial.print(',');
  Serial.print(I_Synapse1);   Serial.print(',');
  Serial.print(Syn2_Vm);      Serial.print(',');
  Serial.println(Synapse1_decay);  
  delay(6);
}
