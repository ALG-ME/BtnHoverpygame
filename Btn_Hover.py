import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, blur_radius):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False
        self.blur_radius = blur_radius

    def draw(self, window):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height:
            self.is_hovered = True
        else:
            self.is_hovered = False

        # Создаем поверхность для отображения кнопки с эффектом размытия
        button_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        if self.is_hovered:
            pygame.draw.rect(button_surface, self.hover_color, (0, 0, self.width, self.height), border_radius=10)
        else:
            pygame.draw.rect(button_surface, self.color, (0, 0, self.width, self.height), border_radius=10)

        # Применяем эффект размытия к поверхности с кнопкой
        button_blurred = button_surface.copy()
        button_blurred.fill((255, 255, 255, 50), special_flags=pygame.BLEND_RGBA_MULT)
        button_blurred.fill((0, 0, 0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        # Отображение эффекта размытия сзади кнопки
        window.blit(button_blurred, (self.x - self.blur_radius, self.y - self.blur_radius))

        # Отображение кнопки
        window.blit(button_surface, (self.x, self.y))

        # Отображение текста на кнопке
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        window.blit(text_surface, text_rect)

# Инициализация Pygame и создание экрана
pygame.init()
win_width = 800
win_height = 600
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Моя игра")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Создание кнопки с эффектом размытия
my_button = Button(100, 100, 200, 50, "Нажми меня", RED, GREEN, WHITE, 10)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    window.fill(WHITE)

    # Отображение кнопки
    my_button.draw(window)

    # Обновление экрана
    pygame.display.flip()

# Выход из игры
pygame.quit()
