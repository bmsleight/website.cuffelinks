Title: Miniature RGB
Date: 2015-04-19 17:00
Category: blog
Tags: cuffelinks, rgb
Author: Brendan M. Sleight


I designed a [prototype PCB](https://github.com/bmsleight/chameleon-cufflink/tree/master/pcb/breakout-test-pcb) in kicad and then ordered a small batch of them from the great [oshpark.com](https://oshpark.com/). I used interesting method to solder them, put the PCB on a standalone electric hotplate, move the components in to place with the aid of a USB microscope. 

<a href="images/Miniature-RGB/soldering.jpg"><img src="images/Miniature-RGB/thumbnails/480x_/soldering.jpg" /></a>

This actually worked, but proved I needed two cells to run all colours red, green and blue. 

![Alt text](images/Miniature-RGB/Successfully_soldering.gif)

Wired up to a simple sketch, to give some random colours. 

![Alt text](images/Miniature-RGB/Quite_good_RGB_need_to_tweak_to_reduce_flicker.gif)

I have since improved [the script](https://github.com/bmsleight/chameleon-cufflink/blob/master/software/chameleon/simple-random-colour.ino) a little to reduce the flicker. 
