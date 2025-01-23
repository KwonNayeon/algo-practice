"""
Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Time Complexity: O(n)
Space Complexity: O(1)

Problem Summary:
1. Area Formula:
 area = distance between pillars × min(height1, height2)
2. Key Points for Maximum Area:
 - Longer distance between pillars is better
 - Higher pillars are better
 - The shorter pillar determines the water height
"""

class Solution:
   def maxArea(self, height: List[int]) -> int:
       max_area = 0
       s, e = 0, len(height) - 1
       while s < e:
           area = (e - s) * min(height[s], height[e])
           max_area = max(area, max_area)
           if height[s] < height[e]:
               s += 1
           else:
               e -= 1
       return max_area
