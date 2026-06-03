import pygame
import tkinter as tk
from tkinter import messagebox


def draw_bar(screen, x, y, width, height, label, current, max_value, color):
    """Draw a level/stat bar with label and values."""
    font_small = pygame.font.Font(None, 24)
    font_label = pygame.font.Font(None, 28)
    
    # Draw label
    label_text = font_label.render(label, True, (255, 255, 255))
    screen.blit(label_text, (x, y))
    
    # Draw background bar (dark)
    pygame.draw.rect(screen, (50, 50, 50), (x, y + 30, width, height))
    pygame.draw.rect(screen, (200, 200, 200), (x, y + 30, width, height), 2)
    
    # Draw filled portion
    fill_width = (current / max_value) * width if max_value > 0 else 0
    pygame.draw.rect(screen, color, (x, y + 30, fill_width, height))
    
    # Draw value text
    value_text = font_small.render(f'{current}/{max_value}', True, (255, 255, 255))
    screen.blit(value_text, (x + width + 10, y + 30))


def draw_character_sprite(screen, x, y, frame=0, color=(100, 200, 255)):
    """Draw a character sprite with round head, arms, and legs with animation."""
    import math
    
    # Bobbing motion
    bob_offset = math.sin(frame * 0.1) * 5
    y_pos = y + bob_offset
    
    # Arm swing animation
    arm_swing = math.sin(frame * 0.15) * 8
    
    # Head (circle)
    head_radius = 20
    pygame.draw.circle(screen, color, (x, int(y_pos)), head_radius)
    pygame.draw.circle(screen, (255, 255, 255), (x, int(y_pos)), head_radius, 2)
    
    # Eyes
    pygame.draw.circle(screen, (255, 255, 255), (x - 8, int(y_pos) - 5), 3)
    pygame.draw.circle(screen, (255, 255, 255), (x + 8, int(y_pos) - 5), 3)
    
    # Body
    body_x = x
    body_y = int(y_pos) + 25
    body_width = 25
    body_height = 35
    pygame.draw.rect(screen, color, (body_x - body_width//2, body_y, body_width, body_height))
    pygame.draw.rect(screen, (255, 255, 255), (body_x - body_width//2, body_y, body_width, body_height), 2)
    
    # Left arm (swinging motion)
    left_shoulder_x = body_x - body_width//2
    left_shoulder_y = body_y + 8
    arm_length = 25
    left_hand_x = int(left_shoulder_x - arm_length + arm_swing)
    left_hand_y = int(left_shoulder_y + 10)
    pygame.draw.line(screen, color, (left_shoulder_x, left_shoulder_y), (left_hand_x, left_hand_y), 6)
    pygame.draw.circle(screen, color, (left_hand_x, left_hand_y), 6)  # Hand
    
    # Right arm (opposite swing)
    right_shoulder_x = body_x + body_width//2
    right_shoulder_y = body_y + 8
    right_hand_x = int(right_shoulder_x + arm_length - arm_swing)
    right_hand_y = int(right_shoulder_y + 10)
    pygame.draw.line(screen, color, (right_shoulder_x, right_shoulder_y), (right_hand_x, right_hand_y), 6)
    pygame.draw.circle(screen, color, (right_hand_x, right_hand_y), 6)  # Hand
    
    # Left leg
    left_leg_x = body_x - 8
    left_leg_y = body_y + body_height
    leg_length = 30
    pygame.draw.line(screen, color, (left_leg_x, left_leg_y), (left_leg_x, left_leg_y + leg_length), 6)
    pygame.draw.circle(screen, color, (left_leg_x, left_leg_y + leg_length), 6)  # Foot
    
    # Right leg
    right_leg_x = body_x + 8
    right_leg_y = body_y + body_height
    pygame.draw.line(screen, color, (right_leg_x, right_leg_y), (right_leg_x, right_leg_y + leg_length), 6)
    pygame.draw.circle(screen, color, (right_leg_x, right_leg_y + leg_length), 6)  # Foot


def draw_character(screen, name, strength, intelligence, charisma, health, max_health, mana, max_mana, experience, level, frame=0):
    font_title = pygame.font.Font(None, 44)
    name_text = font_title.render(name, True, (255, 215, 0))
    screen.blit(name_text, (50, 10))
    
    # Level display
    font_small = pygame.font.Font(None, 28)
    level_text = font_small.render(f'Level: {level}', True, (150, 150, 255))
    screen.blit(level_text, (50, 40))
    
    # Draw stat bars on the left
    bar_width = 180
    bar_height = 15
    
    # Core Stats
    draw_bar(screen, 50, 80, bar_width, bar_height, f'STR: {strength}', strength, 20, (255, 100, 100))
    draw_bar(screen, 50, 130, bar_width, bar_height, f'INT: {intelligence}', intelligence, 20, (100, 150, 255))
    draw_bar(screen, 50, 180, bar_width, bar_height, f'CHA: {charisma}', charisma, 20, (255, 150, 255))
    
    # Health bar
    draw_bar(screen, 50, 230, bar_width, bar_height, 'Health', health, max_health, (100, 255, 100))
    
    # Mana bar
    draw_bar(screen, 50, 280, bar_width, bar_height, 'Mana', mana, max_mana, (100, 200, 255))
    
    # Experience bar
    draw_bar(screen, 50, 330, bar_width, bar_height, 'Experience', experience, 100, (255, 200, 100))
    
    # Draw character sprite on the right side with animation
    draw_character_sprite(screen, 420, 200, frame, color=(100, 200, 255))

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 420))
    pygame.display.set_caption("RPG Character")

    name = "Hero"
    strength = 15
    intelligence = 12
    charisma = 14
    health = 85
    max_health = 100
    mana = 60
    max_mana = 75
    experience = 65
    level = 5
    
    frame = 0
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        draw_character(screen, name, strength, intelligence, charisma, health, max_health, mana, max_mana, experience, level, frame)
        pygame.display.flip()
        
        # Increment frame for animation
        frame += 1
        clock.tick(60)  # 60 FPS

    pygame.quit()


if __name__ == "__main__":
    main()



