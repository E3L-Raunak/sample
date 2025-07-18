def parse_numbers(numbers):
    if len(numbers) <= 10:
        return "Please provide more than 10 numbers."
    return [num for num in numbers if isinstance(num, (int, float))]

# Example usage
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parsed_numbers = parse_numbers(numbers_list)
print(parsed_numbers)