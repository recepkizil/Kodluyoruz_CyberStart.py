import math

"""
Resimdeki formül:
d = √(x₂-x₁)²+(y₂-y₁)²

Öklid mesafesi, Öklid uzayındaki iki nokta arasındaki "sıradan" düz çizgi mesafesidir. Bu formül ile, düzlemde veya üç boyutlu uzayda iki nokta arasındaki mesafeyi bulabilirsiniz.

Göreviniz:

Python'da fonksiyonlar ve döngüler kavramlarını kullanarak, aşağıdaki işlemleri gerçekleştiren bir program yazmanız gerekmektedir:

Noktaların Tanımlanması:

‘points’ adında bir liste oluşturun. Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir. Örneğin, ‘(x, y)’ noktası bir demet ‘(x, y)’ olarak temsil edilecektir.

Öklid Mesafesi İçin Bir Fonksiyon Yazma:

‘euclideanDistance’ adında bir fonksiyon tanımlayın. Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir.

Mesafelerin Hesaplanması:

Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın. Bu mesafeleri ‘distances’ adında başka bir listede saklayın.

Minimum Mesafenin Bulunması:

‘distances’ listesinden minimum mesafeyi bulun ve yazdırın.
"""

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