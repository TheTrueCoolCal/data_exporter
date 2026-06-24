#add type hint, make code cleaner, add try/exsept block 

#Import
import subprocess
import sys

#Files being exported
files: list[str] = []

#File search function
def file_searcher(file_type, name, extension=None):
    while True:
        output = subprocess.run(f"sudo find / -name *{name}*", shell=True, capture_output=True)
        cleaned_output = output.stdout.decode()
        if len(cleaned_output) > 0:
            output_list = cleaned_output.split("\n")
            for i in range(0, len(output_list) - 1):
                print(f"{i + 1}: {output_list[i]}")
            output_index = input(f"\n\nThese are the {file_type}s found based on your search keyword.\nPlease input the {file_type} index that is correct. Or select 0 to search for a diffrent file. Or exit to close the program.\n")
            if output_index.lower() == "exit":
                sys.exit()
            try:
                output_index_int = int(output_index)
            except Exception as e:
                    print("Invalid input, please try again.\n\n\n\n\n\n")
                    continue
            if output_index == "0":
                return 0, 0
            output_index_int -= 1
            return output_index_int, output_list
        else:
            failed = input("File could not be found. Would you like to try again? Yes or No:")
            while 1:
                if failed.lower() == "yes":
                    break
                elif failed.lower() == "no":
                    sys.exit()
                else:
                    print("Input not regonized please try again.")
                    continue
            continue
                    

#File search
def file_search():
    while True:
        #File being exported
        file_name = input("Please enter the file you wish to export:\n")
        type = input("Would you like to spesify a file type? Yes, No ")
        if type.lower() == "yes":
            file_type = input("Please enter the file type: 0 for folder other wise enter the extension .txt .py .md etc")
            file_index, file_list = file_searcher("file", file_name, file_type)
        file_index, file_list = file_searcher("file", file_name)
        if file_index == 0:
            continue

        #Export location
        export = input("Where would you like to export to? Please provide the full path.\n") 
        export_locations, export_list = file_searcher("export location", export)
        if export_locations == 0:
            continue
        subprocess.run(f"sudo cp {file_list[file_index]} {export_list[export_locations]}", shell=True)
        while True:
            loop = input("Your file has been exported. Do you wish to export another? Type Yes to export another or No to close the program.\n")
            if loop.lower() == "yes":
                break
            elif loop.lower() == "no":
                sys.exit()
            else:
                print("Input unregonized. Please try again.")
                continue
                