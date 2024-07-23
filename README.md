flappy bird game
how it work:
A game consist of one bird in middle of the screen, there will be pipes going from the right to the left of the screen, the goal is to make the bird go through as much pipes as possible
About bird physics:
When clicked: the model rotate antilockwise and change increase the Y value
Gravity: if no click in put. the bird is pulled down by gravity, decreasing Y and model face down

About pipe movement:
The pipe create clone of it and move from right to left, the clone dismiss when touching the left end of the screen
the height of the pipe is generated randomly

About score count:
Score + 1 when the following conditions are met:
  The right end of the bird position (X value) is smaller than the pipe's right end
  The left end of the bird position (X value) is bigger than the pipe's left end

Game ends when:
Bird collide with pipe or floor, when it happens, the pipes stops, the birds no longer receive click input and fall to the ground if collide with pipe
The end screen pops up indicating score and high score, along with the medal the player gain for having such score
Below the end screen is the start button, which reset the game

When the game is reset:
The bird goes back to its original place
The clone pipes from last game are erased
