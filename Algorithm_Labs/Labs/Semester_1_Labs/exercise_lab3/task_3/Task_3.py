import math

def distance_to_origin(point):
    return math.sqrt(point[0]**2 + point[1]**2)

def closest_points_to_origin(points, k):
    sorted_points = sorted(points, key=distance_to_origin)
    return sorted_points[:k]

# Считываем входные данные из файла
with open('input.txt', 'r') as f:
    n, k = map(int, f.readline().split())
    points = [list(map(int, f.readline().split())) for _ in range(n)]

# Находим K ближайших точек к началу координат
closest_points = closest_points_to_origin(points, k)

# Записываем результат в выходной файл
with open('output.txt', 'w') as f:
    f.write('[')
    for i, point in enumerate(closest_points):
        f.write(f'({point[0]}, {point[1]})')
        if i < k - 1:
            f.write(', ')
    f.write(']')
