def get_red_tiles(filename):
    with open(filename, 'r') as f:
        return [list(map(int, digits.strip().split(','))) for digits in f]

def get_max_rectangle(redTiles):
    maxArea = 0
    for i1 in range(len(redTiles)):
        for i2 in range(i1 + 1, len(redTiles)):
            tile1 = redTiles[i1]
            tile2 = redTiles[i2]
            dx = tile2[0] - tile1[0]
            dy = tile2[1] - tile1[1]
            if dx != 0 and dy != 0:
                area = (abs(dx) + 1) * (abs(dy) + 1)
                if area > maxArea:
                    maxArea = area
    return maxArea

def is_point_inside_or_on_boundary(x_check, y_check, redTiles):
    intersections=0

    for i in range(len(redTiles)):
        x1, y1 = redTiles[i]
        x2, y2 = redTiles[(i + 1) % len(redTiles)]
        
        if x1 == x2 == x_check:
            if min(y1, y2) <= y_check <= max(y1, y2): 
                return True

        if y1 == y2 == y_check:
            if min(x1, x2) <= x_check <= max(x1, x2): 
                return True
            
        if x1 == x2:
            if min(y1, y2) <= y_check <= max(y1, y2):
                if x1 > x_check:
                    intersections += 1

    return intersections % 2 == 1

def boundary_intersects_rectangle(rx1, ry1, rx2, ry2, redTiles):
    rectMinX, rectMaxX = min(rx1, rx2), max(rx1, rx2)
    rectMinY, rectMaxY = min(ry1, ry2), max(ry1, ry2)

    for i in range(len(redTiles)):
        p1 = redTiles[i]
        p2 = redTiles[(i + 1) % len(redTiles)]
        
        x1, y1 = p1
        x2, y2 = p2
        
        if x1 == x2:
            yMin, yMax = min(y1, y2), max(y1, y2)
            
            if rectMinX < x1 < rectMaxX:
                overlapStart = max(yMin, rectMinY)
                overlapEnd = min(yMax, rectMaxY)
                
                if overlapStart < overlapEnd:
                    return True

        elif y1 == y2:
            xMin, xMax = min(x1, x2), max(x1, x2)
            
            if rectMinY < y1 < rectMaxY:
                overlap_start = max(xMin, rectMinX)
                overlap_end = min(xMax, rectMaxX)
                
                if overlap_start < overlap_end:
                    return True 
                    
    return False

def get_max_inter_rectangle(redTiles):
    maxArea = 0
    
    for i1 in range(len(redTiles)):
        for i2 in range(i1 + 1, len(redTiles)):
            x1, y1 = redTiles[i1]
            x2, y2 = redTiles[i2]
            
            dx = x2 - x1
            dy = y2 - y1

            if dx != 0 and dy != 0:
                c3x, c3y = x1, y2
                c4x, c4y = x2, y1
                
                if is_point_inside_or_on_boundary(c3x, c3y, redTiles) and is_point_inside_or_on_boundary(c4x, c4y, redTiles):
                    
                    if not boundary_intersects_rectangle(x1, y1, x2, y2, redTiles):
                        area = (abs(dx) + 1) * (abs(dy) + 1)
                        if area > maxArea:
                            maxArea = area

    return maxArea

def main():
    redTiles = get_red_tiles('day 9/red_tiles.txt')
    print(get_max_rectangle(redTiles))
    print(get_max_inter_rectangle(redTiles))

if __name__ == '__main__':
    main()