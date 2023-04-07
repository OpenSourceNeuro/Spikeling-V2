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

<div>
<img align="center" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/PCB.png" width="400" height="250" >

<img align="center"  src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/Spikeling_cover.png" width="400" height="250">

<h6 align="center">Left: Rendering of spikeling electronic components. Right: Acrylic cover detailing spikeling functionalities.</h6>

</div>

<div>

<p style='text-align: justify;'>
The spikeling project emerged from local needs to teach neuroscience class modules for direct interaction with neuron physiology, data analysis, fluorescence imaging, protocol design, etc. The aim is to provide hands-on experience on how neurons encode information and how diverse variables modulates their activities, while engaging students with crucial aspects of data collection, experimental limitations, methodology and statistical analysis.

<p style='text-align: justify;'>
In order to give users a full interactive experience with the Spikeling neuron, a drawing engraved on the cover details in a neuro-morphic fashion all device functionalities. Furthermore, a spike-triggered LED and buzzer have been added to the device.

<p style='text-align: justify;'>
A dedicated GUI (Graphical User Interface) allows users to fully interact with Spikeling, plot all data generated and record them for further analysis.

<p style='text-align: justify;'>
Overall, Spikeling is a versatile device, allowing any teaching staff to conceive dry-lab tutorials or home assignments related to their own teaching course materials.

<p style='text-align: justify;'>
Enthusiasts and potential collaborators can source the electronic bits for this project from <a href="https://kitspace.org/boards/github.com/maxzimmer/spikeling-v2/">KitSpace</a></p>


</div>

***

<h3 align="left">Detailed Spikeling functions</h3></p>

