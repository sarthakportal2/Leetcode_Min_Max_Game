class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        #T(C(N)==O(N*2)) and S(C(N)==O(N)) as it requires contigous memory allocation iteratievly at each allocated pos.
        while len(nums)>1:#Iterating through nums's End length 
            newnums=[]#NewNums's Array Initialzing
            for i in range(0,len(nums)//2):#Iterating through Nums's Initial Indx even Length  
                if i%2==0:newnums.append(min(nums[2*i],nums[2*i+1]))#Even Minimum Indx Value Calculation 
                else:newnums.append(max(nums[2*i],nums[2*i+1]))#odd Minimum Indx Value Calculation 
            nums=newnums#Swapping the Min. and Max elemenal Val to newNums
        return nums[0]#Printing Output appended elements from Initial Val
