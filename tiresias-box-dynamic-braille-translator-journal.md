# Tiresias' Box (Dynamic Braille Translator) — Journal Export

- Exported at: 2026-07-20T18:35:10Z
- Project ID: 2388
- Entries: 15

## Entry 1
- ID: 11321
- Author: kevinkunzhong
- Created At: 2026-06-03T05:54:26Z

### Content

Today I began my journey creating my dynamic braille translator. I used Onshape to design a single braille cell, which consists of 6 pegs that will eventually be controlled by a CAM to make them move up and down; each cell will be its own letter. In real life, I got out a ruler and figured out the approximate dimensions of each braille cell, which is about 15mm x 22mm. I created the outer casing and then the inside pins, since they need to be moving around in the casing.
![Screenshot 2026-06-02 220050.png](https://fallout.hackclub.com/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYxMDYsInB1ciI6ImJsb2JfaWQifX0=--a182191e49a3422bc15f294d3c78be94d5ef4a0f/Screenshot%202026-06-02%20220050.png)
This is a bit larger than conventional braille cells but it is still relatively small and also big enough so it will work well with a CAM. After creating temporary tolerances for the pegs as well as their design, with the bump on the top and part of it sticking downwards which will be in contact with the CAM.

![Screenshot 2026-06-02 222305.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYxMDcsInB1ciI6ImJsb2JfaWQifX0=--42786f58c6722cb557234e66211960fbdb5a0608/Screenshot 2026-06-02 222305.png)
I chose the pegs to take on this shape since the top is where the people will feel it, so a nice smooth bump will be great. I tapered the bottom down a little bit so that it will fit well with the CAM. The smaller the bottom is, the more intricate it can be with the CAM and thus have more positions to get to / more accurate. I also made the bottom rounded so when it does rotate with the CAM, it will be smoother.

![Screenshot 2026-06-02 223451.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYxMDgsInB1ciI6ImJsb2JfaWQifX0=--9962d4ad01aed241e6b5e2b6ac5c766fd75a3328/Screenshot 2026-06-02 223451.png)
I also figured out how to use the linear pattern tool, which I have never used before which is very cool and it allowed me to multiply one pin into 6 and fit them into my casing without having to re-cad the pins over and over again.

![Screenshot 2026-06-02 222620.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYxMTAsInB1ciI6ImJsb2JfaWQifX0=--91dfad881542a22158abb327b79236927f373e86/Screenshot 2026-06-02 222620.png)
After creating the casing and the pins, I started creating the rotating CAMs. I didn’t make the up and down pattern of the CAM yet but I created a general location of where it will be.

I overall goal is to achieve dynamic braille while using the LEAST amount of electronic possible. Of course, using a servo for EVERY SINGLE pin would be soooo excessive (and expensive). Therefore, I thought of using a rotating CAM which can be powered by one servo only, but can cause the pins to be in multiple orientations. This not only saves servos, but also allows the pins to rest on something stable, giving it the normal force it needs when people feel it from above. However, CAMs are annoying and you have to map it out very accurately for each orientation. To make things simpler for myself, I separated the rotation wheels into an inner and outer one to make the CAM patterns separate into two separate parts, so that it is easier (relatively). I haven’t thought of using two servos or still using one but a shifting mechanism to move from outer to inner CAMs.

This leads me to actually mapping out the CAM shape which took FOREVER. 

![Screenshot 2026-06-02 210157.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYxMTIsInB1ciI6ImJsb2JfaWQifX0=--4b38c0282d39984b4085e4f9bcdff0f0f5b63edc/Screenshot 2026-06-02 210157.png)
I first found an image of the braille alphabet online and then mapped out all of the patterns and groupings of dots in every single letter. I grouped the dots by pair; top, middle, and bottom. Firstly, I delt with the inner CAM and since theres only two pins, it was very easy. You can either have up up, down down, up down, or down up, which was absolutely no problem for the CAM.
The nightmare began with the outer CAM. I took a screenshot and put approximate positions the 4 pins may be located at and then spaced them out somewhat evenly. This way, I can figure out what positions I can use for my CAM. I also figured out that for the top two and bottom pins, there are only 9 different combinations. So all I needed to do was map out the 9 orientations onto the outer CAM. Easier said than done. 

![Screenshot 2026-06-02 215937.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjYxMTMsInB1ciI6ImJsb2JfaWQifX0=--9013cb352c79db7a2e53feb894c5cf83cd375489/Screenshot 2026-06-02 215937.png)
After about more than an hour of trial and error (yes that is how I figured out this CAM pattern) I finally decoded the positions the CAM needs to be at for the 9 orientations. It only took re-sizing the under portion of the pins to fit more positions and a pack of gushers.
So of course it was not blindly mapping. I tried my best to use as less circles as possible and reuse circles if I can. This is because I have very limited room and I cannot keep on shrinking the bottom side since it is already very small. For example, There are multiple cases where the bottom two are both down so I can just do down down and then instead of adding another pair, I just simply use a down from the previous one and add one down, saving one circle. I kept on doing this, and finally came up with this. I am genuinely so proud of myself for this, this was probably the most complicated CAM I’ve mapped despite it being only ups and downs. And this is where I stopped for today. 
TLDR: I did a rough CAD of my braille cells and mapped out the shape of my CAMs.

### Recording Links

- https://lookout.hackclub.com/api/media/2ff125fc-58fb-4db9-b666-54302c8e27e4/video.mp4

## Entry 2
- ID: 11553
- Author: kevinkunzhong
- Created At: 2026-06-04T06:28:12Z

### Content

Today I worked on actually designing the physical CAMs. Previously, I used an online whiteboard software to manually create the circles and map them out so I also did so in Onshape just for reference as well. This allowed me to better get a feel of where the pins would be touching the surface so that I can cad the actual CAM design a lot better with less uncertainties.
![Screenshot 2026-06-03 170242.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjY4NjAsInB1ciI6ImJsb2JfaWQifX0=--ac2123db29ee19950566a2085e62e121e2ebc9d5/Screenshot 2026-06-03 170242.png)

I started off with the outer ring, which is the harder one. I began by writing comments on each of the circles and labelling them so it would be easier for me to design which area should rise up and which should fall down. 
![Screenshot 2026-06-03 192849.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjY4NjEsInB1ciI6ImJsb2JfaWQifX0=--e83dcc3909d67515eaacd28977a1e067f2e71bb0/Screenshot 2026-06-03 192849.png)

Afterwards, since I could not directly sketch onto the cylinder’s outside, I had to calculate a long strip, visualizing the cylinder is laid flat. This way, I can cad the designs onto that and the use the Wrap tool to wrap the extrude around the cylinder.
![Screenshot 2026-06-03 192818.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjY4NjIsInB1ciI6ImJsb2JfaWQifX0=--52104e0f2aad3caa69719bf33d3af1c9d142db53/Screenshot 2026-06-03 192818.png)

However, this did not make it any easier. As you can see, there are so many dimensions labeled out (partly because I forgot I could pattern the sketches so I lwk just copied and pasted all of them). But it turned out great. I sectioned off each area/circle with its own construction rectangle and went to work. I used conic arcs to make smooth ramps and inclines for the pins to run on. I further smoothened it later with fillets. This way, there will be minimal effort for the pins to move along the CAM. After wrapping around, the CAM looked good and although wonky, it should do its job.
![Screenshot 2026-06-03 201849.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjY4NjMsInB1ciI6ImJsb2JfaWQifX0=--c9c4f8d10a4992d8fce92caa6b7f84e30d9f72e7/Screenshot 2026-06-03 201849.png)

I also made the ends of the pins thinner so that it can better fit into the CAM and not get stuck in it. Making it smaller also ensures only one point of contact at all times. Two points of contact will likely get the pins stuck and the CAM jammed. 
![Screenshot 2026-06-03 201932.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjY4NjQsInB1ciI6ImJsb2JfaWQifX0=--316c45d276bc4092538eeea16c26033f91b9a39c/Screenshot 2026-06-03 201932.png)

Next, I did the same with the inner CAM. Since this one only had 4 possible orientations, it was a lot easier to design. I did the same routine/process as the outer CAM, just a lot less complicated.
![Screenshot 2026-06-03 213512.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjY4NjUsInB1ciI6ImJsb2JfaWQifX0=--d546a2cdf383761d051c0cc3a1481a9ba6630991/Screenshot 2026-06-03 213512.png)

In the end, I got two finished designs of the CAMs needed for a single braille cell. But since they are inside each other, a problem would be to how to operate each with a servo. I was thinking, since the inside one is surrounded by the outside, the servo has to be from the bottom, so I can either directly design it onto the servo, or I can link them with bevel gears to put the servo at an angel if I liked. The outside CAM was originally hard to think of a design, but I realized I could simply just create a gear pattern on its lower end and also gear a servo next to it. This helped give me a goal for tomorrow.
TLDR: I designed the physical inner and outer CAMs.
![Screenshot 2026-06-03 230340.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjY4NjYsInB1ciI6ImJsb2JfaWQifX0=--4695e6222fb49edf2a619ab9b4e6c558143bfdb1/Screenshot 2026-06-03 230340.png)

NOTE: Also oops, I accidentally named one of the timelapses (inner CAM design) 6/2 instead of 6/3.

### Recording Links

- https://lookout.hackclub.com/api/media/17b43fd1-0139-49f8-83d7-cb27872353d7/video.mp4
- https://lookout.hackclub.com/api/media/06e3b5d5-5656-443d-a121-36fdcbf41531/video.mp4

## Entry 3
- ID: 11789
- Author: kevinkunzhong
- Created At: 2026-06-05T07:02:50Z

### Content

Today, I first tried visualizing my CAM mechanism in an assembly to make sure it can rotate and the pins are able to slide up and down and contact the CAMs properly. I tried making it be able to move and all with the slider mates and revolute mates but I couldn’t get the tangent mate to work since the CAM is not a swept shape. I tried many different ways to get around this but in the end it just didn’t work so I just manually visualized it :) . 
![Screenshot 2026-06-04 113018.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc0ODQsInB1ciI6ImJsb2JfaWQifX0=--ca93420029ecb55fcadf3df27ce46008d41e2ba5/Screenshot 2026-06-04 113018.png)

