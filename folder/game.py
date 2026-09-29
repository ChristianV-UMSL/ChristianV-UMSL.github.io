

from random import randint
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

#--------------------------------
time_left = int(21)
kirby_speed = 1 # base movement speed, increases with score
#--------------------------------


kirby = Actor("kirby")
kirby.pos = 100, 100
coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    kirby.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    # --------------------------------changed str to str(int())
    screen.draw.text("time: " + str(int(time_left)), color="black", topleft=(10, 30))
    #      my edit
    # --------------------------------
    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)
        ######added restart prompt###
        screen.draw.text("press R to restart", topleft=(10, 80), fontsize=30)
        #######restart########
        #if keyboard.r:
            #screen.fill("red") #testing that code was correct
        #############################
def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score, time_left, game_over, kirby_speed
    #####added code: timer count down#######
    time_left = time_left -(.05/3)
    ########################################
    if keyboard.left:
        kirby.x = kirby.x - 2*kirby_speed #changing them from elif to if allows diagonal movement
    if keyboard.right: #            elif: exclusive       if: inclusive
        kirby.x = kirby.x + 2*kirby_speed
    if keyboard.up:
        kirby.y = kirby.y - 2*kirby_speed
    if keyboard.down:
        kirby.y = kirby.y + 2*kirby_speed
    coin_collected = kirby.colliderect(coin)
    if coin_collected:
        sounds.coin.play()  #coin sound effect added
        score = score + 10
        place_coin()
        ######kirby speed increase########
        kirby_speed = kirby_speed + .5
        #############################
    ########Restart feature implemented#########
    if keyboard.r:
        game_over = False
        time_left = int(21)
        score = 0
        kirby_speed = 1
        kirby.pos = 100, 100
        clock.schedule(time_up, 20.0)
    ############################################


clock.schedule(time_up, 20.0)
place_coin()