import pandas as pd
from ListGenenerator import ListGenerator


class SaveList(ListGenerator):
    def save_list(self):
        numbersList, target = self.generate()
        print("Generated Numbers:", numbersList)
        print("Target Sum:", target)
        
        # Create a DataFrame
        df = pd.DataFrame({'Numbers': numbersList, 'TargetSum': target})
        
        # Save the DataFrame to a CSV file
        df.to_csv('list_numbers.csv', index=False)

if __name__ == '__main__':
    get = SaveList()  # You can specify the list size here
    get.save_list()
