from elevator import *


class Building:
    def __init__(self, num_of_floors, num_of_elevators):
        self.floors = [Floor(i) for i in range(num_of_floors)]
        self.elevators = [Elevator(i) for i in range(num_of_elevators)]

    # This function call for each floor and each elevator to draw themselves

    def draw(self, world, delta_time):
        for level in range(len(self.floors) - 1):  # Call the all floors except the last one
            self.floors[level].draw(world)
            self.floors[level].update_button(delta_time)

        # Call the last floor
        self.floors[-1].draw(world, not_last_level=False)
        self.floors[-1].update_button(delta_time)

        for elevator in self.elevators:
            elevator.draw(world)
            elevator.update(delta_time)

    # Check which elevator it will take the shortest time to arrive the current floor
    def allocate_elevator(self, pos_y):
        """
        function
        :param pos_y:
        :return:
        """
        min_time = float("inf")
        chosen_elevator = None
        for elevator in self.elevators:
            last_task = elevator.get_last_task()  # Check which floor the elevator will finish its tasks
            time_of_current_task = time_of_new_task(last_task, pos_y)   # How much time it takes from last task to the current task
            if elevator.tasks_time + time_of_current_task < min_time:
                min_time = elevator.tasks_time + time_of_current_task
                chosen_elevator = elevator
        return chosen_elevator, min_time

    # Check if one of the buttons were pressed
    def if_elevator_was_invited(self, pos):
        for floor in self.floors:
            if floor.press_button(pos):
                chosen_elevator, min_time = self.allocate_elevator(floor.pos[1])
                # Check if there is an elevator in the floor, or an elevator was invited already
                if floor.level != chosen_elevator.current_floor and not floor.elevator_on_the_way:
                    floor.timer = min_time
                    floor.elevator_on_the_way = True
                    # Add the current task to the tasks array
                    Elevator.add_stop(chosen_elevator, floor)