Next, I made the CAMs actually be able to rest on something and not just be floating around. I am trying to finish up my cad today. I made it so that the CAMs will be able to slide into each other and essentially use each other to guide themselves so they keep in position. I did this by making a slot in the bottom CAM for the top CAM to slide into so it is resting on top of it. This way, I don’t need any complicated bearings and things for them to rotate. I also made the tolerances were good so they can actually spin without friction.
![Screenshot 2026-06-04 234724.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc0ODYsInB1ciI6ImJsb2JfaWQifX0=--d71f80a2700ba13ac0fa6f907cf08d46fa3ece0a/Screenshot 2026-06-04 234724.png)
![Screenshot 2026-06-04 172254.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc0ODcsInB1ciI6ImJsb2JfaWQifX0=--2d6af2303c582b3f26f4059e47ee98971fa7d5d1/Screenshot 2026-06-04 172254.png)

Next, I generated all of the gears I need to make sure my servos can move the CAMs. I did this using a featurescript in Onshape to generate the gears and then attached the gears to the CAMs to make them a single part using a bore hole and the boolean feature. This makes sure the parts print together and they move as a whole in real life. Then, by using the same module dimensions for the gears, I geared the gears in a 3:2 ratio to translate the 180 degrees of rotation in the servo to 270 degrees in the CAM. I did this for both CAMs and also attached the gears onto the servos. For the gears on the servo, I also made custom servo splines to directly attach the gears onto the servo. This is because it will be more stable.
![Screenshot 2026-06-04 165838.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc0ODgsInB1ciI6ImJsb2JfaWQifX0=--907844c83641c6a987703a07889a688c7776eff5/Screenshot 2026-06-04 165838.png)

