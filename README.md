# Asteroids Game

This is a simple **Asteroids** game built as part of the [boot.dev](https://www.boot.dev). This program was written in slow steps, which will be described below. During this project I worked through the instructions on *boot.dev* as instructed in the program. I then took the code and used [ChatGPT](https://www.chatgpt.com) to make sure the comments were adequate and then used it to check the code for errors and optimize the code.

![boot.dev](https://blog.boot.dev/img/300/bootdev-logo-full-small.png)

## HOW IT WAS MADE

### Chapter 1: Pygame
This game is built using Pygame to generate the graphics and control the game pieces. In the first part of the [boot.dev](https://www.boot.dev) I installed Pygame and created a basic screen for the game to be played on.

#### INSTALL PYGAME

The first step was to ensure Pygame was installed correctly. Through the website, I learned that best practice is to create a virtual environment for Python. Creating a unique virtual environment for each Python project brings several benefits with it. First, it allows you to use different versions of libraries with each project and not worry about conflicts. It also provides an easy way for all collaborators to set up the same environment when working on a project together

For this project, a `requirements.txt` file is included that has the proper version of Pygame defined. Running `pip3 install -r requirements.txt` will install the proper libraries to your virtual environment.

#### LET'S BEGIN

The first step in building this project was to just build a boilerplate main.py file to begin running the program and have a base to build upon. It was just a simple piece of code importing `pygame` and writing a main function to output **Starting Asteroids!** Below is the code that as generated for this step.

```
import pygame

def main():
    print('Starting Asteroids!')

if __name__ == "__main__":
    main()
```

### Chapter 2: Player
