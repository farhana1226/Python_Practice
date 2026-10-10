#STORE FREQUENCY IN DICTIONARY
#.................METHOD-01..................

nums=[1,6,8,5,7,2,6,5,4,1,1,0,2,3,6,5,4,8,5,1,4,8,8,8,5]
frequency_map={}
for i in range (len(nums)):
    if nums[i] in frequency_map:
        frequency_map[nums[i]] += 1
    else:
        frequency_map[nums[i]] = 1
print(frequency_map)


#....................METHOD-02 ....................

nums=[1,6,8,5,7,2,6,5,4,1,1,0,2,3,6,5,4,8,5,1,4,8,8,8,5]
frequency_map={}
n=len(nums)
for i in range(0,n):
    frequency_map[nums[i]]=frequency_map.get(nums[i],0)+1
print(frequency_map)


