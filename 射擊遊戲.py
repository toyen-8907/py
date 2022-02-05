# sprite
import pygame
import random
import os
# 遊戲初始化 and 創建視窗
pygame.init()

WIDTH = 700
HEIGHT = 600

COLOR = (185, 211, 238)
R_CO = (200, 200, 122)
PLA = (100, 100, 100)
ORANGE = (238, 154, 0)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 元祖設定寬度高度

pygame.display.set_caption("第一個遊戲")

clock = pygame.time.Clock()
# 載入圖片 要先初始化pygame # 轉換成 pygame 容易讀取的格式
background_img = pygame.image.load(
    os.path.join("img", "background.png")).convert()
player_img = pygame.image.load(
    os.path.join("img", "player.png")).convert()
bullet_img = pygame.image.load(
    os.path.join("img", "bullet.png")).convert()
rock_img = pygame.image.load(
    os.path.join("img", "rock.png")).convert()


class Players(pygame.sprite.Sprite):  # 繼承 sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 48))
        self.image.set_colorkey(BLACK)
        # self.image.fill(PLA)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2
        self.rect.bottom = HEIGHT - 10  # 設定左上角x軸起始點 設定左上角y軸起始點
        self.speedx = 8

    def update(self):
        key_pressed = pygame.key.get_pressed()  # 回傳一整串布林值，表示鍵盤上的每個案件有無被按下去，有按下去是true

        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Rock(pygame.sprite.Sprite):  # 繼承 sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = rock_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -20)  # 設定左上角x軸起始點 設定左上角y軸起始點
        self.speedy = random.randrange(2, 6)  # 落石t垂直速度隨機
        self.speedx = random.randrange(-4, 3)  # 水平速度 負數才會向左移動

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -20)
            self.speedy = random.randrange(2, 6)
            self.speedx = random.randrange(-4, 3)


class Bullet(pygame.sprite.Sprite):  # 繼承 sprite
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y  # 設定左上角x軸起始點 設定左上角y軸起始點
        self.speedy = -10  # 子彈往上方所以是負的

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()  # 刪除sprite


all_sprites = pygame.sprite.Group()  # 建立所有 sprite 群組
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Players()
all_sprites.add(player)  # 把玩家加進群組

for rock in range(8):
    rock = Rock()
    all_sprites.add(rock)
    rocks.add(rock)

FPS = 60
running = True
# 遊戲迴圈
while running:
    clock.tick(FPS)  # 一秒鐘內最多可被執行幾次
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # 更新遊戲
    all_sprites.update()  # 執行每個 all_sprites 物件的 update 函式
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)
    '''sprite 內建碰撞判定函式(群組1,群組,碰撞後群組1是否刪除(布林值),碰撞後群組是否刪除(布林值))'''
    for hit in hits:
        r = Rock()
        all_sprites.add(r)
        rocks.add(r)

    hits = pygame.sprite.spritecollide(player, rocks, False)
    if hits:
        running = False
    # 畫面顯示
    screen.fill(COLOR)  # 元祖放三原色彩度
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)  # 畫出 SPRITE
    pygame.display.update()      # 更新畫面
pygame.quit()
