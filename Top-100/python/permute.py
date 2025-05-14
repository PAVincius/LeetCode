class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            if len(path) == len(nums):
                # If the current permutation is complete, add it to the result
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in path:
                    # Skip if the number is already in the current permutation
                    continue
                
                # Include the number in the current permutation and recurse
                path.append(nums[i])
                backtrack(path)
                # Backtrack: remove the last number to explore other possibilities
                path.pop()
        
        result = []
        backtrack([])
        return result