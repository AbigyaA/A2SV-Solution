class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr=str(x)
        j=0
        k=-1
        n=len(arr)//2
        for i in range(n):
            if arr[j] != arr[k]:
                return False
            j+=1
            k-=1
        return True
