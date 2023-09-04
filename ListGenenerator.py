import random

class ListGenerator:
    def __init__(self, list_size=None):
        if list_size is None or not isinstance(list_size, int):
            self.list_size = 1
            print("You must enter an integer for list_size.")
        elif list_size < 2:
            self.list_size = 2  # Minimum size set to 2
            print("The quantity of numbers must be at least 2.")
        else:
            self.list_size = list_size

    def generate(self, target_sum=None):
        if target_sum is None or not isinstance(target_sum, int):
            self.target_sum = random.randint(1, 50)
            print("You must enter an integer for target_sum.")
        else:
            self.target_sum = target_sum
        numbers_of = random.randint(2, 50) if  self.list_size < 2 else self.list_size 
        numbers = [random.randint(1, 50) for _ in range(numbers_of)]
        return numbers, self.target_sum

    def __str__(self):
        return f"ListSize: {self.list_size}, TargetSum: {self.target_sum}"

if __name__ == '__main__':
    get = ListGenerator()  # You can specify the list size here
    numbers, target_sum = get.generate()
    print(f"Generated Numbers: {numbers}")
    print(f"Target Sum: {target_sum}")
