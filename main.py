import pygame , random , time 
pygame.font.init()
pole = pygame.display.set_mode(
    (500, 500)
)
BLUE = (200, 200, 255)
RED = (255, 70, 70)
Green = (162, 223, 115)
BLACK = (0, 0, 0)
YELLOW = (255,255,0)

pole.fill(Green)
clock = pygame.time.Clock()
class Area():
    def __init__(self, x, y, widht, height, color):
        self.rect = pygame.Rect(x, y, widht, height)
        self.color = color
    def set_color(self, new_color):
        self.color = new_color
    def fill(self):
        pygame.draw.rect(pole, self.color, self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(pole, frame_color, self.rect, thickness)
class Label(Area):
    def set_text(self, text, font_size=12, text_color=(0, 0, 0)):
        self.text_image = pygame.font.Font(None, font_size).render(text, True, text_color)
    def draw(self, shift_x=10, shift_y=30):
        self.fill()
        pole.blit(self.text_image,(self.rect.x+shift_x, self.rect.y+shift_y))

card_points = Label(0, 0, 100, 100 , YELLOW)
card_points.set_text('Очки')
card_time = Label(400, 400, 200, 200, YELLOW)
card_time.set_text('Время')
card_pobeda = Label(200, 200, 200, 200, YELLOW)
card_pobeda.set_text('ПОРАЖЕНИЕ')
card_proig = Label(200, 200, 200, 200, YELLOW)
card_proig.set_text('ПОРАЖЕНИЕ')
x = 70
cards = list()
for i in range(4):
    card = Label(x, 150, 70, 100, BLUE)
    card.set_text('Click', 30)
    cards.append(card)
    x += 100
wait = 0
points = 0
start_time = time.time()

while True:
    card_time.set_text('Время ' + str(round(time.time() - start_time)), 30)
    card_time.draw(0, 20)
    card_points.set_text('Очки ' + str(points), 30)
    card_points.draw(20, 20)
    event  = pygame.event.wait()
    
    
    
    if event.type == pygame.QUIT:
            break
            
    if points == 10 and time.time() - start_time <= 30:
        
        card_pobeda.set_text('ПОБЕДА', 30)
        card_pobeda.draw(25, 25)
    elif points <= 10 and time.time() - start_time >= 30:
        card_proig.set_text('ПОРАЖЕНИЕ',30 )
        card_proig.draw(25, 25)
    else:

        if wait == 0:
            click = random.randint(0, 3)
            for i in range(4):
                cards[i].set_color(BLUE)
                if click == i:
                    cards[i].draw(10, 30)
                else:
                    cards[i].fill()
                cards[i].outline(RED, 10)
            wait = 20
        else:
            wait -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            x,y = event.pos
            for i in range(4):
                if cards[i].rect.collidepoint(x, y):

                    if i == click:
                        cards[i].set_color(Green)
                        points += 1
                    else:
                        cards[i].set_color(RED)
                        points -= 1
                    cards[i].fill()  


    pygame.display.update()
    clock.tick(40)

