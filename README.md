<p align="left"><img width="270" height="170" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/SpikyLogo.png">

<h1 align="center"> Spikeling V 2.2</h1></p>
<h3 align="center">  A hardware implementation of spiking neurons for neuroscience teaching and outreach</h3></p>
<p align="center"><h6 align="right">developed by M.J.Y. Zimmermann, A.M. Chagas & T. Baden</h6></p>

<br>

<div>



![](https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/GUI/PyQt/resources/spike.gif)


This project is licensed under the [GNU General Public License v3.0](https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/LICENSE)<br>
The hardware is licensed under the [CERN OHL v1.2](https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/PCB%20-%202.2c/LICENSE)

</div>

***

<div>

<p style='text-align: justify;'>
Understanding how neurons encode and compute information is fundamental to our study of the brain, but opportunities for hands-on experience with neurophysiological techniques on living neurons are scarce in science education.

<p style='text-align: justify;'>
Due to budgetary constraints and logistical hurdles, few students can be afforded the opportunity to experience electrophysiological recordings on living neurons in action. Yet, a fundamental aspect of neuroscience courses is to understand electrical signalling within neurons and the transmission of signals across synapses, as well as the experimental techniques necessary to observe these properties.

<p style='text-align: justify;'>
To support university-level neuroscience teaching, we designed ‘Spikeling’, an open-source teaching support device that mimics the electrical properties of spiking neurons by running the computationally efficient yet versatile Izhikevich model.

<p style='text-align: justify;'>
It is an artificial neuron that can receive different inputs, integrate them and send and outputs its computation, just like a spiking neuron would!

<p style='text-align: justify;'>
Technically, it consists on a microcontroller (an ESP32) running the computationally efficient Izhikevich model of a spiking neuron.

</div>

<br>

<div><p>
<img align="left" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/PCB.png" width=400">

<img align="left"  src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/Spikeling_cover.png" width="400">
</p></div>

<br>

<h6 align="center">Left: Rendering of spikeling electronic components. Right: Acrylic cover detailing spikeling functionalities.</h6>



<br>

***

</br>


<div>

<p style='text-align: justify;'>
The spikeling project emerged from local needs to teach neuroscience class modules for direct interaction with neuron physiology, data analysis, fluorescence imaging, protocol design, etc. The aim is to provide hands-on experience on how neurons encode information and how diverse variables modulates their activities, while engaging students with crucial aspects of data collection, experimental limitations, methodology and statistical analysis.

<p style='text-align: justify;'>
In order to give users a full interactive experience with the Spikeling neuron, a drawing engraved on the cover details in a neuro-morphic fashion all device functionalities. Futhermore, a spike-triggered LED and buzzer have been added to the device.

<p style='text-align: justify;'>
A dedicated GUI (Graphical User Interface) allows users to fully interact with Spikeling, plot all data generated and record them for further analysis.

<p style='text-align: justify;'>
Overall, Spikeling is a versatile device, allowing any teaching staff to conceive dry-lab tutorials or home assignments related to their own teaching course materials.

<p style='text-align: justify;'>
Enthusiasts and potential collaborators can source the electronic bits for this project from <a href="https://kitspace.org/boards/github.com/maxzimmer/spikeling-v2/">KitSpace</a></p>


</div>

***

<div>

<h3 align="left"> Neurophysiology:</h3></p>

<p style='text-align: justify;'>
Spikeling is conceived on the Izhikevich model, which “reproduces spiking and bursting behaviour of known type of cortical neurons. The model combines the biologically plausibility of Hodgkin-Huxley-type dynamics and the computational efficiency of integrate-and-fire neurons” (E.M. Izhikevich, IEEE Transactions on Neural Networks, 2003, doi: 10.1109/TNN.2003.820440).

<p style='text-align: justify;'>
Students can appreciate playing with many variables that can be encountered in textbook or related to class material. A simulated patch-clamp experiment (represented by a pipette drawing on the top cover) allows students to “inject current” into the Spikeling neuron. They can furthermore modulate the amount of current injected, the speed and duration at which it is injected and observe the adaptation effect on a spiking neuron.

<p style='text-align: justify;'>
Spikeling also possesses a photodiode (modelized on the top cover as a photoreceptor) making Spikeling photo-sensitive. The photodiode mimics current inputs a photoreceptor would have on a spiking neuron. Students can appreciate the impact of a flash light onto the photoreceptor and investigate the different effects it may have. Ultimately, a supplied LED can be connected to the stimulus port and can then be controlled in frequency and intensity for controlled experiments. Advanced variable such as photoreceptor decay and recovery rate could also be investigated.

