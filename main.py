import pygame
import time

# GAME VARS
WIDTH, HEIGHT = 800, 600
SCREENSIZE = (WIDTH, HEIGHT)
UPDATETIME = .05

# COLORS           R    G    B   
BLUE          = (  0,   0, 255)
RED           = (255,   0,   0)
GREEN         = (  0, 255,   0)
BLACK         = (  0,   0,   0)
bgColor = GREEN

def game():
  pygame.init()

  screen = pygame.display.set_mode(SCREENSIZE)
  text = pygame.font.SysFont('Comic Sans MS', 45)

  clickerImage = pygame.image.load("money.jpg")
  clickerImage = pygame.transform.scale(clickerImage, (255, 255))
  clickerRect = clickerImage.get_rect()
  clickerRect.center = WIDTH/2, HEIGHT/2

  coderBucks = 0          # Money
  hackers = 0             # Money Makers
  hackerValuePerSec = 2   # Money made per second
  hackerCost = 50         # Cost per Hacker
  hackerTime = 0          # Wait time for hackers

  hackerText = text.render(f'Cost of Hacker: {hackerCost}\nHackers Active: {hackers}', False, BLACK)
  hackerRect = hackerText.get_rect()
  hackerRect.left, hackerRect.top = (25, 75)

  while True:
    hackerTime += UPDATETIME
    if (hackerTime >= 1):
      coderBucks += hackerValuePerSec * hackers
      hackerTime -= 1
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if (clickerRect.collidepoint(x,y)):
          coderBucks += 1
        elif (hackerRect.collidepoint(x,y)):
          if coderBucks >= hackerCost:
            coderBucks -= hackerCost
            hackers += 1
      if event.type == pygame.KEYDOWN:
        key = pygame.key.get_pressed() 
        if event.key == pygame.K_SPACE:
          coderBucks += 1
        if event.key == pygame.K_1:
          if coderBucks >= hackerCost:
            coderBucks -= hackerCost
            hackers += 1

    screen.fill(bgColor)
    screen.blit(clickerImage, clickerRect)

    scoreText = text.render(f'Coder Bucks: {coderBucks}', False, BLACK)
    screen.blit(scoreText, (25,25))

    hackerText = text.render(f'Cost of Hacker: {hackerCost}\nHackers Active: {hackers}', False, BLACK)
    screen.blit(hackerText, hackerRect)

    pygame.display.flip()
    time.sleep(UPDATETIME)

if __name__ == "__main__":
  print("RUN CODE")
  game()