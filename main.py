from building import *
from floor import *


pygame.init()


# Show the visible screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Elevator Project")
# Show the scrolling screen
world_surface = pygame.Surface((SCREEN_WIDTH, SURFACE_HEIGHT))


# Variables to scroll the screen
scroll_speed = 20
offset_y = SURFACE_HEIGHT - SCREEN_HEIGHT


previous_update = pygame.time.get_ticks()


# Create an object of building class
building = Building(NUM_OF_FLOORS, NUM_OF_ELEVATORS)

# Loop to run the game
run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:   # Play the exit button
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:   # Play the main button and the scrolling buttons
            if event.button == 1:
                event_pos = event.pos[0], event.pos[1] + offset_y
                building.if_elevator_was_invited(event_pos)
            elif event.button == 4:
                offset_y = max(0, offset_y - scroll_speed)  # Scroll the screen up
            elif event.button == 5:
                offset_y = min(SURFACE_HEIGHT - SCREEN_HEIGHT ,offset_y + scroll_speed) # Scroll the screen down

    current_update = pygame.time.get_ticks()    # Calculate the remainder between the updates
    delta_time = (current_update - previous_update) / 1000 # Converting from ms to seconds
    world_surface.fill(WHITE)
    building.draw(world_surface, delta_time)    # Call draw function
    previous_update = current_update
    # Copy the scrolling screen on the small screen
    screen.blit(world_surface, (0, 0), (0, offset_y, SCREEN_WIDTH, SCREEN_HEIGHT))


    pygame.display.update()
