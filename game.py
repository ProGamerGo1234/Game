import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0
with open('players.txt') as players_raw:
  players1 = int(players_raw.read)
players_raw.close()
with open('players.txt', "w") as players:
  players.write(f'{players1 + 1}')
players.close()

player_location = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
     running = False

  screen.fill("lime")

  pygame.draw.circle(screen, "blue", player_location, 40)
  
  key = pygame.key.get_pressed()
  if key[pygame.K_w]:
    player_location.y -= 300 * dt
  if key[pygame.K_s]:
    player_location.y += 300 * dt
  if key[pygame.K_a]:
    player_location.x -= 300 * dt
  if key[pygame.K_d]:
    player_location.x += 300 * dt
    
  pygame.display.flip()
  dt = clock.tick(60) / 1000

pygame.quit()
