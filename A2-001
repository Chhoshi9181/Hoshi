# Claude AI generates this code.

def solve():
    # Read input
    N, M = map(int, input().split())
    red_points = [0] + list(map(int, input().split()))
    blue_points = [0] + list(map(int, input().split()))
    
    # Generate line segments for both beams
    red_segments = []
    blue_segments = []
    
    # For red beam
    for i in range(N):
        x1, y1 = red_points[i], i % 2  # Alternating between bottom (0) and top (1)
        x2, y2 = red_points[i+1], (i+1) % 2
        red_segments.append((x1, y1, x2, y2))
    
    # For blue beam
    for i in range(M):
        x1, y1 = blue_points[i], i % 2  # Alternating between bottom (0) and top (1)
        x2, y2 = blue_points[i+1], (i+1) % 2
        blue_segments.append((x1, y1, x2, y2))
    
    # Count intersections
    count = 0
    
    # Track intersections we've already counted
    counted_intersections = set()
    
    # Check all pairs of segments
    for r_idx, r_seg in enumerate(red_segments):
        for b_idx, b_seg in enumerate(blue_segments):
            # Check if segments intersect
            intersection = find_intersection(r_seg, b_seg)
            if intersection:
                x, y = intersection
                # Only count each unique intersection point once
                if (x, y) not in counted_intersections:
                    counted_intersections.add((x, y))
                    count += 1
    
    return count

def find_intersection(seg1, seg2):
    x1, y1, x2, y2 = seg1
    x3, y3, x4, y4 = seg2
    
    # Check if lines are parallel
    denominator = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denominator == 0:
        # Lines are parallel
        return None
    
    # Calculate intersection point
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denominator
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denominator
    
    # Check if intersection point is on both segments
    if 0 <= ua <= 1 and 0 <= ub <= 1:
        x = x1 + ua * (x2 - x1)
        y = y1 + ua * (y2 - y1)
        return (x, y)
    
    return None

if __name__ == "__main__":
    print(solve())
