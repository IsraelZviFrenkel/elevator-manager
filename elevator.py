from floor import *

# Calculate the time between the last task to the new task
def time_of_new_task(last_task, current_task):
    if last_task > current_task:
        time = (last_task - current_task) / PIXELS_PER_SECONDS
    elif last_task < current_task:
        time = (current_task - last_task) / PIXELS_PER_SECONDS
    else:
        time = 0
    return time


class Elevator:

    def __init__(self, num):
        self.num = num
        self.image = pygame.transform.scale(pygame.image.load(ELEVATOR_IMAGE_PATH), (ELEVATOR_WIDTH, ELEVATOR_HEIGHT))
        self.pos = (FLOOR_WIDTH + 10 + num * ELEVATOR_WIDTH, SURFACE_HEIGHT - 80)
        self.current_floor = 0
        self.tasks = []
        self.tasks_time = 0
        self.floor_stop = 2


    # Drae the elevators
    def draw(self, world):
        world.blit(self.image, self.pos)

    # Bring the last task
    def get_last_task(self):
        if self.tasks:
            return self.tasks[len(self.tasks) - 1].pos[1]
        else:
            return self.pos[1]

    # Add the new task to the tasks array
    def add_stop(self, floor):
        self.tasks_time += time_of_new_task(self.get_last_task(), floor.pos[1]) + 2
        self.tasks.append(floor)


    def set_floor_stop(self, delta_time):
        if self.floor_stop == 2:
            pygame.mixer.music.load(SOUND)  # Play the sound
            pygame.mixer.music.play()
        self.floor_stop = max(self.floor_stop - delta_time, 0)  # Stays 2 seconds in the floor
        if self.floor_stop == 0:
            self.tasks[0].elevator_on_the_way = False
            self.tasks.pop(0)
            self.floor_stop = 2

    # Update the current position of the elevator
    def update(self, delta_time):
        if self.tasks:
            self.current_floor = None
            current_task = self.tasks[0].pos[1]
            if current_task > self.pos[1]:
                self.pos = self.pos[0], min(self.pos[1] + delta_time * PIXELS_PER_SECONDS, current_task)
            elif current_task < self.pos[1]:
                self.pos = self.pos[0], max(self.pos[1] - delta_time * PIXELS_PER_SECONDS, current_task)

            else:
                self.current_floor = self.tasks[0].level
                self.set_floor_stop(delta_time)
            self.tasks_time = max(self.tasks_time - delta_time, 0)  # Decrease the time of tasks as long as the elevator moves
        else:
            self.tasks_time = 0