Then, I did a LOT of research on what electronics I should use. I know that I will need a camera that will translate the irl letter to braille on the braille cell so I needed a camera. I started with that and found that I can use a raspberry pi to run it as well as the computer vision code. I then went around, since it is my first time working with electronics, finding the good raspberry pi and decided on the 5 with 4GB of RAM as recommended by people online. Then, it was time for the servos and I had to find somewhere to run them. I found the adafruit pca9685 which helped manage all my servos without connecting them directly to the raspberry pi and potentially frying and crashing it during running. After that, I learnt a little bit about how each of these things attach to one another as well as the wires I need, as well as the different cables, power supplies, terminal blocks, etc. After learning all this, I was finally ready to CAD all of these electronics into Onshape and create custom mounting places for them on my project. 
![Screenshot 2026-06-04 231530.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjc0ODksInB1ciI6ImJsb2JfaWQifX0=--384237a3c825813642881f755da6eb3a50c5791a/Screenshot 2026-06-04 231530.png)

TLDR: I finished cadding the gears for the CAMs, attached to servos, and researched about electronics I need.

### Recording Links

- https://lookout.hackclub.com/api/media/d6fa8885-6585-4d31-95a2-32a82572b36e/video.mp4
- https://lookout.hackclub.com/api/media/9060bb9c-0a13-41d8-80d9-0e8b3007a301/video.mp4
- https://lookout.hackclub.com/api/media/66f0dd8d-9adf-4a04-9a20-dd9096727c5d/video.mp4
- https://lookout.hackclub.com/api/media/579aa234-61f3-48e2-aaf2-f54608690615/video.mp4

## Entry 4
- ID: 12005
- Author: kevinkunzhong
- Created At: 2026-06-06T06:52:10Z

### Content

Today, I focused on mounting all of my electronics into my project. I looked at the 3D model of the electronics and made mounting areas, spacers, and plates according to their measurements with also a little bit of wiggle room in order for the wires and other stuff to pass through. I also stacked my pca board and the raspberry pi on top of each other to save space and ensure that my project fits inside a small box.
![Screenshot 2026-06-05 112508.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjgxMTAsInB1ciI6ImJsb2JfaWQifX0=--62e6c34bf8d587c816f374a46c6e3739012f015d/Screenshot 2026-06-05 112508.png)

One part of the project that I was very proud of was my camera mount. I don’t know, I just felt very creative at the moment and so I just created a very creative and cool camera mount that is also very effective, avoiding all the extrusions in the camera board.
![Screenshot 2026-06-05 114437.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjgxMTEsInB1ciI6ImJsb2JfaWQifX0=--5fb8bf89623079c6e57d6ae4ec240220a25cf42f/Screenshot 2026-06-05 114437.png)

After I have my electronics mounted, I started to stabilize the servos. I made very long pillars on the insides of the servos to prop them up, as well as including a screw hole in the center of course. On the outsides. I used a sort of half arc design to keep the mounts compact but effective. I also made it a two in one type of thing and made it so that it can not only hold the servo but also act as a wire guider to guide the servo wire and ensure it does not get caught in the gears. This leads me to my next design, a simple curved wall between the gears and the electronics. Since there will be a lot of wires, in order to make my design compact, I need to keep the electronics close to the gears. But that risks the wires getting caught. Therefore, the easiest solution is just to create a wall between them, which is what I did. 
![Screenshot 2026-06-05 131453.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjgxMTIsInB1ciI6ImJsb2JfaWQifX0=--05bd94ed01b58311e7e75d3dec7bb96492197155/Screenshot 2026-06-05 131453.png)

Then, I started to make the walls and the actual box that will contain all my important parts. But the wall is still equally important. I made it so that there are holes for the necessary components such as the camera, and the areas to plug in my external power supplies. I also made the wall relatively compact to keep the entire project compact.
![Screenshot 2026-06-05 155511.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjgxMTMsInB1ciI6ImJsb2JfaWQifX0=--826ae38174a8e78922ffacec29870a49bf79a22b/Screenshot 2026-06-05 155511.png)

I also sectioned the walls and roof into different parts to make assembling it as well as assembling the inside components a lot easier. I put holes in each part so I can easily assemble it later with screws. Now it is like building lego. I also extruded a bit more for the box since I learned that you should have a few mm of tolerance on each side for screw holes and I didn’t have that before; this made it more sturdy. Finally, I realized I should add a button at the top to take pictures to translate instead of analyzing live feed so I added that into the top portion of the roof. I also found a button online for sale which I can directly plug into the raspberry pi without any external breadboards and stuff like that.
![Screenshot 2026-06-05 173906.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjgxMTQsInB1ciI6ImJsb2JfaWQifX0=--c82ea129c40fc1025d13efc3f0f84be26c31553e/Screenshot 2026-06-05 173906.png)

