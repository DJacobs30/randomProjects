import pygame
import math
import sys

def run_sim():
    ''' Function to Run the Simulator '''

    screen = pygame.display.set_mode((800, 540))
    cart = CollisionCarts(screen)

    while True:
        screen.fill((100, 100, 100))

        cart.move_carts()
        cart.check_collide()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cart.move_cart = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    cart.move_cart = False
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

class CollisionCarts():
    ''' Class to hold all the funtions for the collision carts '''

    def __init__(self, screen):
        ''' Initialize the Carts Class '''
        self.screen = screen
        self.ctype = 'e'
        self.move_cart = False
        self.collision = False

        self.cart_width, self.cart_height = 50, 25
        self.x1, self.y1 = 200, 100
        self.x2, self.y2 = 600, 100

        self.m1, self.v1 = 100 , 0
        self.m2, self.v2 = 10, 4

        self.ex = 2

        self.image1 = pygame.Surface((self.cart_width, self.cart_height))
        self.rect1 = self.image1.get_rect(bottomleft=(100, 100))

        self.image2 = pygame.Surface((self.cart_width, self.cart_height))
        self.rect2 = self.image2.get_rect(bottomright=(300, 100))

    def move_carts(self):
        ''' Move the Carts '''
        if self.move_cart and not self.collision:
            self.x1 += self.v1
            self.x2 -= self.v2
            print(self.v1, self.v2)

        if self.move_cart and self.collision:
            self.x1 -= self.v1f
            self.x2 += self.v2f
            print(self.v1f, self.v2f)


    def check_collide(self):
        ''' Check If the Cart Rects Collided '''

        if self.rect1.colliderect(self.rect2):
            self.collide()

        self.rect1 = self.image1.get_rect(bottomleft=(self.x1, self.y1))
        self.rect2 = self.image2.get_rect(bottomright=(self.x2, self.y2))
        
        pygame.draw.rect(self.screen, (150, 0, 0), self.rect1)
        pygame.draw.rect(self.screen, (0, 0, 150), self.rect2)

    def collide(self):
        ''' if the carts collided, change momentum according to the collision type '''

        if self.ctype == 'e':
            ''' Elastic Collision '''
            self.collision = True

            mr1 = self.m1/self.m2
            mr2 = self.m2/self.m1

            self.v1f = self.v2*mr2
            self.v2f = self.v1*mr1

        if self.ctype == 'ie':
            ''' Inelastic Collision '''
            self.collision = True

            vf = ((self.v1*self.m1)+(self.v2*self.m2))/(self.m1+self.m2)
            self.v1f, self.v2f = vf, vf

        if self.ctype == 'ex':
            ''' Explosion Collision '''
            self.collision = True

if __name__ == '__main__':
    pygame.init()
    run_sim()