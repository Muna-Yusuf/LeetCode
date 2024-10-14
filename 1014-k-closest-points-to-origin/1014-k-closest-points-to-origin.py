class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances = []
        for point in points:
            x, y = point
            distance = x**2 + y**2
            distances.append((distance, point))

        distances.sort(key=lambda x: x[0])
        close_points = [point for _, point in distances[:k]]
        return [list(poi) for poi in close_points]
            
        