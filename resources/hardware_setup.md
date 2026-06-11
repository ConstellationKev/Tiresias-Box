# Hardware Setup
If you haven't already, please set up the Rapsberry Pi 5 software and OS first before doing the hardware setup. This can be found in the software_setup file.
PLEASE REFER TO THIS WIRING DIAGRAM AS YOU PROCEED:
![](wiring%20diagram.jpg)
Also refer to the [BOM](Tiresias-Box/BOM/BOM.csv) which will contain everything you will need to assemble this project.

## Starting to Putting Everything Together (Leave Gears to the End)
1. First, print out the 3D file for the base of this box, as well as all of the other required 3D printed parts included.
2. Take your base and we will first start with the Raspberry Pi
3. Place your Raspberry Pi onto the 4 screw holes with the USB-C port facing away from the curvy wall.
4. Take your 4 long spacers and put them respectively onto the 4 holes on the Raspberry Pi.
5. Use M2.5 16mm screws to screw the Raspberry Pi and the 4 spacers from below the base.
6. Attach your Raspberry Pi Camera Module 3 to the camera mount, the one with holes facing horizontally, using M2.5 8mm screws and nuts on the back.
7. Connect your Raspberry Pi 5 FPC Camera Cable, with the wider end into the camera and the thinner end into the Pi's camera port, aka the closest MIPI connector.
8. Take the 3D printed upper mounting plate for the PCA9685 and place it on top of the four long spacers, making sure the opened up part is facing the curvy wall.
9. Make sure to tuck the camera's FPC cable nice and snug under the plate so that it doesn't block any of the header pins on the Raspberry Pi.
10. Attach the top plate on by screwing in M2.5 5mm screws into the spacers.

## Setting Up PCA9685
1. Take your PCA9685 board as well as the header pins and the terminal block that it comes with and place the smaller ends into their designated holes in the board.
2. Use your soldering kit and then solder the header pins and the terminal block onto the board.
3. Next, use M2 10mm screws and nuts to screw the PCA9685 into the upper mounting board.
4. Then, take your female to female jumper wires and plug them into the GROUND, SCL, SDA, and VCC header pins on the PCA9685.
5. Connect these to the corresponding header pins on the Raspberry Pi. The VCC wire should go to the 5V pin on the Raspberry Pi. Everything else goes to the same name.

Refer to these YouTube videos if you are confused, they helped me a ton: https://www.youtube.com/watch?v=-x2EEIUMm6A&t=274s and https://www.youtube.com/watch?v=GwpSpOwvx9Y

## Almost Done Putting Everything Together
1. Take your two servos and then mount them onto the two servo mounting areas on the other side of the wall. The servo wires should be facing outwards.
2. Screw in the servos with the M2 8mm screws that they come with.
3. Take the servo wires and then plug them into the servo pins on the PCA9685. Make sure the colors match up with black to black, orange to orange, so on. Plug the lower servo into the 0 port and plug the higher servo into the 3 port.

## External power supply
1. Take the 20AWG wires and then cut and strip them to however long you want them to be and then insert them into the terminal block onto the PCA9685.
2. Take the other end and insert it into the Female DC power adapter. You need to screw in the screws a bit to keep the wires in place for both.
3. MAKE SURE THE WIRES ARE CORRECTLY WIRED, positive goes to positive and negative goes to negative. Any mix up will potentially fry your entire project. Red is usually positive.
4. Plug in the black 5V power supply into a wall socket and the other end into the female DC power adapter.
5. Plug in the white USB-C power supply into a wall socket and the other end into the Raspberry Pi.

## Gears
1. Plug your Raspberry Pi into a monitory, since you need to run code.
2. Run hardware_setup.py and then make sure to not touch the servo splines or move them after the code is ran.
3. Place the inner orange CAM on the bottom first, onto the indent for it. Locate the small dot on the gear and make sure it faces away from the direction the camera is pointing.
4. Place the orange servo gear onto the lower servo's spline, making sure the gear lines up well with the CAM gear. Make sure not to move the CAM gear. Adjust the servo gear based on it. Try to make the rubbing between the top og the servo gear and the CAM as less as possible.
5. Then, place the white outer CAM on top of the orange CAM, with the dot facing in the same orientation. 
6. Place the white servo gear onto the higher servo's spline. Do the same as the other one.
7. Use the servo srews that they provided and screw the servo gears onto the servos.
8. No screws are needed for the CAMs, they are held in place by the servo gears as well as each other.
9. Unplug the two external power supplies from the PCA9685 and Raspberry Pi.

## Roof and Walls and Button
1. Although the gears should be in place fairly snug, try not to flip the box upside down or shake it violently. It is not meant to be shaken.
2. Now that the base and everything else is set up, screw in the walls first using M2.5 10mm screws. The holes should line up with the ports on the Rapsberry Pi / the camera hole.
3. Take your roof and then wire the button wires through the button hole on the top.
4. Take your button wires and plug the button into the Raspberry Pi, one into a ground pin and the other in GPIO pin 5.
5. Hot glue your button onto the roof, or you can use any other type of binding method, or just leave it. The box isnt supposed to be moved around anyways and the mount for the button should be very snug such that it will be decently stuck in there.
6. Screw in the roof using M2.5 10mm screws.
7. Finally, place the 6 braille pins into the 6 holes on the top of the roof. Do not push them in, simply let them drop in.

You are done! Make sure to keep the box mostly upright when using to keep the pins from falling out (which is unlikely but only if you turn it fully upside down).
