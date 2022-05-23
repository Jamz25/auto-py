import pygame

class Game:
    
    def __init__(self, windowSize, title):
        
        self.windowSize = windowSize
        self.windowTitle = title
    

    def start(self):
    
        pygame.init()
        self.screen = pygame.display.set_mode(self.windowSize)
        pygame.display.set_caption(self.windowTitle)

        self._game_loop()


    def _game_loop(self):

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen.fill(0)

            # Drawing

            pygame.display.update()
        
        pygame.quit()
