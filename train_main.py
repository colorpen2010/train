import wrap, random
from wrap import sprite, world, actions

# мир
wrap.add_sprite_dir("training_sprite's")
world.create_world(1000, 1000, 400, 10)
world.set_back_image('fon/pacman_fon/circus.jpg')

# игрок
player1 = sprite.add(sprite_type="mod's_pacman", x=500, y=500, costume='clown')
sprite.set_size(player1, 5, 5)
actions.set_size(player1, 35, 35, delay=1000)

# еда
ball_x = random.randint(100, 600)
ball_y = random.randint(100, 600)
ball = sprite.add(sprite_type='pacman', costume='dot', x=ball_x, y=ball_y)

# охота
actions.set_angle_to_point(player1, ball_x, ball_y, 2000)
actions.move_to(player1, ball_x, ball_y, 2000)
sprite.remove(ball)

# призрак
oxotnic1y = ball_y - 100
oxotnic1x = ball_x + 100
oxotnic1 = sprite.add("mod's_pacman", oxotnic1x, oxotnic1y, 'blue_hunter1')
oxotnic1govorit = sprite.add_text('попался я тебя сожру', oxotnic1x - 100, oxotnic1y - 100,text_color=[5,94,105])
sprite.set_costume(player1,'blue_hunter1')

player1right=sprite.get_right(player1)
actions.move_left_to(oxotnic1,player1right,1000)
sprite.remove(oxotnic1govorit)
oxotnic1govorit2=sprite.add_text('вот я тебя поймал пожарю тебя на шашлык',oxotnic1x - 200, oxotnic1y - 100,text_color=[5,94,105])
actions.set_angle(player1,-120)
actions.move_at_angle_dir(player1,1100,2000)