from datatime import datatime

WIDTH = 1280
HEIGHT = 640

# definicje klas
class Game:
    def __init__(self, background_active):
        # ustawiamy najważniejsze elementy, niektóre na stałe
        self.background_active = background_active
        self.background_position = (0, 0)
        self.game_start = False
        self.game_finish = False
        self.actual_room = 5
        self.start_time = None
        # grafiki na rozpoczęcie i zakończenie gry
        self.intro_canvas = Actor("intro-canvas.png")
        self.intro_canvas.pos = (640, -160)
        self.game_over_canvas = Actor("intro-gamover-canvas.png")
        self.intro_canvas.pos = (320, -160)

        # elementy związane z bohaterem
        self.floor_level = 460
        self.hero = Actor("character-right-01.png")
        self.hero.pos = (WIDTH / 2, self.floor_level)
        # wyznaczanie rozmiarow gracza
        self.hero.height = 256
        self.hero.width = 140
        self.hero.frame = 1
        self.animation_step = 15


    def draw_intro(self):
        def draw_text(text, x_offset, y_offset, fontsize=20):
            dcreen.draw.text (
            text,
            (self.intro_canvas.x + x_offset, self.intro_canvas.y + y_offset),
            fontname = "ptsansnarrowbold" )
            fontsize = fontsize,
            color = (187, 96, 191)
            )
        # wyswietlenie ekranu startowego
        self.intro_canvas.draw()
        animate(self.intro_canvas, pos=(640, 320), duration=0.3, tween = "linear")
        draw_text("Przygoda", -450, -200, fontsize=32)

        # wprowadzenie: przedstawienie histori gry, obsługa klawiszy
        story = (
            "Tu opisujemy swoja przygode "
            "ipsum dolor sit amet, consectetur adipiscing elit. Curabitur "
            "at arcu sollicitudin, elementum velit a, tempus erat. Quisque sed"
            "tortor id nibh ullamcorper dictum. Vivamus efficitur gravida mauris"
            "ut mattis. Fusce fringilla facilisis sagittis. In mi risus, pellentesque"
            "at sodales vitae, mattis vel nibh. Duis ac iaculis justo. Etiam a dolor eu"
            "\n\n"
            "klawisz 'Q' - koniec gry"
            "\n\n"
            "Spacja start gry"
        )
        screen.draw.text(
            story,
            (self.into_canvas.x - 450, self.intro_canwas.y - 160),
            width= 900,
            fontname = "ptsansnarrowregular"
            fontsize=20,
            color=(0,0,0)
        )
        # opis klawiszy kontrolnych
        draw_text("otwieranie drzwi", 200,-55)
        draw_text("chodzenie w lewo", 75,175)
        draw_text("podnoszenie", 220,175)
        draw_text("chodzenie w prawo", 330,175)
    def draw_pocket(self):
        self.pocket.draw()
        # ustalimy polozenie i odleglosci miedzy kluczami
        key_pos = [-200,-100,0,100,200]
        pass
    def hero_move(self, direction):
        if direction == "right":
            # jeżeli jest to mozliwe przesuwamy postać
            if self.hero.x < WIDTH - self.hero.width:
               self.hero.x += self.animation_step
        if direction == "left":
            if self.hero.x > self.hero.width:
                self.hero.x -= self.animation_step

    # wstawiamy odpowiedni obraze animujacy ruch
    self.hero.image = f"character-{direction}-0{self.hero.frame}.png"
    #zwiekszamy numer obrazka co bedzie pozwornie wygladalo jak ruch
    self.hero.frame +=1
    if self.hero.frame > 8:
        # to wracamy do 1
        self.hero.frame = 1

    def upade_game(self):
        if not self.game_start and keyboard.space:
            self.game_start = True
            self.start_time = datatime.now()
        if keyboard.q:
            quit()

        if self.game_start:
            if keyboard.right:
                self.hero_move("right")
            if keyboard.left:
                self.hero_move("left")






    def update_game(self):
        """ ta metoda będzie wywoływana z funkcji update() programu głównego """
        screen.blit(self.background_active, self.background_position)

    def draw_scene(self):
        # rysujemy tło
        screen.blit(self.background_active, self.background_position)
        #rysujemy głównego bohatera
        self.hero.draw()

class Key:
    def __init__(self, key_name, in_pocket, room_number, place_on_floor):
        """ self oznacza *siebie samego* - czyli konkretny klucz """
        # te właściwości obiektu *self* przepisywane są z parametrów
        self.key_name = key_name
        self.in_pocket = in_pocket
        self.room_number = room_number
        self.place_on_floor = place_on_floor

    # na razie nie robimy nic
    pass

# podstawowe zmienne
background_active = "corridor-01.jpg"

# tworzymy klucze, a jako *self* będą przypisane nazwy zmiennych key_
key_00 = Key("key-00.png", False, 11, 1025)
key_01 = Key("key-01.png", False, 17, 80)
key_02 = Key("key-02.png", False, 16, 850)
key_03 = Key("key-03.png", False, 4, 950)
key_04 = Key("key-04.png", False, 0, 370)

# tworzymy zmienną gry
game = Game(background_active)

def update():
    game.update_game()

def draw():
    game.draw_scene()



class Door:
    def __init__(self, room_number, door_position, next_room_number, open):
        self.room_nymber = room_number
        self.x_left_door = door_position
        self.x_right_door = door_position
        self.next_room_number = next_room_number
        self.open = open
    pass

# tworzymy drzwi zgodnie z planem pomieszczeń
# domyślnie każde z drzwi będzie otwarte
door_00 = Door(0, 900, 5, True)
door_01 = Door(0, 900, 5, True)
door_02 = Door(0, 900, 5, True)
door_03 = Door(0, 900, 5, True)
door_04 = Door(0, 900, 5, True)
door_05 = Door(0, 900, 5, True)
door_06 = Door(0, 900, 5, True)
door_07 = Door(8, 900, 3, False)
door_08 = Door(0, 900, 5, True)
door_09 = Door(0, 900, 5, True)
door_10 = Door(0, 900, 5, True)








