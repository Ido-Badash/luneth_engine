"""
Space Station Manager - Main Entry Point
"""

import pygame
import sys

# Uncomment when backend/frontend are implemented
# from backend.core.game_state import GameState
# from frontend.core.renderer import Renderer
# from frontend.core.input_handler import InputHandler
# from frontend.views.side_view import SideView

from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, COLOR_BACKGROUND


def main():
    """Main game loop"""
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Station Manager")
    clock = pygame.time.Clock()
    
    # TODO: Initialize game systems
    # game_state = GameState()
    # view = SideView()
    # renderer = Renderer(view)
    # input_handler = InputHandler(view)
    
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # TODO: Handle input
            # command = input_handler.handle_event(event, game_state)
            # if command:
            #     game_state.execute_command(command)
        
        # Update game logic
        # TODO: game_state.update(dt)
        
        # Render
        screen.fill(COLOR_BACKGROUND)
        # TODO: renderer.render(screen, game_state)
        
        # Temporary placeholder text
        font = pygame.font.Font(None, 48)
        text = font.render("Space Station Manager", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
