import pygame.draw
from constants import *


class Floor:
    def __init__(self, level):
        self.level = level
        self.elevator_on_the_way = False
        self.image = pygame.transform.scale(pygame.image.load(FLOOR_IMAGE_PATH), (FLOOR_WIDTH, FLOOR_HEIGHT))
        self.pos = POS_FLOOR_X, POS_FLOOR_Y - self.level * FLOOR_HEIGHT
        self.timer = 0

    # Draw the floors the button the black line in the top and the timer
    def draw(self, world, not_last_level=True):
        world.blit(self.image, self.pos)
        button_color = self.button_color()
        pygame.draw.circle(self.image, button_color, (75, 35), RADIUS_BUTTON, 0)
        if not_last_level:
            pygame.draw.line(world, BLACK, (POS_FLOOR_X, POS_FLOOR_Y - self.level * FLOOR_HEIGHT), (POS_FLOOR_X + FLOOR_WIDTH, POS_FLOOR_Y - self.level * FLOOR_HEIGHT), 9)
        number_of_floor = pygame.font.SysFont(None, 36, True, False)
        number_of_floor = number_of_floor.render(str(self.level), False, YELLOW)
        number_pos = number_of_floor.get_rect()
        number_pos.center = 75, 35
        self.image.blit(number_of_floor, (number_pos))

        numbers_of_timer = pygame.font.SysFont(None, 24, True, False)
        visual_timer = numbers_of_timer.render(str(round(self.timer, 2)), False, RED)

        if self.timer > 0:
            pygame.draw.rect(world, WHITE, (POS_FLOOR_X + 5, POS_FLOOR_Y - self.level * FLOOR_HEIGHT + 8, 40, 30), 0, 25)
            world.blit(visual_timer, ((POS_FLOOR_X + 8, POS_FLOOR_Y - self.level * FLOOR_HEIGHT + 14)))

    def press_button(self, pos: (int, int)):
        if RADIUS_BUTTON >= ((pos[0] - POS_FLOOR_X - FLOOR_WIDTH / 2) ** 2 + (pos[1] - (POS_FLOOR_Y + FLOOR_HEIGHT / 2 - self.level * FLOOR_HEIGHT)) ** 2) ** 0.5:
            return True

    def button_color(self):
        if self.timer > 0:
            color = RED
        else:
            color = GREEN
        return color


    def update_button(self, delta_time):
        if self.timer > 0:
            self.timer -= max(delta_time, 0)
            color = RED
        else:
            self.timer = 0
            color = GREEN



