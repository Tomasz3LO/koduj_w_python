WIDTH = 1280 # szerokość okna
HEIGHT = 720 # wysokość okna

# definicje klas

class Game:
   # na razie nie robimy nice
  pass

class Key:
    # na razie nie robimy nice
  pass

# podstawowe zmienne
background_active = "corridor-01.jpg"
background_position = (0,0)

def update():
    screen.blit(background_active,background_position)
