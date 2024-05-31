import pygame
class Boat(pygame.sprite.Sprite):
    def __init__(self, type):
        self.following = False
        self.xpos = 0
        self.ypos = 0
        super().__init__()
        if type == 'aircraft':
            imported = pygame.image.load('graphics/aircraftboat.png').convert_alpha()
            surface = pygame.transform.rotozoom(imported, 0, 0.5)
            surface_rot = pygame.transform.rotozoom(surface, 90, 1)
            self.rot = [surface, surface_rot]
            self.rot_index = 0
            self.length = 5
            self.image = self.rot[self.rot_index]
            self.rect = self.image.get_rect(center = (580, 160))
            self.default = (580, 160)
        elif type == 'destroyer':
            imported = pygame.image.load('graphics/destroyerboat.png').convert_alpha()
            surface = pygame.transform.rotozoom(imported, 0, 0.4)
            surface_rot = pygame.transform.rotozoom(surface, 90, 1)
            self.rot = [surface, surface_rot]
            self.rot_index = 0
            self.length = 4
            self.image =  self.rot[self.rot_index]
            self.rect = self.image.get_rect(center = (580, 260))
            self.default = (580, 260)
        elif type == 'cruiseboat':
            imported = pygame.image.load('graphics/cruiserboat.png').convert_alpha()
            surface = pygame.transform.rotozoom(imported, 0, 0.5)
            surface_rot = pygame.transform.rotozoom(surface, 90, 1)
            self.rot = [surface, surface_rot]
            self.rot_index = 0
            self.length = 3
            self.image =  self.rot[self.rot_index]
            self.rect = self.image.get_rect(center = (780, 160))
            self.default = (780, 160)
        elif type == 'submarine':
            imported = pygame.image.load('graphics/submarineboat.png').convert_alpha()
            surface = pygame.transform.rotozoom(imported, 0, 0.5)
            surface_rot = pygame.transform.rotozoom(surface, 90, 1)
            self.rot = [surface, surface_rot]
            self.rot_index = 0
            self.length = 3
            self.image =  self.rot[self.rot_index]
            self.rect = self.image.get_rect(center = (780, 260))
            self.default = (780, 260)
        elif type == 'gunboat':
            imported = pygame.image.load('graphics/gunboat.png').convert_alpha()
            surface = pygame.transform.rotozoom(imported, 0, 0.5)
            surface_rot = pygame.transform.rotozoom(surface, 90, 1)
            self.rot = [surface, surface_rot]
            self.rot_index = 0
            self.length = 2
            self.image =  self.rot[self.rot_index]
            self.rect = self.image.get_rect(center = (680, 360))
            self.default = (680, 360)
    def is_clicked(self):
        if self.following == False and self.xpos == 0 and self.ypos == 0:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                self.following = True
    def movement(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.following:
            self.rect.center = mouse_pos
            self.image.set_alpha(128)
        else: 
           self.image.set_alpha(255)
    def set_rect(self, new_rect):
        self.rect = new_rect
    def update(self):
        self.is_clicked()
        self.movement()


  
  
