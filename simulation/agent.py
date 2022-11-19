import random
from math import cos, sin


class Screen:
    def __init__(self, width, height, screen, speed=1) -> None:
        self.size = (width, height)
        self.screen = screen
        self.speed = speed
        self.agents = [] #[Agent((width/2, height/2)) for x in range(20)]
        self.colour = (255, 255, 255)

    def draw(self):
        for agent in self.agents:
            self.screen.draw_circle_v((agent.x, agent.y), 5, self.screen.Color(*self.colour, 255))
            while len(agent.past) > 100:
                agent.past.pop(0)
            for (index, pos) in enumerate(agent.past):
                self.screen.draw_circle_v(pos, 5, self.screen.Color(*self.colour, int((200*index)/(len(agent.past)))))

    def step(self, time):
        for agent in self.agents:
            agent.move(self.speed, time, self.size)
        self.draw()
    
    def spawn(self, pos):
        self.agents.append(Agent(pos))


class Agent:
    def __init__(self, size) -> None:
        self.x, self.y = size
        self.angle = random.randint(0, 359)
        self.past = []

    def move(self, speed, time, size):

        self.past.append((self.x, self.y))

        if not (0 <= self.x <= size[0]):
            self.angle = random.randint(0, 359)
            if self.x < 0:
                self.x = 0
            else:
                self.x = size[0]

        if not (0 <= self.y <= size[1]):
            self.angle = random.randint(0, 359)
            if self.y < 0:
                self.y = 0
            else:
                self.y = size[1]
        self.x = self.x + cos(self.angle) * speed * time
        self.y = self.y + sin(self.angle) * speed * time
