from fltk import *
from models.snake import *
from models.apples import *
from window import *
from time import sleep

def is_continued() -> bool:
    event = attend_ev()
    if type_ev(event) == 'Touche' and touche(event) == 'Escape':
        return False
    return True 

def play_one_game():
    window = Window(10, 600, 40)
    apples = Apples(8)
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
                ferme_fenetre()
                break
        
        if snake.isEncountered(window.width, cs):
            window.loss()
            break
        
        if apples.nb_apples == 0:
            window.win()
            break

        sleep(0.1)

def main():
    while True:
        play_one_game()
        if not is_continued():
            break 
        ferme_fenetre()

if __name__ == '__main__':
    main()
