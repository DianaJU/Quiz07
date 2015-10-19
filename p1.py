def main():
    distance()

def distance( x1 , y1 , x2 , y2):
    from math import sqrt
    result = sqrt((x2 - x1) ** 2 + (y2 -y1) ** 2)
    return (result)

print(dist(23,3,43,5))
if __name__ == "main": main()
