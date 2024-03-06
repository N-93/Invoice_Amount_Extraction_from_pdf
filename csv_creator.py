import pandas as pd



def convert_csv(data_list):
    column_names = [
    "Page no",
    "Names",
    "Amount"
    ]
    
    

    file_name ='good_pdf_data.csv'

    df = pd.DataFrame(data_list, columns = column_names)
    df.to_csv(file_name, index=False)

    print(f"File created Sucessfully as '{file_name}'. ")

