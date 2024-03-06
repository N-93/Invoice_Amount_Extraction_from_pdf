import PyPDF2

def pdf_extract(file_path):
# Open the PDF file
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)

        # Get the number of pages in the PDF
        num_pages = len(reader.pages)
        #print("Number of pages:", num_pages)

        # Access specific pages if needed
        # For example, to access the first page and extract text
        first_page = reader.pages[4]
        text = first_page.extract_text()


        list1 = []
        j=1
        for i in range(num_pages):
            page = reader.pages[i]
            text = page.extract_text()

            text_list = text.split('\n')
        # for solving problem for seperating name ie 'karun' and 'shrestra' seperates into two different elements

            if text_list[11] != '₨':
                text_list[10] = text_list[10] + ' ' + text_list[11]
                text_list.pop(11)

            if text_list[19] == '-':
                text_list[19] = text_list[19] +text_list[21]


            #print(text_list)
            if text_list[19]!='0.00' and text_list[10]!= '0.00' :
                a = text_list[10]  # this is the name


                list1.append(j)
                list1.append(a)   # this is for the name
                list1.append(text_list[19])     #this is for the amount
                #print(j,text_list[10],text_list[19])
            j+=1
        return(list1)







    