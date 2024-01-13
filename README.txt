I created a python project that simulates a ball freefall, bounce off the edges of the screen, and come to a stop. 
The ball has a user specified mass and user specified x-velocity. The goal was to use my physics knowledge from high school and try to create a simulation. 
The goal was to make it look realistic, using the acceleration from gravity and an estimated amount of energy loss from each bounce to come to a rest.


I made a Freefall class which took in the parameter of how much mass the user wanted which they chose by clicking a button on the first screen. 
It takes the mass and sets the color of the ball to match the button. Then I created two methods which were for bouncing. 
One was called xBounce, it takes in the current x-velocity, changes the direction and reduces it by 10 percent. 
The other bounce method was called yBounce, which did the same thing but with the y velocity, but reduced it by 5 percent. 
These reductions weren’t scientific, they were just guesses.


The main function consists of creating the starting screen which takes the user inputs. 
Then, the first while loop starts where it continues until it is determined it is not bouncing significantly anymore. 
This loop updates the ball’s position for each frame. Keeping track of time and using a frame rate, I was able to update the position 60 times per second, 
and keep the acceleration accurate. This loop also checks to see if one of the bounce methods needs to be called. Once that loop ends, 
it goes to a loop which brings the ball to a stop, pretending it is rolling or sliding to a stop.


It took some testing to find a good percentage of reduction for the velocities after bounces. 
If I kept working on it, I may have chosen a scientifically accurate number, but it depends on the ball chosen. 
I tried to incorporate sound, but I ran into difficulties on windows getting the simpleaudio on my computer, therefore the sound wasn’t working. 
I created one sound for a bounce that would be the length of one frame which would replace the wait, 
but I imagine it would lag and cause problems if the sound had to be called instantaneously. 
I also created a sound which would be like background music, except it would be the ball bouncing sound. 
Unfortunately this would leave out bouncing off the walls since that would be different based on the initial x velocity. Also I couldn’t get it working either. 
Those two sounds are in the folder.


I did not use any code besides the button class. I had a decent idea how to approach this project because in my high school calculus based physics class, 
we coding with this platform called pyret, where we made simulations, but I did not have the code and it was very different from what we do here. 
That is also what inspired this project.