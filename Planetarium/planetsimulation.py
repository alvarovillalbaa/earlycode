from turtle import update
import pygame
import math

pygame.init()

WIDTH, HEIGHT = 900, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

FPS = 60

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (188, 39, 50)
DARK_GREY = (93, 93, 93)


SUN_MASS = 1.98892 * 10**30
EARTH_MASS = 5.9742 * 10**24
MARS_MASS = 6.39 * 10**23
MERC_MASS = 0.33 * 10**24
VENUS_MASS = 4.8685 * 10**24

FONT = pygame.font.SysFont("arial", 18)

# OOP: to simplify code
class Planet:
    # Defining physics constant variables
    AU = 149.6e6 * 1000  # Distance to Earth from Sun(Astronomical Unit)
    G = 6.67428e-11
    SCALE = 250 / AU  # 1 AU = 100 px
    TIMESTEP = (
        3600 * 24
    )  # 1 day movement of planets(to not make the simulation too long)

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False  # Beause we don't want the orbit of the Sun
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, window):
        x = self.x * self.SCALE + WIDTH / 2  # To be drawn in the middle of the window
        y = self.y * self.SCALE + HEIGHT / 2

        # Drawing the orbits
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(
                window, self.color, False, updated_points, 2
            )  # We pass False so that it is not an enclosed line

        pygame.draw.circle(window, self.color, (x, y), self.radius)

        if (
            not self.sun
        ):  # We must use a FONT variable to be able to rende text on the sreen
            distance_text = FONT.render(
                f"{round(self.distance_to_sun/1000, 1)} km", 1, WHITE
            )  # First 1 is for decimal points and second is for anti-aliasing
            window.blit(
                distance_text,
                (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2),
            )  # So that it's drawn dirctly on the center

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(
            distance_x**2 + distance_y**2
        )  # Pytagoras Triangle equation

        if other.sun:
            self.distance_to_sun = distance

        # Basic mathematical operations
        force = self.G * self.mass * other.mass / distance**2  # The force
        theta = math.atan2(distance_y, distance_x)  # The angle
        force_x = math.cos(theta) * force  # The Fx and Fy
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        # Calculating the force of the planets
        for planet in planets:
            if self == planet:
                continue  # Don't want the force off the same planet

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP  # v = a * t = (F / m) * t
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP  # r = v * t
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))  # Tuple


# To keep the program running(not opening and closing)
def main():
    run = True
    clock = (
        pygame.time.Clock()
    )  # To run it at a normal speed(no dependance on the computer speed)

    # We could/should have done a SIZE variable for easier comparison instead of putting all the data(same for other data)
    sun = Planet(0, 0, 30, YELLOW, SUN_MASS)
    sun.sun = True  # So that we don't set any distance from Sun to Sun(Sun = Sun)

    # Defintion of each planets' values
    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, EARTH_MASS)
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, MARS_MASS)
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, MERC_MASS)
    mercury.y_vel = (
        -47.4 * 1000
    )  # Negative because they start at the other end of the screen

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, VENUS_MASS)
    venus.y_vel = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(FPS)
        WINDOW.fill(BLACK)
        # pygame.display.update() used everytime we need to change appearance

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WINDOW)

        pygame.display.update()

    pygame.quit()


main()
