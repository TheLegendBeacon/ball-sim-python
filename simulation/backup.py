import random
from math import cos, sin

import pygame


class Screen:
    def __init__(self, height, width, screen, speed=1) -> None:
        self.height = height
        self.width = width
        self.screen = screen
        self.speed = speed
        self.agents = [Agent(width/2, height/2) for x in range(50_000)]

    def draw(self):
        for agent in self.agents:
            pygame.draw.rect(self.screen, (255, 255, 255), (agent.x, agent.y, 1, 1))

    def step(self, time):
        for agent in self.agents:
            agent.move(self.speed, time, self.height, self.width)
        self.draw()


class Agent:
    def __init__(self, x, y) -> None:
        self.x, self.y = x, y
        self.angle = random.randint(0, 359)

    def move(self, speed, time, height, width):
        if not (0 <= self.x <= width):
            self.angle = random.randint(0, 359)

        if not (0 <= self.y <= height):
            self.angle = random.randint(0, 359)

        self.x = self.x + cos(self.angle) * speed * time
        self.y = self.y + sin(self.angle) * speed * time
