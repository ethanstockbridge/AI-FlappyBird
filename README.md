
# AI Flappybird game

# Overview
This program impliments a similar creation of the game, flappybird. There are 3 options to run: Play the game yourself, Train the AI, and Play the resulting AI. 

# Methodology
This AI program impliments the NEAT algorithm to play a re-created version of flappybird using Pygame. Using python's NEAT library, we are able to give the AI network 3 inputs: bottom pipe height, top pipe height, and bird's y position. With this, the AI network uses (2) hidden nodes to do varying mathematical calculations to determine values of the output nodes. With each genome, this calculation changes in order to (hopefully) improve the output. Then these are piped to two output nodes, which represents 2 of the options: Jump, Not-Jump. The birds resulting action is determined by seeing which output node has the greatest value. 

# Installation

This project requires [Python](https://www.python.org/downloads/) to run, and the following plugins:

- [Pygame](https://www.pygame.org/news)
- [NEAT](https://neat-python.readthedocs.io/en/latest/)


# Testing
