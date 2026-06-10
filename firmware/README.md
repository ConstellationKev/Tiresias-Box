# Tuning Positions
A lot of this code requires to manually tune positions of the servos based on the braille pin positions and the gear positions. I have put everything that requires to be tuned as a value of 0 for now and they will be tuned when parts arrive for actual building.

Tuning only needs to be done once as the servo models will be the same for the project so other people building this project will have the same degrees of rotation. The hardware setup python file will set the servos to the inital positions so that each similar project to this will be set up the same way. So, this code and to-be-tuned postions will be able to be used for any project like this one.

Additionally, other things that also need to be tuned are the delay and timing thresholds for the servo movements