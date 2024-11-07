import pygame
import random
import math
#initialize pygame
pygame.init()

#constants
FPS=60
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 4, 4
RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS
OUTLINE_COLOR = (187,173,160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205,192,180)
FONT_COLOR = (119,110,101)

pygame.display.set_caption("2048")
FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20
#pygame window
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self):
        color_index = int(math.log2(self.value)) - 1
        color = self.COLORS[color_index]
        return color

    def draw(self,window):
        color= self.get_color()
        pygame.draw.rect(window, color, (self.x,self.y,RECT_WIDTH,RECT_HEIGHT))
        text = FONT.render(str(self.value), 1, FONT_COLOR)
        #blit makes you put an object on top of the screen
        window.blit(
            text,
            (self.x + (RECT_WIDTH/2 - text.get_width()/2), 
             self.y + (RECT_HEIGHT/2 - text.get_height()/2)
            ),

        )

    def set_pos(self):
        pass

    def move(self,delta):
        pass

def draw_grid(window,tiles):
    for tile in tiles.values():
        tile.draw(window)
    pygame.draw.rect(window,OUTLINE_COLOR,(0,0,WIDTH,HEIGHT),OUTLINE_THICKNESS)

def draw(window,tiles):
    window.fill(BACKGROUND_COLOR)
    draw_grid(window,tiles)
    pygame.display.update()

def main(window):
    #clock object to regulate speed of loop
    clock = pygame.time.Clock()
    run = True

    tiles={
        "00":Tile(128,0,0), "01":Tile(2,0,1)
    }

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
                break
        draw(window,tiles)

    pygame.quit()

if __name__=="__main__":
    main(WINDOW)

