#  Snake Game 
<br>

## Introduction :
- Snake Game is a video game genre where the player maneuvers a growing line that becomes a primary obstacle to itself. 
- The concept originated in the 1976 two-player arcade game Blockade from Gremlin Industries, and the ease of implementation has led to hundreds of versions (some of which have the word snake or worm in the title) for many platforms. 1982's Tron arcade game, based on the film, includes snake gameplay for the single-player Light Cycles segment. 
- After a variant was preloaded on Nokia mobile phones in 1998, there was a resurgence of interest in snake games as it found a larger audience. 
<br>

## Gameplay :
- The player controls a dot, square, or object on a bordered plane. As it moves forward, it leaves a trail behind, resembling a moving snake. 
- In some games, the end of the trail is in a fixed position, so the snake continually gets longer as it moves. 
- In another common scheme, the snake has a specific length, so there is a moving tail a fixed number of units away from the head. The player loses when the snake runs into itself.
- A sole player attempts to eat items by running into them with the head of the snake. Each item eaten makes the snake longer, so avoiding collision with the snake becomes progressively more difficult.
<br>

## About the Program:
- There are many languages from which *Snake Game* can be developed. 
  - I used `python` to develop this game.
- Again, there are many methods in which we can develop the game in Python. 
   - I used mainly `turtle` module to develop this game.
   - Used ` random ` to get random co-ordinates of snake-food.
   - Used ` tkinter ` to create a GUI.
<br>

## Packages used in this Program:
1. Turtle.
2. Tkinter.
3. Random.
<br>

## Packages need to be installed:

## 1. Turtle:

#### `turtle` is a Python feature like a drawing board, which lets us command a turtle to draw all over it! We can use functions like turtle.forward(…) and turtle.right(…) which can move the turtle around.

### Installation:

#### You can simply install this module by typing the below command in your terminal.

```
pip install turtle 
```
### To know more about turtle:

https://docs.python.org/3/library/turtle.html

## 2. Tkinter:

#### Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, ``tkinter`` is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter is the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.

### Installation:

#### You can simply install this module by typing the below command in your terminal.

```
pip install tkinter
```
### To know more about turtle:

https://docs.python.org/3/library/tkinter.html  
<br>

## Working of the Program:

- ### Initially `Tkinter` module is used to show a initial window with buttons i.e. Start and Exit. 

Below is the screenshot showing that:
![Screenshot (85)](https://user-images.githubusercontent.com/86250589/150624445-ab4f2495-87cf-4cdd-8751-c9e3bd8087ea.png)

- ### After the START button is pressed game is started and the snake starts to move with initially in upward direction.

Below is the screenshot showing the same:
![Screenshot (89)](https://user-images.githubusercontent.com/86250589/150624630-10ba07e3-422f-47f7-8606-abbefe36966f.png)

- ### When the snake touches the food, there will be addition of an element to the snake which results in the increase in the length of the snake.

Below sreenshot shows how length has increased to that of last screenshot:
![Screenshot (87)](https://user-images.githubusercontent.com/86250589/150624734-f672d85d-f8b4-416f-85e2-9778c7e5c2fc.png)

- ### After some time when there is a scenario where the snake bits itself, another window pops up and asks you some options. This is also done with the help of `Tkinter` module.

Below Screenshots shows such condition:
![Screenshot (88)](https://user-images.githubusercontent.com/86250589/150624814-da97cf6d-6a9c-49ec-9e6e-9c98d3501745.png)



