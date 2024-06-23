import pygame
import random
import math

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physarum Polycephalum Simulation")

# Parámetros de la simulación
NUM_AGENTS = 5000
MOVE_DISTANCE = 3
TURN_ANGLE = math.radians(30)
SENSOR_DISTANCE = 20

# Colores
BACKGROUND_COLOR = (0, 0, 0)
AGENT_COLOR = (255, 255, 255)

# Clase para los agentes
class Agent:
    def __init__(self, x, y, z, angle):
        self.x = x
        self.y = y
        self.z = z
        self.angle = angle

    def move(self):
        self.x += MOVE_DISTANCE * math.cos(self.angle)
        self.y += MOVE_DISTANCE * math.sin(self.angle)
        self.x = self.x % WIDTH
        self.y = self.y % HEIGHT

    def sense(self):
        return random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)

    def update_angle(self, right, front, left):
        self.angle += random.choice([-TURN_ANGLE, TURN_ANGLE])

# Inicializar agentes
agents = [Agent(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(-50, 50), random.uniform(0, 2 * math.pi)) for _ in range(NUM_AGENTS)]

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
        right, front, left = agent.sense()
        agent.update_angle(right, front, left)

    # Dibujar
    screen.fill(BACKGROUND_COLOR)
    for agent in agents:
        pygame.draw.circle(screen, AGENT_COLOR, (int(agent.x), int(agent.y)), 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
