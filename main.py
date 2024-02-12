import pyray as pr
import numpy as np

import background

if __name__ == "__main__":

    sprites = {
        "enemies": [
        ]
    }

    player = {
        "type": "player",
        "rec": pr.Rectangle(0,0,32,32),
        "col": pr.RED,
    }

    seed = np.random.randint(0, 2**32)
    bck = background.Background(x=20,y=20,octaves=2,seed=seed)
    height_map = bck.generate_map()

    for i in range(30):
        pos_x = np.random.randint(0, 20)
        pos_y = np.random.randint(0, 20)
        sprites["enemies"].append({
                "type": "middleground",
                "rec": pr.Rectangle(pos_x*32,pos_y*32,32,64),
                "col": pr.WHITE,
            })

    pr.init_window(800, 800, "Sprite Layers")
    pr.set_target_fps(60)
    cam = pr.Camera2D((400,400), (player["rec"].x, player["rec"].x), 0, 4)


    while not pr.window_should_close():
        if pr.is_key_down(pr.KEY_RIGHT):
            player["rec"].x += 2
        elif pr.is_key_down(pr.KEY_LEFT):
            player["rec"].x -= 2
        elif pr.is_key_down(pr.KEY_UP):
            player["rec"].y -= 2
        elif pr.is_key_down(pr.KEY_DOWN):
            player["rec"].y += 2

        cam.target = (player["rec"].x, player["rec"].y)

        pr.begin_drawing()
        pr.draw_fps(10,10)
        pr.clear_background(pr.BLACK)
        pr.begin_mode_2d(cam)

        for x in range(20):
            for y in range(20):
                if height_map[x][y] <= 0:
                    pr.draw_rectangle(x*32,y*32,32, 32, pr.BLUE)
                elif height_map[x][y] > 0 and height_map[x][y] < 0.2:
                    pr.draw_rectangle(x*32,y*32,32, 32, pr.GREEN)
                else:
                    pr.draw_rectangle(x*32,y*32,32, 32, pr.PURPLE)


        # Draw sprites sorted by their Y-axis positions
        new_sprites = [player] + sprites["enemies"]
        for y in sorted(new_sprites, key=lambda pos: pos["rec"].y):
            index = new_sprites.index(y)
            if new_sprites[index]["type"] == "player":
                pr.draw_rectangle_pro(new_sprites[index]["rec"], (16,16), 0, new_sprites[index]["col"])
            else:
                pr.draw_rectangle_pro(new_sprites[index]["rec"], (0,32), 0, new_sprites[index]["col"])

        
        pr.end_mode_2d(cam)
        pr.end_drawing()
    pr.close_window()  