class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        o=[[]]
        for i in range(len(arr)+1):
            for j in range(i):
                o.append(arr[j:i])
        s=0
        for i in o:
            l=len(i)
            if l%2:
                s+=sum(i)
        return s
