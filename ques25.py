# Python Programming Assignment-1
# 25. Write a program that copies the contents of one text file to another.
def copy_file(source_file, destination_file):
    try:
        with open("C:/Users/Yashank/Downloads/Harshi/demo1.txt", 'r') as src:
            contents = src.read()
        with open("C:/Users/Yashank/Downloads/Harshi/demo.txt", 'w') as dest:
            dest.write(contents)
        print(f"Contents copied from {source_file} to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"Error: The file {source_file} was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred. {e}")
copy_file("C:/Users/Yashank/Downloads/Harshi/demo1.txt", "C:/Users/Yashank/Downloads/Harshi/demo.txt")