<p style='text-align: justify;'>
Each Spikeling unit possesses one “axonal” output and two “dendritic” inputs. Each dendritic input possesses a knob that can modulate the synaptic gain positively or negatively (mimicking excitatory and inhibitory synapses). In advanced stages, students could be encouraged to form neuronal networks. Auxiliary neurons can furthermore be stimulated synchronously from the “main neuron” experiment box to set a controlled environment.

<img align="left"  src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/Spikeling_hardware.png">

<img align="right" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/101_graph.jpg">

<h6 align="center">Left: A Spikeling unit being stimulated by a direct current injection (blue cable) while receiving synaptic inputs from a second unit (pink cable). Right: Spikeling GUI displaying the unit membrane voltage (red trace) while being light-stimulated by a controlled LED (blue trace) which generates input current (green trace).</h6>

</div>

***

<div>

<h3 align="left"> Data Analysis</h3></p>

<p style='text-align: justify;'>
Handling large dataset is an important part of daily academic work. However, few universities offer coding and programming modules for their neuroscience courses. A proper data analysis of any kind starts with the understanding of a program language and the understanding of every steps of the analysis pipeline. Only then, students can appreciate the results of their experiments and engage in their critical interpretation.

<p style='text-align: justify;'>
Any data generated by Spikeling can be saved and exported.  The GUI comes with a simple built-in data analysis that allows students to check their data and generate raster plots. From this simple analysis they could appreciate how neuronal information is encoded within stochastic spike trains (see below).

<p style='text-align: justify;'>
This simple analysis could be used for home assignments in the early stages of student degree before engaging them in developing their own analysis code.

<p style='text-align: justify;'>
For advanced data analysis and basic statistics, python notebooks are provided to serve as template for the teaching staff. It is our hope to create a Spikeling community where users could share courses, exercises and data analysis scripts to be widely used in neuroscience and coding courses.

<img align="center" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/103_data%20analysis.jpg">

<h6 align="center">GUI displaying the “Neuron Generator” page where users can appreciate the model underlying Spikeling activity and from which they can generate unique neuron to further run on Spikeling.</h6>

</div>

***

<div>

<h3 align="left">Stimulus generator:</h3>

<p style='text-align: justify;'>
Spikeling comes by default with a repeated square wave pattern stimulus, on which the user could only modulate the intensity and the frequency, might it be for direct current injection or light stimulation.

<p style='text-align: justify;'>
Here users are encouraged to develop their own stimulus (successive waves, sinusoidal loops, chirp, binary noise, etc.). Some basic stimuli are already available. The main point of this feature is to encourage the students to conceive their own experiments leading them to think about the protocol that needs to be implemented in order to answer the experimental questions they are being faced with.

<img align="left"  src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/401_steps.jpg">

<img align="right" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/401_sine.jpg">

<h6 align="center">GUI displaying the “Simulus Generator” page where users can generate their own unique stimuli. The left screen shows repetitive increments of current, as seen in classic electrophysiology experiments (10 steps with 10 a.u. current increment lasting 25 ms with a resting period of 5ms at 0 a.u. current). The right screen shows a sine wave stimulus (50 a.u. amplitude, 20 Hz frequency over a period of 250 ms and a resting period of 100 ms at 0 a.u. current)</h6>

</div>

***

<div>

<h3 align="left">Exercises:</h3>

<p style='text-align: justify;'>
Spikeling comes with a set of suggested exercises that could be used in class as a guideline for the teaching staff to explore Spikeling functionalities. They are conceived to allow students to make a concrete connection between neurophysiology concepts seen in lectures with a responsive in silico model.

<p style='text-align: justify;'>
Exercises are also a mean to introduce some epistemology into the teaching material: Understanding how a neurobiology concept became a knowledge and how it can be tested, confirmed or refuted.
In advance courses, giving students the opportunity to design their own experiment as assignment also allows to introduce good methodology and protocol design practices. Which, unfortunately has shown to be too often mistaken with methods.

<p style='text-align: justify;'>
We would always encourage teachers to develop their own exercises based on the content they cover in class. It is our hope that such exercises could also be used as homework grading system.

</div>

***

<div>

<h3 align="left">Fluorescence imaging simulation:</h3>

<p style='text-align: justify;'>
Since Spikeling generates membrane voltage data, we could use this “ground truth data” to generate a simulated calcium concentration transient underlying spike occurrence in the neuron. And from then, use the later to model a simulated fluorescence.

<p style='text-align: justify;'>
Students could then be engaged into dynamic calcium fluorescence imaging (i.e two-photon microscopy) and play with many variables that could be encountered from the experimenter side (frame rate, laser power, photo detector gain, etc.), from the calcium concentration properties within the neuron (concentration baseline, decay, increase jump per spike, etc.)  or from the calcium indicator properties itself (indicator affinity, dissociation constant, brightness, photo-bleach, etc.).

