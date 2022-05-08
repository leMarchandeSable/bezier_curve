import pygame
import numpy as np


blanc = (255, 255, 255)
gris = (150, 150, 150)
noir = (0, 0, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)
vert = (0, 255, 0)


class Point:
    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.r = 10
        self.r_plus = 3 * self.r

        self.surface = surface

    def is_click(self):
        x, y = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            if self.x - self.r_plus < x < self.x + self.r_plus:
                if self.y - self.r_plus < y < self.y + self.r_plus:
                    return True
        return False

    def move(self):
        if self.is_click():
            x, y = pygame.mouse.get_pos()
            self.x = x
            self.y = y

    def show(self, color=blanc):
        pygame.draw.circle(self.surface, color, (self.x, self.y), self.r)

    def update(self):
        self.move()
        self.show()


class Ligne:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.pt = Point(self.p1.x, self.p1.y, self.p1.surface)

        self.t = 0
        self.alpha = self.angle()

        self.switch = 1

    def middle(self):
        return (self.p1.x + self.p2.x) // 2, (self.p1.y + self.p2.y) // 2

    def angle(self):
        if self.p2.x > self.p1.x:
            return np.arctan((self.p2.y - self.p1.y) / (self.p2.x - self.p1.x))
        elif self.p2.x < self.p1.x:
            return np.pi - np.arctan((self.p2.y - self.p1.y) / (self.p1.x - self.p2.x))
        elif self.p2.x == self.p1.x:
            if self.p1.y < self.p2.y:
                return np.pi / 2
            else:
                return - np.pi / 2

    def len(self):
        return ((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2)**0.5

    def show(self):
        star = (self.p1.x, self.p1.y)
        end = (self.p2.x, self.p2.y)
        pygame.draw.line(self.p1.surface, blanc, star, end, 2)

    def update(self):
        self.alpha = self.angle()
        self.pt.x = self.p1.x + np.cos(self.alpha) * self.t * self.len()
        self.pt.y = self.p1.y + np.sin(self.alpha) * self.t * self.len()

        self.t += self.switch * 0.0002
        if self.t >= 1 and self.switch == 1:
            self.switch = -1
        if self.t <= 0 and self.switch == -1:
            self.switch = 1