- [Spikeling A spiking neuron interface](#Spikeling-A-spiking-neuron-interface)
- [Spikeling GUI - neuron parameters](#Spikeling-GUI-neuron-parameters)
- [Spikeling GUI - stimuli parameters](#Spikeling-GUI-stimuli-parameters)
- [Spikeling Data Analysis](#Spikeling-Data-Analysis)
- [Spikeling Neuron generator](#Spikeling-Neuron-generator)
- [Spikeling Stimulus Generator](#Spikeling-Stimulus-Generator)
- [Spikeling Multiple recording](#Spikeling-Multiple-recording)

- [Fluorescence imaging simulation](#Fluorescence-Imaging-simulation)
- [Fluorescenc: Imaging parameters](#Fluorescence-Imaging-parameters)
- [Fluorescence Calcium parameters](#Fluorescence-Calcium-parameters)
- [Fluorescence Fluorescence parameters](#Fluorescence-Imaging-parameters)
- [Fluorescence Data Analysis](#Fluorescence-Data-Analysis)
- [Fluorescence Multiple fluorescence](#Fluorescence-Multiple-fluorescence)

- [Exercices GUI](#Exercices-GUI)
- [Exercices Python](#Exercices-Python)

- [GitHub Contributions](#GitHub-Contributions)


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

</div>

<br>

<div>

<img align="center"  src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/Spikeling_hardware.png" width="400" height="250">

<img align="center" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/101_graph.png" width="400" height="250">

<h6 align="center">Left: A Spikeling unit being stimulated by a direct current injection (blue cable) while receiving synaptic inputs from a second unit (pink cable). Right: Spikeling GUI displaying the unit membrane voltage (red trace) while being light-stimulated by a controlled LED (blue trace) which generates input current (green trace).</h6>

</div>

***

<div>

<h3 align="left"> Data analysis</h3></p>

<p style='text-align: justify;'>
Handling large dataset is an important part of daily academic work. However, few universities offer coding and programming modules for their neuroscience courses. A proper data analysis of any kind starts with the understanding of a program language and the understanding of every steps of the analysis pipeline. Only then, students can appreciate the results of their experiments and engage in their critical interpretation.

<p style='text-align: justify;'>
Any data generated by Spikeling can be saved and exported.  The GUI comes with a simple built-in data analysis that allows students to check their data and generate raster plots. From this simple analysis they could appreciate how neuronal information is encoded within stochastic spike trains (see below).

<p style='text-align: justify;'>
This simple analysis could be used for home assignments in the early stages of student degree before engaging them in developing their own analysis code.

<p style='text-align: justify;'>
For advanced data analysis and basic statistics, python notebooks are provided to serve as template for the teaching staff. It is our hope to create a Spikeling community where users could share courses, exercises and data analysis scripts to be widely used in neuroscience and coding courses.

</div>

<br>

<div>

<img align="center" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/103_dataanalysis.jpg" width="400" height="250">

<img align="center" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/103_data%20analysis.jpg" width="400" height="250">

<h6 align="center">GUI displaying the “Neuron Generator” page where users can appreciate the model underlying Spikeling activity and from which they can generate unique neuron to further run on Spikeling.</h6>

</div>

***

<div>

<h3 align="left">Stimulus generator:</h3>

<p style='text-align: justify;'>
Spikeling comes by default with a repeated square wave pattern stimulus, on which the user could only modulate the intensity and the frequency, might it be for direct current injection or light stimulation.

<p style='text-align: justify;'>
Here users are encouraged to develop their own stimulus (successive waves, sinusoidal loops, chirp, binary noise, etc.). Some basic stimuli are already available. The main point of this feature is to encourage the students to conceive their own experiments leading them to think about the protocol that needs to be implemented in order to answer the experimental questions they are being faced with.

</div>

<br>

<div>

<img align="center"  src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/401_steps.jpg" width="400" height="250">

<img align="center" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/401_sine.jpg" width="400" height="250">

<h6 align="center">GUI displaying the “Simulus Generator” page where users can generate their own unique stimuli. The left screen shows repetitive increments of current, as seen in classic electrophysiology experiments (10 steps with 10 a.u. current increment lasting 25 ms with a resting period of 5ms at 0 a.u. current). The right screen shows a sine wave stimulus (50 a.u. amplitude, 20 Hz frequency over a period of 250 ms and a resting period of 100 ms at 0 a.u. current)</h6>

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

</div>

<br>

<div>

<img align="center"  src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/201_graph.png" width="400" height="250">

<img align="center" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/201_graphsat.png" width="400" height="250">

<h6 align="center">GUI displaying linear(left) and (non-linear) models of simulated fluorescence (green) based on simulated calcium concentration (pink)</h6>

</div>

<div>

<p style='text-align: justify;'>
Here, the aim is to familiarise students with the type of data they could encounter in their future academic work, incorporating noise and limitations to the data that are inherent to every experiments.

<p style='text-align: justify;'>
Ultimately, students could be encouraged to analyse imaging data, even implement spike inference algorithms and compare their results to the “ground truth data” that generated the fluorescence trace.

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
***

## Spikeling A spiking neuron interface

<div>

<img align="left"  src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/Spikeling_cover.png" width="400" height="250">

<p style='text-align: justify;'>
The entire layout of the Spikeling board has been reconceived and a laser-cut acrylic sheet repesenting a neuron now sits on top of the board. All ports and potentiometers are now strategically placed.

<p style='text-align: justify;'>
The ESP32 is placed below the soma, the synaptic inputs from other Spikeling units are placed on the left, the synaptic output is placed on the right. Along the axon now sits a RGB LED, the red LED brightness follows as before the Vm status of the neuron, and the LED sparks in white when the neuron spike. The spike buzzer also sit along the axon, a small hole on the acrylic sheet sitting just above so the click can be heard coming from that direction. Both indicators can now be disabled by users at their pleasure.

<p style='text-align: justify;'>
The Vm potentiometer and the Current-in port are now grouped together and sit on the acrylic sheet at the bottom of an electrode pipette. They can now be considered as patch clamp experiment variables.

<p style='text-align: justify;'>
A photoreceptor is now drawn on the acrylic sheet, below the opsin sits a photodiode, and a potentiometer on the photoreceptor body now controls the photoreceptor sensitivity and its polarity (users can thus decide if the photoreceptor has an excitatory or an inhibitory effect on the neuron)

<p style='text-align: justify;'>
The noise potentiometer now sits in a box by itself as it represents parasitic noise from the experiment environment(synaptic inputs, receptor noise, thermal noise, experimental setup, etc.) and is independent from the rest of the Spikeling functions. This potentiometer is different from the others: it is not center-detented as it generates noise from a zero to a maximum value.

<p style='text-align: justify;'>
Next is the Neuron mode box which contains the twelve available modes to the users and a push button that allows the user to switch between them.

<p style='text-align: justify;'>
Finally, the last box contains all experimental tools allowing stimuli generation. As detailed on the acrylic top cover, the user can control the stimulus frequency and the stimulus intensity, along with its polarity. The stimulus output can either be directly connected to the current-in port to simulate a current applied to a patched neuron through the pipette; or be connected to a cable with a 5mm LED soldered at its tip which can be placed directly on top of the photoreceptor opsin (photodiode below). The photoreceptor potentiometer allows to modulate the gain and polarity of the light-induced input current. Furthermore, the photoreceptor possesses functions (on the GUI: decay/recovery) simulating how a variety of photoreceptors would integrate a light stimuli and how it will adapt to prolonged stimulation.  

</div>

***

<p style='text-align: justify;'>
Spikeling now possesses its own GUI, written in python and using the latest pyQt6 library. The script then uses pyInstaller so it can be translated into a windows/linux/mac app, ready to be easily distributed to users.

<img align="left" width="400" height="250" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/101_graph.png">

<p style='text-align: justify;'>
The GUI is divided into distinct pages. The first one is the main GUI window where users connect the board to the computer. From there they can choose to either select the neuronal mode on the board directly (neuron mode box) or through the GUI (note that custom modes will have to be selected from here, and in this instance the GUI takes priority over the board commands).

<p style='text-align: justify;'>
The main window displays the Spikeling activity (Neuron Vm, total current input from all sources & stimulus ). If connected to other Spikelings, the GUI can display synaptic inputs: their incoming neuron Vm and their spiking events, which will be translated into input current for the main neuron. Traces can be selected through checkbox and superimposed over the same graph with a common timeline.

<p style='text-align: justify;'>
Below the main window, sits the recording window.

<p style='text-align: justify;'>
On the right hand side two control columns can be found. For all commands, when the toggle button is enabled, the GUI takes over the potentiometer and controls directly the Spikeling variables. This allows users to design an experimental protocol in a controlled fashion.

<p style='text-align: justify;'>
Below the stimulus frequency and strength sliders can be found a custom stimulus display. Here the user can choose to use instead of the classical square wave, either a stimulus from a pre-design library (comprising sine wave, chirp, white noise, etc.), or either a custom made stimulus generated from the GUI "stimulus generator" tab.

</div>

***

## Spikeling GUI neuron parameters

<div>

<img align="left" width="400" height="250" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/Neurogen.jpg">

<p style='text-align: justify;'>
In this tab, the user can play directly with the Izhikevich model. A short text from Izhikevich's publication explain the role of each variable.

<p style='text-align: justify;'>
The main window computes the Izhikevich model with a modifiable current input. Users can change the 4 variable of the code and display the resulting "neuron mode". This is also where users can come up with their own neuronal modes to experiment on. This is also where teachers can generate their own custo-made neuron, save them, and impose them as experimental model for, i.e. home assignements.

</div>

***

## Spikeling Stimulus Generator

<div>

Stimulus generator and data analysis tabs needs to be finished (cf. development log) but they will include ... a stimulus generator, allowing the user to come up with custom made stimulation loop, and ... a data analysis routine for early computation course where student could upload their recorded traces and extract information from it, generating raster plot, computing data and generate basic statistics. For advanced courses an integrated python exercise manual (no IGOR !!!) will guide students through creating a data analysis pipeline using .csv files saved from the main window.

<img align="center" width="400" height="250" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/401_steps.jpg">

<img align="center" width="400" height="250" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/401_sine.jpg">

<img align="center" width="400" height="250" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/401_triangle.jpg">

<img align="center" width="400" height="250" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/401_linchirp.jpg">

<img align="center" width="400" height="250" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/401_expchirp.jpg">

<img align="center" width="400" height="250" src="https://github.com/OpenSourceNeuro/Spikeling-V2/blob/main/Images/401_ampchirp.jpg">



</div>
