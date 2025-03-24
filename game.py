global x
global y
x = 0
y = 0

import pygame
pygame.init()
max_width = 1280
max_height = 720
half_width = max_width / 2
half_height = max_height / 2
screen = pygame.display.set_mode((max_width, max_height))


def draw_vertical(x):
  thickness = 10 if x == half_width else 2 
  pygame.draw.line(screen, (0, 0, 0), (x, 0), (x,max_height), thickness)
  
def draw_horizontal(y):
  thickness = 10 if y == half_height else 2
  pygame.draw.line(screen, (0, 0, 0), (0, y), (max_width,y), thickness)

def render():
  # fill the screen with a color to wipe away anything from last frame
  global x
  global y
  screen.fill("white")

  # RENDER YOUR GAME HERE
  for x_pos in range(160, 1280, 160):
    draw_vertical(x_pos)
  for y_pos in range(90, 720, 90):
    draw_horizontal(y_pos)
  
  draw_x = (x + 4.0) * 1280 / 8
  draw_y = (y + 4.0) * 720 / 8
  print(f"{x}, {y}; {draw_x}, {draw_y}")
  pygame.draw.circle(screen, (0, 0, 255), (draw_x, draw_y), 20, 20)

  # flip() the display to put your work on screen
  pygame.display.flip()


def main():
  clock = pygame.time.Clock()


  running = True
  while running:
      # poll for events
      # pygame.QUIT event means the user clicked X to close your window
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              print("got a quit")
              running = False
      render()
  
  
      clock.tick(60)  # limits FPS to 60

  pygame.quit()


if __name__ == "__main__":
  main()
