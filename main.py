import pyray as pr


if __name__ == "__main__":

    sprites = {
        "player": [{
            "rec": pr.Rectangle(0,0,32,32),
            "col": pr.RED
        }],
        "enemies": [
            {
                "rec": pr.Rectangle(0,0,32,32),
                "col": pr.PURPLE,
            },
            {
                "rec": pr.Rectangle(32,32,32,32),
                "col": pr.GREEN,
            }
        ]
    }


    player = pr.Rectangle(0,0,32,32)
    pr.init_window(800, 800, "Sprite Layers")
    pr.set_target_fps(60)
    cam = pr.Camera2D((400,400), (player.x, player.x), 0, 4)

    while not pr.window_should_close():
        if pr.is_key_down(pr.KEY_RIGHT):
            sprites["player"][0]["rec"].x += 2
        elif pr.is_key_down(pr.KEY_LEFT):
            sprites["player"][0]["rec"].x -= 2
        elif pr.is_key_down(pr.KEY_UP):
            sprites["player"][0]["rec"].y -= 2
        elif pr.is_key_down(pr.KEY_DOWN):
            sprites["player"][0]["rec"].y += 2

        cam.target = (sprites["player"][0]["rec"].x, sprites["player"][0]["rec"].y)

        pr.begin_drawing()
        pr.draw_fps(10,10)
        pr.clear_background(pr.BLACK)
        pr.begin_mode_2d(cam)

        # Draw sprites sorted by their Y-axis positions
        new_sprites = sprites["player"] + sprites["enemies"]
        for y in sorted(new_sprites, key=lambda pos: pos["rec"].y):
            index = new_sprites.index(y)
            pr.draw_rectangle_pro(new_sprites[index]["rec"], (16,16), 0, new_sprites[index]["col"])

        
        pr.end_mode_2d(cam)
        pr.end_drawing()
    pr.close_window()  