import pyray as pr
from raylib import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

from .agent import Screen

HEIGHT = 640
WIDTH = 480

pr.init_window(HEIGHT, WIDTH, "The Ball Pit.")
pr.set_target_fps(60)
screen = Screen(HEIGHT, WIDTH, pr, 1)
colours = [
    (255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255)
]

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)


    screen.step(1)

    pr.draw_text(
        "Delete to remove balls | L/R arrow keys for colour", 10, 460, 20, pr.WHITE
    )
    pr.draw_text(
        "Click to add balls  | Right-Click to add 10 balls", 10, 440, 20, pr.WHITE
    )
    pr.draw_text("Arrow key up to increase speed", 10, 20, 20, pr.WHITE)
    pr.draw_text("Arrow key down to decrease speed", 10, 40, 20, pr.WHITE)
    if screen.speed > 4:
        pr.draw_text(f"Speed: {round(screen.speed, 1)}", 10, 60, 40, pr.RED)
    elif screen.speed < 0:
        pr.draw_text(f"Speed: {round(screen.speed, 1)}", 10, 60, 40, pr.BROWN)
    elif 0 <= screen.speed < 1:
        pr.draw_text(f"Speed: {round(screen.speed, 1)}", 10, 60, 40, pr.BLUE)
    else:
        pr.draw_text(f"Speed: {round(screen.speed, 1)}", 10, 60, 40, pr.GREEN)
    pr.end_drawing()

    if pr.is_mouse_button_pressed(0):
        position = pr.get_mouse_position()
        screen.spawn((position.x, position.y))
    if pr.is_mouse_button_pressed(1):
        for _ in range(10):
            position = pr.get_mouse_position()
            screen.spawn((position.x, position.y))

    if pr.is_key_down(KEY_UP) and screen.speed < 4.9:
        screen.speed += 0.1
    if pr.is_key_down(KEY_DOWN) and screen.speed > -4.9:
        screen.speed -= 0.1
    
    if pr.is_key_pressed(KEY_LEFT):
        i = colours.index(screen.colour)
        screen.colour = colours[i-1]
    if pr.is_key_pressed(KEY_RIGHT):
        i = colours.index(screen.colour)
        if i == len(colours)-1:
            screen.colour = colours[0]
        else:
            screen.colour = colours[i+1]


pr.close_window()