Finally, I added some finishing touches to my project and colored the project how it will be when I 3D print it. I also spent some time adding some cool designs as well as more braille on the outside for ease of use (but also for aesthetic purposes). Now it looks very cool!
![Screenshot 2026-06-05 220245.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjgxMTUsInB1ciI6ImJsb2JfaWQifX0=--3c9eb908b64df6813ede850b70566c6897be525c/Screenshot 2026-06-05 220245.png)

TLDR: I attached the electronics, made mounts for everything, made the actual box, and designed it.

### Recording Links

- https://lookout.hackclub.com/api/media/847e5e3d-78bb-401d-ba62-6a97dd3baa10/video.mp4
- https://lookout.hackclub.com/api/media/56dfc40b-1351-43d3-9070-d5f5969ceb90/video.mp4

## Entry 5
- ID: 12208
- Author: kevinkunzhong
- Created At: 2026-06-07T05:45:17Z

### Content

Today, I finished up my cad by adding some finishing touches such as the holes which will help for an easier assembly. I also finished creating my assembly, taking all of the parts and electronics and put them together using mates. I also put revolute and gear mates on the CAMs to better help visualize them. I also researched on which screws to use for which electronics and also imported and took note of the different screws to use. I made sure to use the correct ones so my model will be put together properly. However, while I was doing this, I encountered a problem. The PCA board’s part model was not coming out properly so I had to re-cad its model based on the dimensions in order to import it into my assembly. Additionally, I also found the backlash dimensions for the gears and added in a bit to ensure the gears turn smoothly with minimal friction. I also organized my part studio features a little bit because it was getting out of hand. In the end, I finished putting screws on everything and mating all components together for my project model.
![Screenshot 2026-06-06 220110.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg2NjUsInB1ciI6ImJsb2JfaWQifX0=--714d1f36841fcfd79b12960f00e1d62326819dd7/Screenshot 2026-06-06 220110.png)

I also began working on my zine, brainstorming its theme. I know that I need a QR code to my repository as well as a few pictures and descriptions of my project. Since I named my project Tiresias’ Box, I was thinking to have a mysterious, Greek mythology type theme for my zine. I wanted a dark green aura and mist for the color scheme. I also wanted to draw a cartoon picture of Tiresias very auraful and holding my project.
![Screenshot 2026-06-06 223742.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg2NjYsInB1ciI6ImJsb2JfaWQifX0=--06c415c69e34facc24417d4c85e1a668a937ef48/Screenshot 2026-06-06 223742.png)

I also started my README, researching a little bit on what I should include for a hardware project. I created a document that listed out my stuff and thought process and what components to add to my README. I started looking at other people’s READMEs and found some inspiration on what to put into mine. I did a general outline on what to write today and I will start writing soon.
![Screenshot 2026-06-06 223926.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg2NjcsInB1ciI6ImJsb2JfaWQifX0=--0a6c2f99e09351b4e1f2274fd38520fc9ab8edbb/Screenshot 2026-06-06 223926.png)

Finally, I did some testing with my 3d CAM model for the first time! I went in very optimistic but my first model did not come out good. My pins kept jamming in the CAM and some tolerances were not good so the CAMs could not spin properly. I printed my models using a 0.2 nozzle and the finest settings in my Bambu slicer so my models overall came out very nice. This is so that my curves for the CAM are as smooth as possible, as well as my layers. However, I did also figure out my pins were hard to put into their slots so I needed to also widen them a little bit. Overall, the first model was not bad. 
![v1 testing.jpg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjg2NjgsInB1ciI6ImJsb2JfaWQifX0=--cd2669a9ced35821dc713aaf80f3182d7b3df27e/v1 testing.jpg)

TLDR: I made my CAD assembly, started my zine and README designs, and tested my first CAM model. 

### Recording Links

- https://lookout.hackclub.com/api/media/7246bb88-8616-46b3-b0ab-54a43fc396ca/video.mp4
- https://lookout.hackclub.com/api/media/76c34f42-1cf1-4e91-8394-28b946cc46d6/video.mp4

## Entry 6
- ID: 12433
- Author: kevinkunzhong
- Created At: 2026-06-08T05:06:19Z

### Content

I was honestly a bit tired today so I didn’t do much. But I still did as much as I can lol. I did lots and lots of 3d printing today, testing out my CAMs and pins, which are the most important parts. I printed using the most fine settings to get the best layers and most precise parts. I tested and tweaked multiple different measurements for the CAM such as making it half as tall, which made my CAM much smoother since the pins don’t need to travel that much distance now. It also jams a lot less. Another tweak I made to make it jam less is by making the pin tip a bit bigger since the original point is very small and sometimes get caught between the layer lines of the print. Yes very annoying. I also made the holes for the pins ever so slightly bigger to make it have less contact with the pins. Overall, everything is coming together very nicely actually. I also made the pins taller since I realized there is a bit of room and the taller they are, the easier they are to feel irl so yeah very nice!
![Screenshot 2026-06-07 190542.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkxNjksInB1ciI6ImJsb2JfaWQifX0=--85978576237600a457e74fc7a3e2b3572fa90a9c/Screenshot 2026-06-07 190542.png)
![Screenshot 2026-06-07 192345243.jpeg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkxNzAsInB1ciI6ImJsb2JfaWQifX0=--22bace0cbb223462392e22a8b7b81e9fc4fef2b9/Screenshot 2026-06-07 192345243.jpeg)

I also added a bit more design to my outer box to indicate where the front is and which side of the box should be facing up. This makes this more aesthetic lol but also contributes to the practicality.
![Screenshot 2026-06-07 190227.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkxNzIsInB1ciI6ImJsb2JfaWQifX0=--19d66532faf36fa8b64b2ab54b61b208f5cc6d14/Screenshot 2026-06-07 190227.png)

