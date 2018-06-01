# Pandemic Deck Simulator

## Purpose
This is a command-line based application for creating and shuffling Pandemic decks.

## Use
The use of the application is intuitive but must be run from a command line. When
prompted with an option, please answer with "Y"/"y" or "N"/"n". Once the application
is running, hit enter to end a turn and a new card will be drawn from the deck for
you to use in your real-life copy of the game.

## Development
### Difficulties
This was surprisingly difficult to code due to the specific nature of how a pandemic
deck must be shuffled. They must be split into a number of decks equal to the number
of epidemics that you are playing with. Finding an intuitive and simple way to do
this without just splitting the deck up and emulating how it would be done in real
life proved more complicated. I settled on randomizing the location of the Epidemics
in the deck for the same effect.

### Future
If I ever revisit this it would be nice to add more options and make it a little bit
more user friendly. Also, looking back, the way in which user input is processed is
quite gross and would best be handled from the command line.

## Copyright
This application acts as an extension of the Pandemic board game and should not be
used as a substitute for purchasing the actual content. I do not own Pandemic nor
do I claim to. This software uses the MIT License below.

MIT License

Copyright (c) 2017 David Gourevitch

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
