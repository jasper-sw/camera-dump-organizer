import os


# a class to organize a "camera dump" folder full of different files and filetypes into appropriate subfolders
class Organizer:
    directory_path: str
    all_files = []
    file_types = []

    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.find_files()

    def find_files(self):
        # find all files, add to directory
        for file in os.listdir(self.directory_path):
            self.all_files.append(file)
            # here we assume that filenames will NOT contain . as a character for anything other than to denote file
            #   extension. If they do then this totally breaks. Luckily most cameras do not use periods in their
            #   default naming schemes
            filename, file_extension = file.split(".")
            if file_extension not in self.file_types:
                self.file_types.append(file_extension)
        print(self.all_files)
        print(self.file_types)
        print("")

    def create_type_folders(self):
        pass

    def move_files(self):
        pass


org = Organizer(r"C:\Users\18jsw\Desktop\christmas eve eve")

