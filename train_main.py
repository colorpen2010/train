import wrap, random
from wrap import sprite, world, actions

# мир
wrap.add_sprite_dir("training_sprite's")
world.create_world(1000, 1000, 400, 10)
world.set_back_image()

# игрок
player1 = sprite.add(sprite_type="mod's_pacman", x=500, y=500, costume='clown')
sprite.set_size(player1, 5, 5)
actions.set_size(player1, 35, 35, delay=1000)

# еда
ball_x=random.randint(1, 999)
ball_y=random.randint(1, 999)
ball = sprite.add(sprite_type='pacman', costume='dot', x=ball_x, y=ball_y)

actions.set_angle_to_point(player1,ball_x,ball_y,2000)