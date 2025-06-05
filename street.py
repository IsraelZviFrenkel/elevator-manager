from building import *

class Street:
    def __init__(self, buildings_array):
        self.buildings = []
        self.positions = []  # To store x positions for each building
        self.total_width = 0

        current_x = MARGIN
        for building_data in buildings_array:
            building = Building(building_data[0], building_data[1])
            self.buildings.append(building)
            self.positions.append(current_x)
            current_x += building.size + MARGIN  # Add spacing between buildings

        self.total_width = current_x

    def draw(self, delta_time):
        street_surface = pygame.Surface((self.total_width, SURFACE_HEIGHT))
        street_surface.fill(WHITE)

        for i, building in enumerate(self.buildings):
            building_surface = building.draw(delta_time)
            street_surface.blit(building_surface, (self.positions[i], 0))

        return street_surface

    def if_elevator_was_invited(self, pos):
        for i, building in enumerate(self.buildings):
            # Adjust X pos relative to building
            relative_x = pos[0] - self.positions[i]
            if 0 <= relative_x < building.size:
                building.if_elevator_was_invited((relative_x, pos[1]))