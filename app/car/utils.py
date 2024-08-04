import pygame


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)

def line_intersection(p1, p2, p3, p4):
    """
    Находит точку пересечения двух отрезков (p1p2 и p3p4).
    :param p1: Кортеж (x1, y1) - начальная точка первого отрезка
    :param p2: Кортеж (x2, y2) - конечная точка первого отрезка
    :param p3: Кортеж (x3, y3) - начальная точка второго отрезка
    :param p4: Кортеж (x4, y4) - конечная точка второго отрезка
    :return: Кортеж (x, y) - точка пересечения, если отрезки пересекаются, иначе None
    """
    
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
    
    def sub(a, b):
        return (a[0] - b[0], a[1] - b[1])
    
    def add(a, b):
        return (a[0] + b[0], a[1] + b[1])
    
    # Определяем векторы и их детерминанты
    r = sub(p2, p1)
    s = sub(p4, p3)
    d = det(r, s)
    
    if d == 0:
        # Параллельные линии
        return None
    
    # Расстояния до пересечения
    u = det(sub(p3, p1), s) / d
    v = det(sub(p3, p1), r) / d
    
    # Проверяем, находится ли точка пересечения в пределах обоих отрезков
    if 0 <= u <= 1 and 0 <= v <= 1:
        intersection = add(p1, (u * r[0], u * r[1]))
        return intersection
    else:
        return None

import math

def line_circle_intersection(px1, py1, px2, py2, cx, cy, r, vector_len):
    """
    Найти точки пересечения отрезка и окружности.
    
    :param px1: x-координата начала отрезка
    :param py1: y-координата начала отрезка
    :param px2: x-координата конца отрезка
    :param py2: y-координата конца отрезка
    :param cx: x-координата центра окружности
    :param cy: y-координата центра окружности
    :param r: радиус окружности
    :return: список кортежей с точками пересечения или пустой список, если пересечений нет
    """

    if calculate_line_length(px1, py1, cx, cy) > vector_len + 100: return None
    
    # Переменные для расчетов
    dx = px2 - px1
    dy = py2 - py1
    A = dx**2 + dy**2
    B = 2 * (dx * (px1 - cx) + dy * (py1 - cy))
    C = (px1 - cx)**2 + (py1 - cy)**2 - r**2
    
    discriminant = B**2 - 4 * A * C
    
    if discriminant < 0:
        # Нет пересечений
        return []
    
    discriminant = math.sqrt(discriminant)
    
    # Вычисление параметров t1 и t2
    t1 = (-B - discriminant) / (2 * A)
    t2 = (-B + discriminant) / (2 * A)
    
    # Находим точки пересечения
    points = []
    
    if 0 <= t1 <= 1:
        x1 = px1 + t1 * dx
        y1 = py1 + t1 * dy
        return (x1, y1)
        
    if 0 <= t2 <= 1 and t2 != t1:
        x2 = px1 + t2 * dx
        y2 = py1 + t2 * dy
        return (x2, y2)
    
    return None


def calculate_line_length(x1, y1, x2, y2):
    """
    Вычисляет длину отрезка между двумя точками в двумерном пространстве.

    :param x1: x-координата первой точки
    :param y1: y-координата первой точки
    :param x2: x-координата второй точки
    :param y2: y-координата второй точки
    :return: длина отрезка
    """
    # Вычисляем разности координат
    dx = x2 - x1
    dy = y2 - y1
    
    # Применяем формулу для расчета длины
    length = math.sqrt(dx**2 + dy**2)
    
    return length

# def create_line_mask(start_pos, end_pos, thickness):
#     # Найдите размер поверхности для маски
#     width = abs(end_pos[0] - start_pos[0]) + thickness
#     height = abs(end_pos[1] - start_pos[1]) + thickness
    
#     # Создайте поверхность с прозрачным фоном
#     line_surface = pygame.Surface((width, height), pygame.SRCALPHA)
#     line_surface.fill((0, 0, 0, 0))  # Прозрачный фон
    
#     # Нарисуйте линию на поверхности
#     pygame.draw.line(line_surface, (0, 0, 0), (start_pos[0], start_pos[1]), (end_pos[0], end_pos[1]), thickness)
    
#     # Создайте маску из поверхности
#     line_mask = pygame.mask.from_surface(line_surface)
#     line_mask.get_at
    
#     return line_surface, line_mask

