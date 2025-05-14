class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                # If the target is met, add the current combination to the result
                result.append(path)
                return
            if target < 0:
                # If the target is exceeded, stop exploring this path
                return
            
            # Explore further combinations with the current and subsequent candidates
            for i in range(start, len(candidates)):
                # Include the candidate in the current combination and recurse
                backtrack(i, target - candidates[i], path + [candidates[i]])
        
        result = []
        backtrack(0, target, [])
        return result