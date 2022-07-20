output_file = open("outputFile.txt", "w")
with open("inputFile.txt", "r") as beingread:
    output_file.write(beingread.read())
output_file.close()
print(output_file)