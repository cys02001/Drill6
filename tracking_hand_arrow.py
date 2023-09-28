from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                arrow_x, arrow_y = event.x, TUK_HEIGHT - event.y
                arrows.insert(0, (arrow_x, arrow_y))


def draw_character(x, y, flip):
    character.clip_composite_draw(frame * 100, 0, 100, 100, 0, flip, x, y, 200, 200)

def draw_arrow(x, y):
    arrow.draw(x, y)

def move_character(character_x, character_y, target_x, target_y, move_speed):
    dx = target_x - character_x
    dy = target_y - character_y
    dist = (dx ** 2 + dy ** 2) ** 0.5

    if dist > move_speed:
        character_x += dx / dist * move_speed
        character_y += dy / dist * move_speed
    else:
        character_x, character_y = target_x, target_y

    return character_x, character_y

running = True
frame = 0

arrow_x, arrow_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
move_speed = 1

arrows = []

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    for arrow_x, arrow_y in arrows:
        draw_arrow(arrow_x, arrow_y)

    if arrows:
        arrow_x, arrow_y = arrows[-1]
        if arrow_x < character_x:
            draw_character(character_x, character_y, '')
        else:
            draw_character(character_x, character_y, 'h')
        character_x, character_y = move_character(character_x, character_y, arrow_x, arrow_y, move_speed)
        if character_x == arrow_x and character_y == arrow_y:
            arrows.pop()
    else:
        draw_character(character_x, character_y, '')
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()