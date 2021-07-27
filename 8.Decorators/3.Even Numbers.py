def even_numbers(ref_func):
    def wrapper(nums):
        result = ref_func(nums)
        return [num for num in result if num % 2 == 0]
    return wrapper

@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
