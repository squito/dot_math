global x
global y
x = 0
y = 0

import pygame


def main():
  pygame.init()
  screen = pygame.display.set_mode((1280, 720))
  evt_flag = threading.Event()
  clock = pygame.time.Clock()

  def draw_vertical(x):
    pygame.draw.line(screen, (0, 0, 0), (x, 0), (x,780), 10)
    
  def draw_horizontal(y):
    pygame.draw.line(screen, (0, 0, 0), (0, y), (1280,y), 10)

  running = True
  while running:
      # poll for events
      # pygame.QUIT event means the user clicked X to close your window
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              print("got a quit")
              running = False
  
      # fill the screen with a color to wipe away anything from last frame
      screen.fill("white")
  
      # RENDER YOUR GAME HERE
      for x_pos in range(160, 1280, 160):
        draw_vertical(x_pos)
      for y_pos in range(90, 720, 90):
        draw_horizontal(y_pos)
      
      draw_x = (x + 4.0) * 1280 / 8
      draw_y = (y + 4.0) * 720 / 8
      pygame.draw.circle(screen, (0, 0, 255), (draw_x, draw_y), 20, 20)
   
  
      # flip() the display to put your work on screen
      pygame.display.flip()
  
      clock.tick(60)  # limits FPS to 60

  pygame.quit()


if __name__ == "__main__":
  main()
else:
  import threading
  t1 = threading.Thread(target=main())
  t1.start()
  t1.join()