I also created my BOM, which includes every single part that is needed for my project. I also added in some kits for screws and solders since I don’t have any of those parts and someone who is in my situation probably also doesn’t have them. I also included wires I need to solder or cut for my project as well as connect to my electronics. However, no matter how hard I scour online I can’t find sellers that sell only singular units so they are all in like “bulk” but not really “bulk”, just more than I need but I made the sure prices are cheap, please please. This is also the same for the servos. I also researched which servos to use and digital was my best bet for precision turning. However, the least I can find for digital servos is like 3 and I only need 2 so that was annoying but it is cheap I promise :,)
![Screenshot 2026-06-07 220046.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjkxNzMsInB1ciI6ImJsb2JfaWQifX0=--bc9944469d41436fb6e1477813c682c02d533fd2/Screenshot 2026-06-07 220046.png)

TLDR: Lots of printing and testing, tweaked the CAMs, pins and holes, added more design to the outer box, created BOM.

### Recording Links

- https://lookout.hackclub.com/api/media/31a8774f-5bac-42b9-b532-be0d844d5105/video.mp4

## Entry 7
- ID: 12698
- Author: kevinkunzhong
- Created At: 2026-06-09T06:29:41Z

### Content

Today, I did a lot of research for how to write code for the Raspberry Pi and the Adafruit PCA9685. I learned a lot about all the libraries I needed to use as well as the functions and syntax for coding for Raspberry Pi using Python. For my project, I needed to translate irl words that blind people cannot see, into braille for them to read. Therefore, I figured out how to code my raspberry pi camera and using easy OCR to take a picture on the raspberry pi and then analyze that picture for text. OCR is a computer vision library like OpenCV to detect text in real life and returns it as character text on the computer. This allows me to be able to read text in the real world and convert it to strings that my code can read. I incorporated the easyocr Python library for this project. I wrote code for my servos, camera, and main execution branch in separate files, each initializing its own things. I finished writing the code that initializes the servos as well as functions to move the servos to positions that will pop up certain braille by moving the CAMs. However, the positions still need to be tuned as I do not have the parts to build this yet. I also wrote a custom function that moves the position servos gradually to the positions since the pins might jam or fling out if the CAM moves very quickly. Additionally, I wrote code for the camera, adding in functions to take a photo, and then further analyze the photos for text to return back to the main execution branch. When taking the pictures, it saves as a jpg to the Raspberry Pi but to save storage, I delete the image files after analyzing as they will be no more use. Finally, I made a custom logic loop for a button which takes a picture every short press but turns off the code running and the camera for a press that lasts longer than 3 seconds. This is pretty much it for the coding portion of my project and I was happy I finished it all today.
![Screenshot 2026-06-08 230851.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjk4MDIsInB1ciI6ImJsb2JfaWQifX0=--53f8fa3413fa686bbeb86afcbbf79a01520a83e9/Screenshot 2026-06-08 230851.png)

I also began to work on writing setup guides to the software and hardware processes. I made sure to write them as detailed as possible as well as include external resources for people like me, who are complete beginners, to be able to follow clearly. I was also learning along while writing these setup guides so they may be a bit wonky but I will definitely fix that tomorrow. I also tweaked my CAD assembly a little bit since my gear relations were not working and I could not for the life of me figure out why even though they looked fine in the preview; they just stopped working as soon as I confirmed them. So I just removed them entirely, I know the gears work anyways lol.
![Screenshot 2026-06-08 230832.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjk4MDMsInB1ciI6ImJsb2JfaWQifX0=--f22b3a268afd3ff78990caf35f7a8552949387fd/Screenshot 2026-06-08 230832.png)
![Screenshot 2026-06-08 230937.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6Mjk4MDQsInB1ciI6ImJsb2JfaWQifX0=--89aec936bfaac992a54a9207d05257306c3cecef/Screenshot 2026-06-08 230937.png)

TLDR: I coded everything and started writing the setup guides.

### Recording Links

- https://lookout.hackclub.com/api/media/83b3f5b6-0a11-41bf-927c-63a133a9216c/video.mp4
- https://lookout.hackclub.com/api/media/6f6a3f1d-f7f7-4dd8-b0e9-6db8cc77599b/video.mp4

## Entry 8
- ID: 12949
- Author: kevinkunzhong
- Created At: 2026-06-10T06:38:05Z

### Content

I finished all of the setup guides and finished everything that is required in the repository today. I made sure that the setup guide and the README were very well detailed and complete beginners would be able to follow them very easily. This was easy to test since I am a complete beginner and if I could follow them well, I knew that other people like me could as well. I spent a lot of time making all the files, guides, and the main README as nicely formatted as possible to make everything look extremely polished. I also added a lot more to the README than the required materials since I believe it encompasses my project a lot more and allows people to get a more descriptive grasp on my project, such as the highlights, the future, and the hardware section. I got these inspirations from the many READMEs of many other repos that I came across. 
![Screenshot 2026-06-09 114617.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA0NjEsInB1ciI6ImJsb2JfaWQifX0=--35fae18fbfc47b28435a81969866dbac9a1d00c1/Screenshot 2026-06-09 114617.png)
![Screenshot 2026-06-09 232442.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA0NjIsInB1ciI6ImJsb2JfaWQifX0=--b5d9d2a8a84b1f6954d35b2ef92082f4be49aad9/Screenshot 2026-06-09 232442.png)

I also redesigned the servo gears a bit and added a little overhang at the edge of the gears to help keep the CAM gears in place. This ensures that as long as the servo gears are attached properly to the servos, the CAM gears will not pop out of place and continue with its smooth motion with the servo gears. This also makes sure the CAM gears do not misalign that easily if the box is tilted or maybe even flipped upside down.
![Screenshot 2026-06-09 114557.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA0NjMsInB1ciI6ImJsb2JfaWQifX0=--a7e97b04fc3ef064951b8396f52655ff9877d0a8/Screenshot 2026-06-09 114557.png)