<p style='text-align: justify;'>
For an even more realistic simulation, students could choose to move from a linear model to a non-linear saturation model of the fluorescence signal.

<img align="left"  src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/201_graph.png">

<img align="right" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/201_graphsat.png">

<h6 align="center">GUI displaying linear(left) and (non-linear) models of simulated fluorescence (green) based on simulated calcium concentration (pink)</h6>

<p style='text-align: justify;'>
Here, the aim is to familiarise students with the type of data they could encounter in their future academic work, incorporating noise and limitations to the data that are inherent to every experiments.

<p style='text-align: justify;'>
Ultimately, students could be encouraged to analyse imaging data, even implement spike inference algorithms and compare their results to the “ground truth data” that generated the fluorescence trace.


</div>

<div>
<p style='text-align: justify;'>
<img align="left" width="450" height="250" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/PCB.png">

<p style='text-align: justify;'>
The main upgrade on the PCB concerns the use of an ESP32 module and 2 ADC 8bit expander chips that together allow spikeling to compute more input output with specific input/output ports and dedicated potentiometer. The previous version had limited ports and potentiometers and different functions had to be encoded on the arduino code hence impacting the versatility of the model.

Stereo (3-ways) audio jacks 3.5mm replace the previous BNC cable. Both ports and cables are therefore cheaper, also ports are less bulky and cables more flexible. Moreover, now one single port can carry two distinct information. In this case digital and analog input/output.

Since the user cannot access the microcontroler board anymore (acrylic sheet on top of the board), a reset button has been added to the back of the board.

Previously, "modes" were encoded manually on the microcontroler, and the user could check the set mode number by the amount of flashes the microcontroller built-in LED was providing at the begining of the routine.
Now, the microcontroller is pre-set with 12 distinct "neuron modes" that the user can switch through, 12 proxy LED indicate continuously which mode is currently being set.

The buzzer is now smaller and is powered by the ESP32 3.3V (instead of the 5v from the arduino), making its clicking noise quieter, which is more pleasant for the user ear, especially after a couple of minutes using the device.

A couple of functions have been added to the board and can now be controlled through potentiometers (synaptic polarity(inhibitory/excitatory), photoreceptor gain and polarity, stimulus strength and polarity(only for current input not LED stimulation)).

Another major upgrade concerns the use of the two DAC GPIO from the ESP32. These two are conencted to the synapse out analog, which can be read either by another Spikeling synaptic in analog input port, or either by an external oscilloscope. The other DAC port is connected to the stimulus analog out, whcich drives the Current-in port (from the patch clamp module), therefore improving the direct stimulation from the board.

</p>
</div>

***

<div>
<img align="left" width="450" height="250" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/Spikeling_front.png">
<p style='text-align: justify;'>

The entire layout of the Spikeling board has been reconceived and a laser-cut acrylic sheet repesenting a neuron now sit on top of the board. All ports and potentiometers are now strategically placed.

The ESP32 is placed below the soma, the synaptic inputs from other Spikeling units are placed on the left, the synaptic output is placed on the right. Along the axon now sits a RGB LED, the red LED brightness follows as before the Vm status of the neuron, and the LED sparks in white when the neuron spike. The spike buzzer also sit along the axon, a small hole on the acrylic sheet sitting just above so the click can be heard coming from that direction.

The Vm potentiometer and the Current-in port are now grouped together and sit on the acrylic sheet at the bottom of an electrode pipette. They can now be considered as a voltage clamp experiment variables.

A photoreceptor is now drawn on the acrylic sheet, below the opsin sits a photodiode, and a potentiometer on the photoreceptor body now controls the photoreceptor sensitivity and its polarity (the user decides then if the PR has an excitatory or an inhibitory effect on the neuron)

The noise potentiometer now sits in a box by itself as it represents parasitic noise from the experiment environment and is independent from the rest of the Spikeling functions. This potentiometer is different from the others as it is not center-detented as it generates noise from a zero to a maximum value.

Next is the Neuron mode box which contains the 12 available modes to the users and a push button that allows the user to switch between them.

Finally, the last box contains all experimental tools allowing stimuli generation. As detailled on the acrylic sheet, the user can control the stimulus frequency and the stimulus strenght, along with its polarity. The stimulus output can either be directly connected to the current in port to simulate a current applied to a voltage held neuron through the pipette. Or be connected to a cable with a 5mm LED soldered at its tip which can be placed directly on top of the photoreceptor opsin (photodiode below). The photoreceptor possesses functions (decay/recovery) simulating how a real photoreceptor would integrate a light stimuli and how it will adapt to prolonged stimulation.  

</p>
</div>


***

<div>
<img align="left" width="450" height="250" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/GUI_main_screen.png">
<p style='text-align: justify;'>

