#Runtime: 1205ms
#Memory: 39.46MB

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        potions_len = len(potions)

        for spell in spells:
            left, right = 0, potions_len-1

            while left <= right:
                mid = (left+right) // 2
                if (potions[mid] * spell) >= success:
                    right = mid - 1
                else:
                    left = mid + 1

            result.append(potions_len - left)
        
        return result




