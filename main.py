def twosum(self,nums,target):
    check = 0
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                check = 1
                return [i,j]
                break
        if check:
            break
        
         