I also continued on beginning on designing my zine today. I did start earlier but I wanted a better design. Since I had a Greek prophet’s name for my project, I was thinking of a Greek mythology theme. But since my project uses white and orange, I had to either go with a black orange or white orange theme. And I chose black orange. I was genuinely out of ideas for the day and I started with a very simple background for my zine and generated my qr code. I also had a rendered picture of my finished assembled 3D model to be the main graphic in the center.
![Screenshot 2026-06-09 232213.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzA0NjYsInB1ciI6ImJsb2JfaWQifX0=--0ffff26db515bf17b9d5a9b3a9475ffe395222c4/Screenshot 2026-06-09 232213.png)

TLDR: I finished everything in the repo, tweaked the gears, and I started to create a zine.

### Recording Links

- https://lookout.hackclub.com/api/media/d6c820fa-8891-49f7-b0c0-9bd89653d141/video.mp4
- https://lookout.hackclub.com/api/media/66f1351b-bd33-4efe-a607-abbc8ac0d33f/video.mp4

## Entry 9
- ID: 13163
- Author: kevinkunzhong
- Created At: 2026-06-11T04:43:59Z

### Content

Today I worked on the final part of my Fallout submission, the zine. I was initially thinking to actually draw Tiresias and him holding up my project but I tried for a while and it was honestly too complicated (and I don’t know how to draw so drawing humans was extremely challenging). So, I just went with a very simple “design around my project” approach and just made my zine visually appealing (at least I think) by using a lot of colors and other hand drawn designs! Since my project is white and orange, I was thinking of using a orange theme to create my designs. I honestly don’t know my thought process behind my design I just went with the flow and tried out a lot of new things and eventually this is what came out. I also went into my cad and brought out some parts, especially the custom CAM and made them transparent background like my project picture. After adding them to my repo, I think I am done with my design submission! I am so happy that I finished designing this project and I really hope my design gets accepted.
![Screenshot 2026-06-10 182337.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzEwNTIsInB1ciI6ImJsb2JfaWQifX0=--d334fb2968aa58b93cca0fca46d89445a5c459bb/Screenshot 2026-06-10 182337.png)
![fallout_zine_png.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzEwNTMsInB1ciI6ImJsb2JfaWQifX0=--b0f74a6643016e11b1e8213bc4b7f198961689d4/fallout_zine_png.png)

TLDR: I finished my zine and everything I need for submission.

### Recording Links

- https://lookout.hackclub.com/api/media/8ef3fb35-5e08-4fac-b283-3ef1e938641a/video.mp4
- https://lookout.hackclub.com/api/media/4bb23151-9a4d-4088-9f98-a242de43eb11/video.mp4

## Entry 10
- ID: 13394
- Author: kevinkunzhong
- Created At: 2026-06-12T06:45:40Z

### Content

Today, I added onto my initial code and added in the support for translating Chinese to English. I used the Python library deep_translator to have a quick and efficient way of translating from other languages to English without having to sacrifice the precious RAM that I need for OCR. I made new functions in my code that essentially takes the extracted text from OCR and translates it into English to then translate into braille. So it is basically adding a layer of translation! I added this because I am Chinese, and also Chinese is one of the most widely spoken languages with English so adding support for it is a must imo. However, I don’t want to run unnecessary models or libraries since I already have so little RAM. So, I also added in a toggle between English and Chinese to English with the button and changed the timing a little so the button can take a picture, toggle language, and turn off the camera/code. I also updated my README and installation steps due to this change. Furthermore, I also researched more on the memory usage of EasyOCR and find that it was very scary and actually does use quite a lot of RAM for my purposes. Therefore, I looked into a quantized model that lessens the precision and helps with the memory and latency, especially with using a CPU and no GPU for RPI. One more thing I added is the support for numbers in the braille as well and I found that my braille cam actually works for numbers as well so I added that into the positions dictionary and the extracting text code. 
![Screenshot 2026-06-11 234223.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE3MjMsInB1ciI6ImJsb2JfaWQifX0=--3c1d34f2144fe38880ac4d58b731ed8b5fdd6192/Screenshot 2026-06-11 234223.png)
![Screenshot 2026-06-11 234201.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE3MjQsInB1ciI6ImJsb2JfaWQifX0=--c5292d64cb0a9fdfc6b8ccd4e6bdbcc0c8b34514/Screenshot 2026-06-11 234201.png)
![Screenshot 2026-06-11 234135.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzE3MjUsInB1ciI6ImJsb2JfaWQifX0=--b22fafc86acaf42818aec5385691dfe9afb3e580/Screenshot 2026-06-11 234135.png)

TLDR: I added in support for Chinese to English translating, added in numbers for braille, optimized EasyOCR model.

### Recording Links

- https://lookout.hackclub.com/api/media/11503b03-8c5a-4e3a-a15b-e0e48f8e22f6/video.mp4

## Entry 11
- ID: 13653
- Author: kevinkunzhong
- Created At: 2026-06-13T06:21:34Z

### Content

