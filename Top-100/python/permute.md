# Explanation:
Backtracking Function: The backtrack function is defined to generate permutations by building them incrementally and exploring all possible choices.

# Base Case:
If the length of the current path (path) equals the length of nums, it means we have a complete permutation. We add a copy of the current path to the result list.

# Recursive Exploration:
We iterate over each element in nums.
For each element, we check if it is already included in the current path. If it is, we skip it to avoid duplicates.
If the element is not in the current path, we include it and recursively call backtrack with the updated path.
After the recursive call, we backtrack by removing the last element added to the path. This allows us to explore other possibilities.

# Result Collection: The result list collects all valid permutations of the input array.
This approach ensures that we explore all possible permutations of the input array while avoiding duplicates by checking if an element is already included in the current path. The constraints (with nums.length up to 6) make this approach feasible within reasonable time limits.