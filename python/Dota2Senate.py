# Runtime: 52ms
# Memory: 17.02 MB

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        n = len(senate)
        
        rStack, dStack = deque(), deque()
        for i, c in enumerate(senate):
            if c == "R":
                rStack.append(i)
            else:
                dStack.append(i)
        while rStack and dStack:
            currR = rStack.popleft()
            currD = dStack.popleft()

            if currR < currD:
                rStack.append(currD + n)
            else:
                dStack.append(currR + n)
        
        return "Radiant" if rStack else "Dire"



        # my solution
        # senate = list(senate)

        # def __get_ban_idx(target_senator, senator_idx, senate):
        #     for idx in range(senator_idx + 1, len(senate)):
        #         if senate[idx] == target_senator:
        #             return idx
        #         else:
        #             pass
        #     else:
        #         if target_senator in senate:
        #             return senate.index(target_senator)
        #         else:
        #             return -1


        # while senate.count("R") != 0 and senate.count("D") != 0:
        #     for idx, senator in enumerate(senate):
        #         if senator == "D":
        #             ban_idx = __get_ban_idx("R", idx, senate)
        #             if ban_idx < 0:
        #                 break
        #             else:
        #                 senate[ban_idx] = "r"
                    
        #         elif senator == "R":
        #             ban_idx = __get_ban_idx("D", idx, senate)
        #             if ban_idx < 0:
        #                 break
        #             else:
        #                 senate[ban_idx] = "d"
                    
        #     senate = list(filter(lambda x: x.isupper(), senate))

        # if senate[0] == 'R':
        #     return 'Radiant'
        # else:
        #     return 'Dire'