Today I officially started the build process of my project and it started off fairly well. Almost all of my parts have arrived so I was able to begin putting everything together and testing up my servos. I also got my Raspberry Pi so I was able to do everything with the software setup and that went somewhat smoothly. During the process, I encountered an issue where the Raspberry Pi ran out of storage to install the easyocr package but that was very confusing since it definitely had enough storage for that. However, after looking into the problem more, I realized that the Pi was using its RAM drive to help install the packages, quickly filling up the 2GB space. Therefore, I had to force pip to use the main drive to install it. Since I would assume this problem would also occur with others, I included the steps I used to solve it in the revised software setup guide.
![Screenshot 2026-06-12 184528.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzIzNDMsInB1ciI6ImJsb2JfaWQifX0=--a241829aa707c06279e114338ff255edec712ef7/Screenshot 2026-06-12 184528.png)
![Screenshot 2026-06-12 231338.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzIzNDQsInB1ciI6ImJsb2JfaWQifX0=--2db5ed2498e20686d73bf1c7b3b5810e08aa3cf8/Screenshot 2026-06-12 231338.png)

Next, I went on to solder the PCA9685. This was my very first time soldering so I was very careful and watched a few tutorials before I started. My dad was also watching next to me in case I burnt myself. I took a long time to get the hang of soldering and melting the solder wire cleanly on the pins but eventually I got it and it was actually quite fun. As I tried not to burn myself, I finished up with the soldering and got all the pins and the terminal block to be on the board. I then stripped some of the 20AWG wires and connected the terminal block to the power adapter. Now, I am done with the PCA9685 setup.
![pca.jpeg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzIzNDUsInB1ciI6ImJsb2JfaWQifX0=--1947ce9e57932e3a2d51e675b984c232de337382/pca.jpeg)

Finally, I also tested the servo code as well as the gradual movement code and tuned the delay time to be about 0.01 seconds. This allowed me to have a smooth transition from position to position. I connected all the wiring to the Raspberry Pi and all the power supplies and the servos and this was my first official test (excluding the camera). Everything worked very well but the only thing was the servo positions was not 180 it was more like 120 but that should be fine.
![IMG_4576.jpeg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzIzNDYsInB1ciI6ImJsb2JfaWQifX0=--8047a6972bf67234cc1e21b5c6ee9a219bf43be4/IMG_4576.jpeg)


TLDR: I setup the Raspberry Pi software, I soldered the PCA9685, I tested the servo code with nearly everything setup.

### Recording Links

- https://lookout.hackclub.com/api/media/8df4c368-a249-4b13-a1bb-eed6c1fdeb17/video.mp4
- https://lookout.hackclub.com/api/media/155d09e0-21f7-4988-b6ee-0d9a9449b5f4/video.mp4

## Entry 12
- ID: 13828
- Author: kevinkunzhong
- Created At: 2026-06-13T21:43:07Z

### Content

Today, I tested the servo gears but then I realized the custom servo spline for the micro servo was too precise to be printed properly with the servos so I just decided to change my design and embed the servo horn that the servos came with into the servo gears. Along with this, I also tested the tolerances of the holes the screws would be screwed into and I resized a lot of the holes. Using a caliper and the servo horn in real life, I measures its dimensions and created an area for it to be embedded inside of the servo gears. This works because it is rotational motion and the servo gear is connect to the servo horn still since it has a hole at the top in which the servo screw is gonna be screwed in.
![Screenshot 2026-06-13 112331.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzI4MTgsInB1ciI6ImJsb2JfaWQifX0=--26b86c3169697d1841a8f03dd97e6ed3fe991ffb/Screenshot 2026-06-13 112331.png)


Another thing I added to the cad is a ventilation system (aka just a few holes) under the raspberry pi to allow it cool down better. This allows it to cool better since I noticed that it heated up quite much when running some test code yesterday. Hopefully this will allow it to run better. This also uses less filament lol. 
![Screenshot 2026-06-13 125155.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzI4MTcsInB1ciI6ImJsb2JfaWQifX0=--e531fbae382db470f7e35b74f0a43cff354a82d3/Screenshot 2026-06-13 125155.png)

Afterwards, all of these changes had me to change the hardware setup instructions as well as update the cad files in the repo.

TLDR: Embedded servo horn for servo gears, resized holes, added ventilation.

### Recording Links

- https://lookout.hackclub.com/api/media/98a2ab8f-967d-4abf-babc-359203d88b2d/video.mp4
- https://lookout.hackclub.com/api/media/97477996-9b61-456d-8456-5f9eb3d7c2c8/video.mp4

## Entry 13
- ID: 14473
- Author: kevinkunzhong
- Created At: 2026-06-16T06:46:28Z

### Content

Today I worked on many different things, a lot of which are just testing my components and building. I first finished printing out everything I needed, as well as doing the manual filament color changing since I don’t have an AMS soo yeah. I did not record myself 3D printing btw lol. Anyways, the colors came out very nice and while I was doing that, I also had to tweak a few more hole tolerances for my prints and finally everything is coming together very nicely with the screws. 
![IMG_4579.JPG](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzQzMDIsInB1ciI6ImJsb2JfaWQifX0=--5c1641859aa1a8c5c4139ec7e82bb93d13889c8a/IMG_4579.JPG)
=

For the roof print, I had a very fun time taking off all of the supports since it was a very weird print to orient in the slicer and the colored side had to face up so that was very fun. Another part is the embedded servo horn which I tested and it worked out amazingly, the tolerance was perfect first try and I was very proud of myself for that.
![IMG_4581.jpeg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzQzMDMsInB1ciI6ImJsb2JfaWQifX0=--22346b5f217cefaf6c9cff376b5dd41da10e0800/IMG_4581.jpeg)

I also tested a few things with my code. I tested my easyocr and it worked out perfectly. There was a few hiccups and the red text was a big scary but I was able to get it working with a few tweaks such as flipping the camera orientation in the code since I did not realize that the camera would be mounted upside down. I also changed some of the timing since the camera needed a bit more time to focus than I thought, but it was fine afterwards. I tested the camera with a few different lines of words and my pipeline was able to perfectly split the words into characters nicely. I was also surprised and very proud, and also anxious since I didn’t know what to do if it failed lol.
![IMG_4580.jpeg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzQzMDUsInB1ciI6ImJsb2JfaWQifX0=--67438d711615e2bb2ac30e63d3655792b4bb9cc5/IMG_4580.jpeg)

