# duplex-scanpy
A basic quick and dirty python tool to merge together a batch scan of duplex printed documents with a GUI. 

## How To Use
1. Scan the front sides of all documents (via document feeder) as individual PDFs
2. Flip documents over and scan again (via document feeder) as individual PDFs
3. Run the duplex-scanpy app (if using release) or run main.py (if using source code)

**In GUI:**

4. Select all the files created via scanning
5. Enter the amount of sides each individual document had (Should always be even as even the blank backsides were scanned)
6. Choose the output location for the files that will be generated
7. Enter a prefix that will added before each generated file (ex: "scan_" will produce "scan_01.pdf")
8. Click "Start Generating Files"
9. Enjoy your generated files in the output directory you chose
