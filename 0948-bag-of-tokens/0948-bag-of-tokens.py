class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        l, r = 0, len(tokens) - 1
        score = 0
        max_score = 0
        
        while l <= r:
            # Play smallest token face up if possible
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                max_score = max(max_score, score)
            
            # Otherwise, play largest token face down if we have score to spend
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            
            # No valid move left
            else:
                break
        
        return max_score
