def can_form_triangle(height, red, blue):
    needed_balls = 0
    for i in range(1, height + 1):
        if i % 2 == 1:
            needed_balls += i
            red -= i
        else:
            needed_balls += i
            blue -= i
        if red < 0 or blue < 0:
            return False
    return True
class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        total_balls = red + blue
        max_height = 0
        while (max_height + 1) * (max_height + 2) // 2 <= total_balls:
            max_height += 1
        
        for height in range(max_height, 0, -1):
            if can_form_triangle(height, red, blue) or can_form_triangle(height, blue, red):
                return height

        return 0

