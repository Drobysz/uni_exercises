from fltk import *
from models.snake import *
from models.apples import *
from window import *
from time import sleep
from typing import Literal

game_state = Literal['suspended', 'finished']

def is_continued() -> bool:
    event = attend_ev()
    if type_ev(event) == 'Touche' and touche(event) == 'Escape':
        return False
    return True 

def play_one_game() -> game_state:
    window = Window(10, 600)
    apples = Apples(30, int(sqrt(window.nb_cases)))
    snake = Snake(5)
    cs = window.case_size

    while True:
        window.render(snake, apples)
        event = donne_ev()
        event_type = type_ev(event)
        
        snake.shift_snake()
        if apples.is_apple(snake.current_coordinates()):
            snake.body_positive()

        if event_type == 'Touche':
            key = touche(event)
            
            snake.change_dir(key)
            if key == 'Escape':
                return 'suspended'
        
        if snake.isEncountered(window.width, cs):
            window.loss()
            return 'finished'
        
        if apples.nb_apples == 0:
            window.win()
            return 'finished'

        sleep(0.1)

def main():
    while True:
        state = play_one_game()
        if state == 'suspended':
            ferme_fenetre()
            break
        if not is_continued() and state == 'finished':
            break
        ferme_fenetre()

if __name__ == '__main__':
    main()
