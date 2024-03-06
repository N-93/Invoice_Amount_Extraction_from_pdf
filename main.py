from pdf_extractor import pdf_extract
from csv_creator import convert_csv


file_path = 'pdf_files\Partner Ledger2201-2400.pdf'

data = pdf_extract(file_path)
#print(data)
list_data = [str(item).replace(',', '') for item in data]
list_data = [list_data[i:i+3] for i in range(0, len(list_data), 3)]

print(list)
convert_csv(list_data)