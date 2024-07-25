import math

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    pt = (x2 - x1)**2 + (y2 - y1)**2
    pt = math.sqrt(pt)
    return pt

def min_Dist(points, distances):
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distances.append(euclideanDistance(points[i], points[j]))
            minimum_distance = min(distances)
    print(f"Minimum mesafe: {minimum_distance:.2f}")

if __name__ == "__main__":
    points = [(12, 2), (1, 5), (8, 17), (8, 3), (7, 6)]
    distances = []
    min_Dist(points, distances)