Spikeling now possesses its own GUI, written in python and using the latest pyQt6 library. The script then uses pyInstall so it can be translated into a desktop app, ready to be easily distributed to users.

The GUI is divided (for the moment) into distinct tabs. The first one is the main GUI window where the user connects the board to the computer, can choose to either select the neuron mode on the board directly or through the GUI (note that custom modes will have to be selected from here, and in this instance the GUI takes priority over the board commands).

The main window display the Spikeling activity (Neuron Vm, total current input from all sources & stimulus state). If connected to other spikeling, the GUI can display fore both synaptic input, their incoming neuron Vm and their spiking event, which will be translated into input current for the main neuron. Traces can be selected through checkbox and superimposed over the same graph with a common timeline.

Below the main window, Spikeling traces can be recorded either live or for only a fixed amount of stimulation loop.

On the right hand side two control columns can be found. For all commands, when the checkbox is clicked, the GUI takes over the potentiometer and controls directly the Spikeling variable. This allow advanced user to finely design an experimental protocol for example.

Below the stimulus frequency and strength sliders can be found a custom stimulus display. Here the user can choose to use instead of the classical square wave, either a stimulus from a pre-design library (comprising sine wave, chirp, white noise, etc.), or either a custom made stimulus generated from the GUI "stimulus generator" tab.

One the first Spikeling version, if the user wanted to change the set variable for the photoreceptor and synaptic set variable (gain, decay, recovery, polarity, etc.), one had to manually reupload the arduino code with these changes, and no proper experimental protocol could be establish. Here by clicking the checkbox, the user had the opportunity to change these value directly and therefore is able to play further with each Spikeling parameter, opening the way for teacher to come up with their own personal exercises.


</p>
</div>

***

<div>
<img align="left" width="450" height="250" src="https://github.com/MaxZimmer/Spikeling-V2/blob/main/Images/GUI_neuron_screen.png">
<p style='text-align: justify;'>

In this tab, the user can play directly with the Izhikevich model. A short text from Izhikevich publications explain the role of each variable (later upgrade will include hyperlink to these publication along with pop up window detailing further what the code is actually doing).

The main window computes the code with a current input of +15 (as in Izhikevich publication). User can change the 4 variable of the code and display the resulting "neuron mode". This is also where user can come up with its own neuronal modes to experiment on if the 12 pre-set one are not enough. This is also where teachers can generate their own custom made neuron, save them, and impose them as experimental model for i.e. homework exercises.

</p>
</div>

***

Stimulus generator and data analysis tabs needs to be finished (cf. development log) but they will include ... a stimulus generator, allowing the user to come up with custom made stimulation loop, and ... a data analysis routine for early computation course where student could upload their recorded traces and extract information from it, generating raster plot, computing data and generate basic statistics. For advanced courses an integrated python exercise manual (no IGOR !!!) will guide students through creating a data analysis pipeline using .csv files saved from the main window.

<br>
<div>


## Dependencies:

### Arduino:
 - https://github.com/erropix/ESP32_AnalogWrite (can be installed via the Arduino library manager. Look for ESP32 analogwrite library by erropix)

### GUI:
 - pyQt6



# Development log

### Working Issues

##### Arduino

The negative photogain does not decay towards zero, an absolute value has to be implemented


##### GUI

- Serial reading is slow and pyQtgraph does not update fast enough the serial values.

>FIXED: The entire code was reimplement using a lower BaudRate (9600 instead of 115200) and the pyQtgraph routine was improved.
Currently the GUI functions are being reimplemented with the PySerial readWrite functions. Updates to come.

##### PCB

- The audio jack footprint is not correct. the back pin and holes are mm ahead of their correct position.

>FIXED: the new PCB in the 2.2c version now posses the correct footprint. Previous version will need to cut the plastic pieces in front of the audio jack female and force the component into position

- The LEDs on the board might be to Bright

> The resistance of the 4 CharliePlex and the SpikeLed resistors must be adjusted to the acrylic material chosen for the front cover. The current 100 Ohm is sufficient for opaque PMMA, but clear transparent ones should have 1 kOhm soldered below so that the LEDs do not affect the user vision.

- The CharliePlex footprint orientation (+/-) is not labeled

- Stimulus generation tab to be reimplemented

- Data Analysis tab to be reimplemented

- About tab to be created

##### Acrylic sheet

The custom 1, 2, 3 text has to be changed to the last three neuron mode implemented on the arduino code

> FIXED

</div>



***


Cost estimation spreadsheet for production
https://docs.google.com/spreadsheets/d/1JO1rpfb5DoqT5x59RL3RnkQFxRdzm5al6X8uEcsVFo8/edit#gid=0
