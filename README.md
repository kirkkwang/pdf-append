# PDF Append

A really easy to use Python script that effectively appends a PDF page, like a copyright disclaimer or something to that effect, at the end of another PDF.

Dependencies include Python 3.x and the PyPDF2 library.
https://pypi.org/project/PyPDF2/

Big thanks to Mike Driscoll's post at https://realpython.com/pdf-python/ for doing all the heavy lifting.

All I did was wrap a iterater around it so it will work for a folder of PDFs and not just one.

### Instructions

Either clone the repo or if you don't use Git, just click on the green `Code` dropdown menu on the GitHub repo and choose `Download ZIP` (or just use this link:
https://github.com/kirkkwang/pdf-append/archive/refs/heads/main.zip) and unzip the file somewhere on your computer.

If you don't already have it, download and install Python 3.x (whatever Python 3 version should work) from https://www.python.org/downloads/.

Once that is installed, open Terminal (Mac) or Command Prompt (Windows) and pip install the PyPDF2 library with the `pip3 install pypdf2` command.

Place the PDFs that you want to process in the `folder_of_pdfs_to_process` folder. It should work for one file or a batch of files.

Place the PDF you want to append in the `folder_with_pdf_to_append` folder and rename that file `pdf_to_be_appended.pdf`. There should only be one file here. I've added a dummy file in there to be replaced by your file.

NOTE: If you want to keep your own filename then feel free to change it in the code. In a future version I will make it work regardless of the name of the PDF, just that no more than one PDF needs to be in there.

The `output` folder is where all the processed files will end up. The filenames of the new files will have the exact same filename as the original. Your original files will not be altered or moved.

In the Terminal or Command Prompt, `cd` over to the folder containing `pdf-append.py` and use the command `python3 pdf-append.py`.

That's it! Open the `output` folder and you should see your files.

NOTE: This has only been tested with regular PDFs, not PDF/A or any other format with security features.
