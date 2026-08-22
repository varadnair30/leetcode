class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        '''
        sort the array
        declare res[] and append [intervals[0][0],intervals[0][1]]
        loop thru the intervals [] and then if res[-1][1]>intervals[i][0] and res[-1][1]<intervals[i][1] , 
        then reaplce [res[-1][1]=intervals[i+1][1] 

        else res.append([intervals[i][0],intervals[i][1]]) 
        '''

        intervals.sort()
        res=[[intervals[0][0],intervals[0][1]]]

        for i in range(1,len(intervals)):
            if res[-1][1]>=intervals[i][0]:
                res[-1][1]=max(res[-1][1],intervals[i][1])

            else:
                res.append([intervals[i][0],intervals[i][1]])


        return res
                

        