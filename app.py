import pandas as pd 
import sys
import os
import random
from SaveList import SaveList 



def find_pairs_with_sum(numbers, target_sum):
    pairs = []
    seen = set()
    if os.path.exists('log.csv'):
        global data
        data = pd.read_csv('log.csv')
    else:
        new_log = pd.DataFrame(columns=['Numbers', 'Target Sum'])
        new_log.to_csv('log.csv', index=False)
    for num in numbers:
        complement = target_sum - num
        
        if complement in seen:
            pairs.append((complement, num))
        
        seen.add(num)
    if len(pairs) == 0:
        print("No pairs found that sum up to the target.")
    else:
        new_log = pd.Series({'Numbers': pairs, 'Target Sum': target_sum})
        data = data.append(new_log,ignore_index=True)
        data = pd.DataFrame(data)
        data.to_csv('log.csv', index=False)
    
    return pairs

if __name__=='__main__':
    
    if len(sys.argv) <= 1:
        generate = SaveList()
        generate.save_list()
        list = pd.read_csv('list_numbers.csv')
        listNumbers = list["Numbers"].tolist()
        target = list.iloc[1, list.columns.get_loc('TargetSum')]
        print(f"Use: The values and the target value will be taken from a file  \nthe target is: {target} \nand the numbers are: {listNumbers}.")
        pairs = find_pairs_with_sum(listNumbers, target)
        print(pairs)
        sys.exit(1)
    if len(sys.argv) == 3:
        try:
            numbers = [int(x) for x in sys.argv[1].split(",")]
            target_sum = int(sys.argv[2])
            pairs = find_pairs_with_sum(numbers, target_sum)
            print(pairs)
        except ValueError:
            print( "You must enter an integer.")
    
