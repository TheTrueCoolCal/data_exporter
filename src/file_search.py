#add type hint, make code cleaner, add try/except block 

#Import
import subprocess, sys

#Files being exported
files: list[str] = []

#sys.exit function
def sys_exit(input):
    if input == 0:
        sys.exit(0)

#File search function
def file_searcher(file_name, type="", file_type="", extension="") -> tuple[int, list[str]]:
    while True:
        command = [f"sudo", "find", "/", type, file_type, "-iname", f"*{file_name}*{extension}"]
        output = subprocess.run(command, shell=False, capture_output=True)
        cleaned_output = output.stdout.decode()
        if len(cleaned_output) > 0:
            file_list = cleaned_output.split("\n")
            for i in range(0, len(file_list) - 1):
                print(f"{i + 1}: {file_list[i]}")
            output_index = input(f"\nThese are the files found based on your search keyword.\nPlease input the file index that is correct.\n")
            sys_exit(output_index)
            try:
                file_index = int(output_index)
            except Exception as e:
                    print("Invalid input, please try again.\n\n\n\n\n\n")
                    continue
            file_index -= 1
            return file_index, file_list
        else:
            while 1:
                failed = input("File could not be found. Would you like to try again? Yes or No:")
                if failed.lower() == "yes":
                    return 1, 1
                elif failed.lower() == "no":
                    sys.exit()
                else:
                    print("Input not regonized please try again.")
                continue
        
                    

#File search
def file_search():
    while 1:
        #File being exported
        file_name: str = input("Please enter the file you wish to export:\n")
        sys_exit(file_name)
        type: str = input("Would you like to spesify a file type? Yes, No\n")
        sys_exit(type)
        if type.lower() == "yes":
            extension: str = input("Please enter the file type: 1 for folder other wise enter the extension .txt .py .md etc:\n")
            sys_exit(extension)
            if extension == 1:
                type, file_type = "-type" "d"
                file_index, file_list = file_searcher(file_name, type, file_type)
            else:
                type = "-type"
                file_type = "f"
                file_index, file_list = file_searcher(file_name, type, file_type, extension)
        file_index, file_list = file_searcher(file_name)
        if file_index and file_list == 1:
            continue
        

        #Export location
        export = input("Where would you like to export to? Please provide the full path.\n") 
        export_locations, export_list = file_searcher(export, "-type", "d")
        command = ["sudo", "cp", f"{file_list[file_index]}", f"{export_list[export_locations]}"]
        subprocess.run(command)
        while True:
            loop = input("Your file has been exported. Do you wish to export another? Type Yes to export another or No to close the program.\n")
            if loop.lower() == "yes":
                break
            elif loop.lower() == "no":
                sys.exit()
            else:
                print("Input unregonized. Please try again.")
                continue
