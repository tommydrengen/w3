import csv
import re
output=""

# Define the pattern to match numbers with a comma as the decimal separator (e.g., '299,99')
pattern = re.compile(r'(\d+),(\d{2})')
with (open("source_data.csv", "r", newline='') as inFile,open('destination_data.csv', 'w', newline='') as outFile):
    # Read first line as header
    #firstLine = inFile.readline()
    #firstLine = firstLine.strip('\n')
    #firstLine = firstLine.strip('\r')
    firstLine = inFile.readline().strip()
    colNames = firstLine.split(',')
    print(f"Header Columns: {colNames}")
    #firstLine = firstLine.trim()
    print(f"Header colums: {colNames}")
    # Write the header to the output file
    outFile.write(firstLine + '\n')

    # Process the remaining lines in the input file
    currentLine = ""
    while (currentLine := inFile.readline().strip()):
        # Split the current line by commas to extract individual fields
        lineContent = currentLine.split(',')
        # Check for empty records (i.e., lines like ',,,')
        if all(field == '' for field in lineContent):
            print("Skipping empty record...")
            continue  # Skip this iteration if the line is empty
        # Check if the line has the correct number of columns (same as the header)
        if len(lineContent) == len(colNames):
            purchase_amount = lineContent[-1]
            if pattern.search(purchase_amount):
                # Replace the comma in the decimal part with a period
                purchase_amount = pattern.sub(r'\1.\2', purchase_amount)
                lineContent[-1] = purchase_amount
            # Write the modified content to the output file
            outFile.write(','.join(lineContent) + '\n')
        # Optionally print the current line to see the process
        print(f"Processed Line: {lineContent}")

pass
