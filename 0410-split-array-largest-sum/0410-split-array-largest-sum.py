class Solution:
    def func(self,arr,m):

        splt=1
        splt_ar=0

        for i in range(len(arr)):
            if splt_ar+arr[i] <=m:
                splt_ar+= arr[i]
            else:

                splt+=1
                splt_ar=arr[i]
        return splt

    def splitArray(self, arr: list[int], k: int) -> int:
        if k>len(arr): return -1

        low,high=max(arr),sum(arr)

        while low<=high:

            mid = (low+high)//2

            noStu = self.func(arr,mid)

            if noStu>k:
                low=mid+1
            else:
                high=mid-1
        return low





        