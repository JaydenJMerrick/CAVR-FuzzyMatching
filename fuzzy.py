import pandas as pd

def getUnionName(file_path):
    with open(file_path, 'r') as f:
        union_name = f.readline().strip()
    
    print(f"Building Name is here: {union_name.split(',')[0]}")
    return union_name

def getData(file_path):
    df = pd.read_csv(file_path,skiprows=3);
    columns_to_keep = [col for col in df.columns if not col.startswith('Unnamed:')]
    df = df[columns_to_keep]
    print(df.head())
    
def main():
    path_input = input("What is the file path?: ");
    union_name = getUnionName(path_input)
    getData(path_input)
    
# (This code only runs when the file is executed directly)
if __name__ == "__main__":
    main()

