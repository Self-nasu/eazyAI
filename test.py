import pandas as pd
import numpy as np

def gen_data():
    print("=" * 67)
    print("                      DATA SET GENERATOR                      ")
    print("=" * 67)
    
    while True:
        try:
            no_of_attrs = int(input("Number of attributes you want: "))
            no_of_rows = int(input("Number of rows to generate: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    data_dict = {}
    
    for i in range(no_of_attrs):
        print(f"\n---------- Attribute No. {i + 1} Details ----------\n")
        name = input("Enter the name of the attribute: ")
        
        while True:
            try:
                LRange = int(input("Enter lower limit range: "))
                URange = int(input("Enter upper limit range: "))
                
                if LRange < URange:
                    break
                else:
                    print("Upper limit must be greater than lower limit. Please try again.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        data_dict[name] = np.random.randint(LRange, URange, size=no_of_rows)
    
    print("\nSuccessfully Generated Your Data.\n")
    
    data = pd.DataFrame(data_dict)
    name_of_file = input("Enter file name (e.g., 'example.csv'): ")
    
    data.to_csv(name_of_file, index=False)
    print(f"\n{name_of_file} File Saved Successfully.")

gen_data()
