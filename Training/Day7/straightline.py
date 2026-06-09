# You are given an integer array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.
def checkStraightLine(coordinates):
        x0,y0=coordinates[0]
        x1,y1=coordinates[1]
        dx=x1-x0
        dy=y1-y0
        for i in range(2,len(coordinates)):
            if dy * (coordinates[i][0] - x0) != dx * (coordinates[i][1] - y0):
                return False
        return True

print(checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))