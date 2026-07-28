#Import
import subprocess, sys


#Command class
class Object:
    def __init__(self):
        self.file_name: str = input("Please enter the file you wish to export:\n")
        self.cmd = ["sudo", "find", "/", "-iname", f"*{self.file_name}*"]
        
    def command(self):
            output = subprocess.run(
                self.cmd,
                capture_output=True,
                text=True
            )
            file_list = output.stdout.splitlines()
            file_dict = {}
            for i in range(0, len(file_list)):
                print(f"{i + 1}: {file_list[i]}")
                file_dict[i + 1] = file_list[i]
            if len(file_list) <= 0:
                print("File could not be found. Please try again.\n\n\n\n\n\n")
                self.command()
            try:
                index = int(input(f"\nThis is what was found based on your search keyword.\nPlease input the index that is correct.\n"))
                self.object_path = file_dict[index]
            except Exception as e:
                    print("Invalid input, please try again.\n\n\n\n\n\n")
                    self.command()
    
class File(Object):
    def __init__(self):
        super().__init__()
        self.extension: str = ""
        
    def the_type(self, usr_input) -> None:
        if usr_input.lower() == "yes":
            self.type = "-type"
            file_type_input = input("Please enter the file type: d for directory other wise enter the extension .txt .py .md etc:\n")
            if file_type_input == "d":
                self.file_type = "d"
            else:
                self.file_type = "f"
                self.extension = file_type_input
            self.cmd.insert(2, self.type)
            self.cmd.insert(3, self.file_type)

class Directory(Object):
    def __init__(self):
        super().__init__()
        self.type: str = "type"
        self.file_type: str = "d"
        self.cmd.insert(2, self.type)
        self.cmd.insert(3, self.file_type)