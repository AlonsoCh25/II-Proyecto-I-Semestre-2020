import csv
import pygame

class csv_class:
    def __init__(self, archive, method):
        self.archive = self.read(archive, method)

    #return th matrix in the csv
    def read(self, archive, method):
        f = open(archive, method)
        data = csv.reader(f)
        data = [row for row in data]
        #Deleteth empy spaces in the matrix
        for i in data:
            if i == []:
                data.remove(i)
        return data

    #Modify th variable matrix
    def write(self, matrix):
        self.archive = matrix

    #return th matrix in the csv
    def get_matrix(self):
        return self.archive

    #Update the csv with the variable matrix
    def update_matrix(self, archive, method):
        a = self.archive
        f = open(archive, method)
        with f:
            writer = csv.writer(f)
            writer.writerows(a)

#load the csv
archive_csv = csv_class("ScoreBoard.csv","rt")
matrix_csv = archive_csv.get_matrix()

"""For write matrix in the variable"""
# archivo_csv.write("Nueva matriz")
"""For save the matrix in the csv"""
# archivo_csv.update_matriz("matriz.csv","w")
"""NOTE"""
#Firts write the variable and after save the matrix in the csv

#Class for know the position of the cursor
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0,0,1,1)
    def update(self):
        self.left, self.top = pygame.mouse.get_pos()

#Class for create the buttons, require tho images for animation
class Button(pygame.sprite.Sprite):
    def __init__(self, image1, image2, x, y):
        self.image_normal = image1
        self.image_select = image2
        self.image_current = self.image_normal
        self.rect = self.image_current.get_rect()
        self.rect.left, self.rect.top = (x,y)
    def update(self, screen, cursor):
        if cursor.colliderect(self.rect):
            self.image_current = self.image_select
        else:
            self.image_current = self.image_normal
        screen.blit(self.image_current, self.rect)

