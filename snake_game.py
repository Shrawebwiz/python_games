import turtle
import random

width = 800
height = 600
delay = 200  # milliseconds
foodsize = 32
snakesize = 20

offsets = {
    "up": (0, snakesize),
    "down": (0, -snakesize),
    "left": (-snakesize, 0),
    "right": (snakesize, 0)
}

#highscore
high_score = 0

#load the high score if it exists
try: 
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    pass

def update_high_score():
    global high_score
    if score>high_score:
        high_score = score
        with open("highscore.txt", "w") as file:
            file.write(str(high_score))

def bind_direction_key():
    screen.onkey(lambda: set_snake_direction("up"),"Up")
    screen.onkey(lambda: set_snake_direction("down"),"Down")
    screen.onkey(lambda: set_snake_direction("right"),"Right")
    screen.onkey(lambda: set_snake_direction("left"),"Left")


def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":
            snake_direction = "up"

    elif direction == "down":
        if snake_direction != "up":
            snake_direction = "down"

    elif direction == "right":
        if snake_direction != "left":
            snake_direction = "right"

    elif direction == "left":
        if snake_direction != "right":
            snake_direction = "left"                        



def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    if new_head in snake or new_head[0] < -width / 2 or new_head[0] > width / 2 \
            or new_head[1] < -height / 2 or new_head[1] > height / 2:
        reset()
    else:
        snake.append(new_head)
        if not food_collision():
            snake.pop(0)  # keep the snake the same length unless collision


        stamper.shape("assets/snakehead.gif")
        stamper.goto(snake[-1][0], snake[-1][1])
        stamper.stamp()
        stamper.shape("circle")
        for segment in snake[:-1]:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()
        

       
        screen.title(f"Snake Game  Score: {score}  High Score: {high_score}")
        screen.update()
        turtle.ontimer(game_loop, delay)

def food_collision():
    global food_pos
    global score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        update_high_score()
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(-width // 2 + foodsize, width // 2 - foodsize)
    y = random.randint(-height // 2 + foodsize, height // 2 - foodsize)
    return x, y

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [snakesize, 0], [snakesize*2, 0],[snakesize*3, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()

screen = turtle.Screen()
screen.setup(width, height)
screen.bgpic("assets/bg2.gif")
screen.register_shape("assets/snakefood.gif")
screen.register_shape("assets/snakehead.gif")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
bind_direction_key()

stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("#009ef1")
stamper.penup()



food = turtle.Turtle()
food.shape("assets/snakefood.gif")
food.shapesize(foodsize / 10)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

reset()
turtle.done()
 