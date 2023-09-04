import random
def find_pairs_with_sum(numbers, target_sum):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                pairs.append((numbers[i], numbers[j]))
    
    return pairs

if __name__ == '__main__':
    while True:
        try:
            max_len = int(input("Enter the quantity/number of numbers to evaluate: "))
                
            if max_len < 2:
                raise ValueError("The quantity of numbers must be at least 2.")
        
            
            numbers_of = random.randint(2, max_len)
            numbers = [random.randint(2, max_len) for x in range(numbers_of)]
            print(f"Generated {numbers_of} random numbers: {numbers}")
            
            target_sum = int(input("Enter the sum to search for: "))
            result = find_pairs_with_sum(numbers, target_sum)
            if not isinstance(target_sum, int):
                print( "You must enter an integer.")
            if result:
                print("Pairs that sum up to the target:")
                for pair in result:
                    print(pair)
                break
            else:
                print("No pairs found that sum up to the target.")
        except ValueError as e:
            print( "You must enter an integer.")
            print(f"Error: {e}")
    
    