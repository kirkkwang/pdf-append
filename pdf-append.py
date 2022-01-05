from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

# for reference and thanks to: https://realpython.com/pdf-python/
# dependencies are Python3x and PyPDF2
    # goto https://www.python.org/downloads/ to download Python
    # in terminal or command prompt, run 'pip3 install pypdf2'
    # the folder structures are preset but feel free to change if desired
    # see below for more instructions

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()
    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output, 'wb') as out:
        pdf_writer.write(out)

def list_of_files(directory, pdf_to_append, dir_of_output):
    for file in Path(directory).iterdir():
        if file.is_file() and file.suffix == '.pdf':
            merged_file = f'{dir_of_output}{file.stem}.pdf'
            merge_pdfs([str(file), pdf_to_append], merged_file)
            print(f'New file created: {merged_file}')


def filename_of_pdf_to_append(directory):
    count = 0
    for file in Path(directory).iterdir():
        if file.is_file() and file.suffix == '.pdf':
            count+=1
            if count > 1:
                return "There are more than one PDF in ./folder_with_pdf_to_append"
            else:
                return file


if __name__ == '__main__':
    
    ### MORE INSTRUCTIONS ###

    # put all the PDFs that need to be proccessed in './folder_of_pdfs_to_process/'
    folder_with_pdfs = './folder_of_pdfs_to_process/'

    # put the PDF to be appended in './folder_with_pdf_to_append/'
    pdf_file_to_append = str(filename_of_pdf_to_append('./folder_with_pdf_to_append'))

    # all the proccessed files will apprear in './output/'
    output_folder = './output/'

    list_of_files(folder_with_pdfs, pdf_file_to_append, output_folder)

# to run the file, make sure all files are in place and open terminal (on Mac) or command prompt (on Windows) # and navigate to the folder which this file is contained and type 'python3 pdf-append.py'