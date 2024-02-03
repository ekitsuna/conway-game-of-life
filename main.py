import time;
import pygame;
import numpy as np;

#colors
COLOR_BACKGROUND = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)

#size
SIZE = 100

#update functino
def update(screen, cells, size, with_process=False):
    #creates an empty grid
    updated_cells = np.empty((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        #runs calculations on number of alive neighboring cells 
        alive = np.sum(cells[row-1:row+2, col-1:col-2]) - cells[row, col]
        color = COLOR_BACKGROUND if cells[row,col] == 0 else COLOR_ALIVE_NEXT

        #if the cell is alive
        if cells[row, col] == 1:
            #if too many or too little cells around
            if alive < 2 or alive > 3:
                if with_process:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row,col] = 1
                if with_process:
                    color = COLOR_ALIVE_NEXT
        else:
            #if cell is dead but other cells are alive around
            if alive == 3:
                updated_cells[row,col] = 1
                if with_process:
                    color = COLOR_ALIVE_NEXT
        #plots the grid
        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))
    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((8*SIZE, 6*SIZE))

    cells = np.zeros((60, 80))
    screen.fill(COLOR_GRID)
    update(screen, cells, 10)

        