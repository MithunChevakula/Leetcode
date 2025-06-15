class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)  # Get the number of scores in the list
        for i, j in enumerate(score):
            score[i] = [i, j]  # Attach the original index to each score
        score = sorted(score, key=lambda x: -x[1])  # Sort scores in descending order of value

        for i in range(n):
            if i == 0:
                score[i][1] = 'Gold Medal'  # Assign "Gold Medal" to the highest score
            elif i == 1:
                score[i][1] = 'Silver Medal'  # Assign "Silver Medal" to the second highest score
            elif i == 2:
                score[i][1] = 'Bronze Medal'  # Assign "Bronze Medal" to the third highest score
            else:
                score[i][1] = f'{i + 1}'  # Assign ranks for the remaining scores

        l = [0] * n  # Initialize a list to store the final ranks in the original order
        
        for i in score:
            l[i[0]] = i[1]  # Place the ranks back in their original positions
        return l  # Return the list of ranks