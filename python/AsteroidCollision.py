# Runtime: 81ms
# Memory: 17.90MB

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if (not stack or stack[-1] < 0) or asteroid > 0:
                stack.append(asteroid)
                continue

            while stack:
                if stack[-1] < 0:
                    stack.append(asteroid)
                    break
                if stack[-1] > 0 and stack[-1] > abs(asteroid):
                    break
                if stack[-1] > 0 and stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                stack.pop()
            else:
                stack = [asteroid]
            
        return stack
