class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        w = sum(arr[:k])
        c = 0
        if w/k>=threshold:
            c+=1
        
        for i in range(k,len(arr)):
            w += arr[i] - arr[i-k]
            if w/k >= threshold:
                c+=1
        return c