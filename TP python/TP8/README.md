# Note to the teatcher

### I completely rewrote your initial file snake_init.py and my project has grown to 3 models and 1 little library of view methodes. I'm sorry that i deviated from the original methodes, but i made it for simplicity, for a better code readability.

### I consider that even a simple game like this cannot be fit into one file. It would have taken more time to develop it if i had kept writing the code within a single file. At some point i just felt it'd become difficult to navigate through the file.

# Sneak

## Props:
- size: initial lenght of snake
- dir: current snake directory
- body: list of snake cell coordinates

## Methodes:
- render: rendering of snake
- isEncountered: checking if snake encountered itself of map borders
- current_coordinates: coordinates of snake head
- body_positive: adding of 1 cell to the end of the list
- sheft_snake: moving of snake per 1 cell to current directory
- change_dir: changing of current directory

# Apples

## Props:
- nb_apples: number of apples
- apples: list of coordinates of apples

## Methodes:
- render: rendering of apples on the map
- is_apple: check if there is an apple on the transmitted coordinates
            and deletes it if there is one

# Window

### Description: it's responsible for:
- 1. rendering of all elements on tne map
- 2. displaying of headers
- 3. window and cases configuration

# View
- view_case: it views one case
- view_cases: it views list of cases