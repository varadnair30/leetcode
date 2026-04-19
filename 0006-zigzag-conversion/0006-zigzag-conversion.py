class Solution:
    def convert(self, s: str, nums: int) -> str:

        if nums==1 or nums==len(s):
            return s

        rows=['']*nums

        current_row,step=0,1

        for char in s:
            rows[current_row] += char
            if current_row==0:
                step=1
            elif current_row==nums-1:
                step=-1

            current_row+=step

        return ''.join(rows)


        