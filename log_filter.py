# read the file
# ERROR WARNING INFO SUCCESS 3rd word in the line

inFile = open("app_log.txt", "r")
outFile = open("filtered_log.txt", "w")

#input = inFile.readline() # read all lines into a list
output = ""
for line in inFile:
    if "ERROR" in line: # write (append) to filtered_log
        output = output + line + "\n"
    if "WARNING" in line: # write (append) to filtered_log
        output = output + line + "\n"
outFile.writelines(output)
inFile.close() # close resource
outFile.close() # close resource