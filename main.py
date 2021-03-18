# main.py
from PyPDF2 import PdfFileMerger
import os
import PySimpleGUI as sg

listOfFiles = []  # The list of all files produced by the scanner
documentLength = 0  # The document length in the batch scan
indexSigFig = 1  # How many digits are required to present index
outputFolder = ""  # Output folder for the merged pdfs
filenamePrefix = ""  # Prefix added to all filenames
documentCount = 0  # Amount of documents scanned


def merge_files(files, index):
    filename = filenamePrefix + str(index).zfill(indexSigFig)
    print(f"Merging document {filename} ...")
    merger = PdfFileMerger()

    for file in files:
        merger.append(file)

    output_location = os.path.join(outputFolder, filename + ".pdf")
    merger.write(output_location)
    merger.close()
    print(f"Added document {output_location}")


def split_batch(files):
    print("Splitting batch...")
    split_batch_files = []
    document_count = len(files) // 2
    front_sides = files[:document_count]
    back_sides = files[document_count:]

    for i in range(1, document_count + 1):
        current_batch = []
        for j in range(1, documentLength + 1):
            if j % 2 != 0:
                current_batch.append(front_sides.pop(0))
            else:
                current_batch.append(back_sides.pop(0))
        split_batch_files.append(current_batch)

    print("Finished splitting batch: ", split_batch_files)

    return split_batch_files


def select_files():
    layout = [
        [sg.Text("Welcome to Duplex Scanpy")],
        [sg.Text("Select scanned PDFs: "),
         sg.FilesBrowse(key="-SELECTED_PDFS-", file_types=(("PDFs", "*.pdf"), ("PDFs", "*.PDF")), target=(None, None))],
        [sg.Text("How many sides is each individual document?"),
         sg.Input(key="-DOC_LENGTH-")],
        [sg.Text("Where should generated files be saved?"),
         sg.FolderBrowse(key="-OUTPUT_LOCATION-", target=(None, None))],
        [sg.Text("What should be the file prefix?"),
         sg.Input(key="-FILE_PREFIX-")],
        [sg.Button('Start Generating Files')]
    ]

    window = sg.Window('Duplex Scanpy', layout)

    event, values = window.read()

    # Extract values
    global listOfFiles, documentLength, outputFolder, filenamePrefix, indexSigFig, documentCount
    listOfFiles = str(values["-SELECTED_PDFS-"]).split(";")
    print("Selected PDFs: ", listOfFiles)

    documentLength = int(values["-DOC_LENGTH-"])
    print("Document Length: ", documentLength)

    outputFolder = values["-OUTPUT_LOCATION-"]
    print("Output Location: ", outputFolder)

    filenamePrefix = values["-FILE_PREFIX-"]
    print("File Prefix: ", filenamePrefix)

    documentCount = len(listOfFiles) // documentLength
    indexSigFig = len(str(documentCount))
    print("Index SigFig: ", indexSigFig)

    # Close the window
    window.close()


select_files()
s_batch = split_batch(listOfFiles)

for i, batch in enumerate(s_batch):
    merge_files(batch, i)
