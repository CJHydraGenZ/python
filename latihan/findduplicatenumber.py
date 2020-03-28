
def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    prt1 = nums[0]
    prt2 = tortoise

    while prt1 != prt2:
        prt1 = nums[prt1]
        prt2 = nums[prt2]
    return prt1


print(findDuplicate([3, 1, 3, 4, 2]))
