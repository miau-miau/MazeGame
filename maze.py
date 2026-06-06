from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 85:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 85:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 130:
            self.direction = "right"
        if self.rect.x >= win_width - 420:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite):
    direction = "up"
    def update(self):
        if self.rect.y <= 100:
            self.direction = "down"
        if self.rect.y >= win_width - 610:
            self.direction = "up"
        if self.direction == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        

win_width = 1000
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("back.jpg"), (win_width, win_height))

packman = Player('pusheeeen.png', 5, win_height - 100, 5, 45, 45)
monster = Enemy('angry.png', win_width - 450, 265, 2, 60, 50)
monster2 = Enemy2('angry.png', win_width - 300, 20, 4, 150, 110)
final = GameSprite('sushii.png', win_width - 750, win_height - 0, 0, 150, 150)

w1 = Wall(255, 255, 255, 0, 0, 700, 10)
w2 = Wall(255, 255, 255, 120, 110, 450, 10)
w3 = Wall(255, 255, 255, 120, 120, 10, 380)
w4 = Wall(255, 255, 255, 560, 110, 10, 150)
w5 = Wall(255, 255, 255, 150, 260, 420, 10)
w6 = Wall(255, 255, 255, 150, 350, 230, 10)
w7 = Wall(255, 255, 255, 150, 270, 10, 80)
w8 = Wall(255, 255, 255, 520, 350, 190, 10)
w9 = Wall(255, 255, 255, 700, 0, 10, 350)
w10 = Wall(255, 255, 255, 370, 350, 10, 130)
w11 = Wall(255, 255, 255, 510, 350, 10, 50)
w11 = Wall(255, 255, 255, 370, 470, 630, 10)
w12 = Wall(255, 255, 255, 990, 0, 10, 480)
w13 = Wall(255, 255, 255, 850, 360, 150, 10)

PINK_BG = (255, 182, 193)
WHITE = (255, 255, 255)
DARK_PINK = (255, 105, 180)
restart_btn = Rect(300, 400, 150, 50)
close_btn = Rect(550, 400, 150, 50)
status = "playing"

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!', True, (255, 182, 193))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        packman.update()
        monster.update()
        monster2.update()
        packman.reset()
        monster.reset()
        monster2.reset()
        final.rect.x = 750
        final.rect.y = 0
        final.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()

        if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, monster2) or sprite.collide_rect(packman, w13) or sprite.collide_rect(packman, w12) or sprite.collide_rect(packman, w11) or sprite.collide_rect(packman, w10) or sprite.collide_rect(packman, w9) or sprite.collide_rect(packman, w8) or sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w3) or sprite.collide_rect(packman, w4) or sprite.collide_rect(packman, w5) or sprite.collide_rect(packman, w6) or sprite.collide_rect(packman, w7):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()

        if sprite.collide_rect(packman, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()

    display.update()
    clock.tick(FPS)