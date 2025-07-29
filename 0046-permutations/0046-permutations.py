class Solution:
    def solve(self, idx: int, nums: List[int], result: List[List[int]]) -> None:
        n = len(nums)
        if idx == n:
            result.append(nums[:])          # append a copy (snapshot)
            return

        for i in range(idx, n):
            nums[idx], nums[i] = nums[i], nums[idx]   # choose
            self.solve(idx + 1, nums, result)         # explore
            nums[idx], nums[i] = nums[i], nums[idx]   # un-choose (backtrack)

    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        self.solve(0, nums, result)
        return result