import time
print('Server Started!')
number = 0
while True:
  print(f'Server: {number}th loop')
  print('Counting players...')
  players_raw = open('players.txt')
  players = int(players_raw)
  print(f'There are {players} players online')
  time.sleep(10)
  
  
  
