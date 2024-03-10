def write_to_file(filename, file_content):
    print("Writing extracted text into file\n")
    f = open(filename, "w")
    f.write(file_content)
    f.close()