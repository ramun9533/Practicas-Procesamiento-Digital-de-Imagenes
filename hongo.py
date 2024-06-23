import pygame
import numpy as np
import random
import math

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physarum Polycephalum Simulation")

# Parámetros de la simulación
NUM_AGENTS = 50
SENSOR_ANGLE = math.radians(90)
TURN_ANGLE = math.radians(30)
SENSOR_DISTANCE = 20
MOVE_DISTANCE = 3
TRAIL_DECAY = 0.99
TRAIL_INCREMENT = 10

# Colores
BACKGROUND_COLOR = (0, 0, 0)
TRAIL_COLOR = (0, 0, 255)
AGENT_COLOR = (255, 255, 255)

# Clase para los agentes
class Agent:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self):
        self.x += MOVE_DISTANCE * math.cos(self.angle)
        self.y += MOVE_DISTANCE * math.sin(self.angle)
        self.x = self.x % WIDTH
        self.y = self.y % HEIGHT

    def sense(self, trail_map):
        right_angle = self.angle + SENSOR_ANGLE
        right_x = int(self.x + SENSOR_DISTANCE * math.cos(right_angle)) % WIDTH
        right_y = int(self.y + SENSOR_DISTANCE * math.sin(right_angle)) % HEIGHT

        front_x = int(self.x + SENSOR_DISTANCE * math.cos(self.angle)) % WIDTH
        front_y = int(self.y + SENSOR_DISTANCE * math.sin(self.angle)) % HEIGHT

        left_angle = self.angle - SENSOR_ANGLE
        left_x = int(self.x + SENSOR_DISTANCE * math.cos(left_angle)) % WIDTH
        left_y = int(self.y + SENSOR_DISTANCE * math.sin(left_angle)) % HEIGHT

        right = trail_map[right_y, right_x]
        front = trail_map[front_y, front_x]
        left = trail_map[left_y, left_x]

        return right, front, left

    def update_angle(self, right, front, left):
        if front > right and front > left:
            return
        elif right > left:
            self.angle += TURN_ANGLE
        elif left > right:
            self.angle -= TURN_ANGLE
        else:
            self.angle += random.choice([-TURN_ANGLE, TURN_ANGLE])

# Inicializar agentes
agents = [Agent(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.uniform(0, 2 * math.pi)) for _ in range(NUM_AGENTS)]

# Mapa de rastro
trail_map = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar agentes
    for agent in agents:
        agent.move()
        right, front, left = agent.sense(trail_map)
        agent.update_angle(right, front, left)
        trail_map[int(agent.y), int(agent.x)] += TRAIL_INCREMENT

    # Desvanecer el rastro
    trail_map = np.where(trail_map > 0, trail_map * TRAIL_DECAY, trail_map)

    # Dibujar
    screen.fill(BACKGROUND_COLOR)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            brightness = trail_map[y, x]
            if brightness > 0:
                alpha = min(brightness, 255)
                color = (*TRAIL_COLOR, alpha)
                pygame.draw.circle(screen, color, (x, y), 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
