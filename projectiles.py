class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        #pygame.draw.circle(self.image, RED, self.rect.center, self
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT  - 10
        self.speedx = 0 #user-built speed var
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
    def update(self):
        self.speedx = 0 #always stationary unless

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        if keystate[pygame.K_SPACE]:
            self.shoot()

        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot >self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            shoot_sound.play()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
    #Section #3: Draw the game state to the screen
screen.fill(WHITE)
    #screen.blit(background, background_rect)
all_sprites.draw(screen)
draw_text(screen, str(score), 18, WIDTH / 2, 10)
draw_shield_bar(screen, 5, 5, player.shield)

    # *after* drawing everything flip the display
pygame.display.flip()

    #check to see if a bullet hit a mob
hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
for hit in hits:
        score += 50 - hit.radius
        random.choice(expl_sounds) .play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        newmob()

      