Finally, I also tested the code for the button and it worked fine so I was happy to finally start building. I used my hardware setup guide, to screw everything in and plug the wires in where they are supposed to go. This process was somewhat smooth but sometimes my hands get sweaty and since I am using M2 and M2.5 screws, the allen key is very small and it slips a lot and I get very annoyed. But otherwise, the building process I would say is half complete and the only thing left is to tune the servo positions and screw the walls in.
![IMG_4584.jpeg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzQzMDYsInB1ciI6ImJsb2JfaWQifX0=--8cc212c163a250fa6622672844521b70eb88a5b7/IMG_4584.jpeg)

TLDR: I tested the code, and I started building.

### Recording Links

- https://lookout.hackclub.com/api/media/c806b337-4877-4848-b1ce-7aa41e5820a0/video.mp4
- https://lookout.hackclub.com/api/media/aa9fbc9a-7178-413d-bf52-5835d92567af/video.mp4

## Entry 14
- ID: 14705
- Author: kevinkunzhong
- Created At: 2026-06-17T06:36:00Z

### Content

Today I finished up assembling the whole thing and started tuning the positions of the pins. However, during the process, the servo gears that are colored accidentally got snapped so I had to use my red ones, which are the exact same thing but a different color. Along with that, I finished printing the pins and I also tested my code for the pins. I also retuned the speed constant at which the gears would be rotating to help smooth out the motion of the pins. I assembled the walls, and securely attached all parts of my project. Tuning tins took a long time since you needed to make sure the positions are correct to a very accurate degree so I usually had to go degree at a time for the rotation angle. This took up the bulk of my time. Other than that nothing much really happened. I really hope I can finish tuning tomorrow at test my full code and then hopefully finish my project tomorrow!
![IMG_4586.jpeg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzQ4OTEsInB1ciI6ImJsb2JfaWQifX0=--a75afc41fbdc748a7b5742494efdb6701d4fcbd7/IMG_4586.jpeg)
![IMG_4585.jpeg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzQ4OTIsInB1ciI6ImJsb2JfaWQifX0=--5dac3aa60382e1ee6b22813e670a4cf676e12f75/IMG_4585.jpeg)


### Recording Links

- https://lookout.hackclub.com/api/media/7dbc6cdd-b765-40c9-b0fc-50a6e47d394b/video.mp4

## Entry 15
- ID: 15138
- Author: kevinkunzhong
- Created At: 2026-06-19T03:16:02Z

### Content

Today and yesterday, I finished testing everything and although the cv on my project takes some time to process (since I am running on a Raspberry Pi), MY PROJECT FINALLY WORKS!! This is actually so surprising and I feel so proud because I genuinely didn’t take many attempts to test my project. My final attempts were just used in the video I made later on explaining this project. I made some final adjustments to my project, such as adding barriers to the cams (and I updated the repo :) ) which made my cams and pins even smoother and now they can even run at full speed with the rotating servo without jamming one bit. However, I still set the speed a bit lower just to be safe (and for aesthetic purposes since making it move slower makes it seems so much more cooler). I also finished tuning all the positions of the braille pins for every single letter and number. I didn’t do it for every letter and number, I just did it for every possible combination and then combined the inner and outer cam values to make up the values needed for each letter.
![Screenshot 2026-06-18 200948.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzYwMjIsInB1ciI6ImJsb2JfaWQifX0=--2f85213ebc066c4563a11f37524382f99ddac21a/Screenshot 2026-06-18 200948.png)

I tested my chinese translator as well by typing and printing out a sheet of paper with chinese characters on it and IT WORKED! First try lol. But it was so cool watching my project in action and working properly after all the time I spent making it. After my final bits of testing and confirming my project works 100%, I started creating the video used to showcase my project, making it actually shipped. I did some video planning, taking some of the text I wrote for my repo and making it into a script for me to say. I also printed out a few testing materials (text) to show off on my video. Later, I started filming the actual video and then after filming, I started putting the video together on capcut. Capcut was so laggy and my video was corrupted the first time around and I COULD NOT FIND THE VERSION HISTORY. So I had to salvage my video and that took some time but in the end, it came out how I wanted it to. I genuinely did not know I could create something like this in 14 days and I want to thank fallout for giving me this opportunity. I am so excited to finish! Please go watch my demo video, it has a lot of cool clips and stuff :)))))
![front.jpeg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzYwMjEsInB1ciI6ImJsb2JfaWQifX0=--a6e23948b77e0096fe0798056a5660c0cdbdc64e/front.jpeg)

TLDR: FINAL SUCCESS

### Recording Links

- https://lookout.hackclub.com/api/media/6ca60236-953b-4222-a0a4-50c2169f14e2/video.mp4
- https://lookout.hackclub.com/api/media/41a01b6f-2deb-4bb6-ae12-ca7666a528d8/video.mp4
- https://lookout.hackclub.com/api/media/dd32f75c-4f4d-4a17-a409-42afcd3b34cb/video.mp4
- https://lookout.hackclub.com/api/media/b6a09a5d-43a2-489e-99c0-87a0cfdae077/video.mp4
- https://lookout.hackclub.com/api/media/b85b4b3b-036c-490d-896f-32da0922bc62/video.mp4
- https://lookout.hackclub.com/api/media/daee17cc-462d-4080-af52-c1dd61495655/video.mp4
