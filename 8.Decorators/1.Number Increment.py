def number_increment(nums):
    def increase():
        return [num +1 for num in nums]
    return increase()

print(number_increment([1,2,3]))