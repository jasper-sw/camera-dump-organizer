import os


# a class to organize a "camera dump" folder full of different files and filetypes into appropriate subfolders
class Organizer:
    directory_path: str
    all_files = []
    file_types = []

    def __init__(self, directory_path):
        self.directory_path = directory_path

    def organize(self):
        self.find_files()
        self.create_type_folders()
        self.move_files()

    def find_files(self):
        # find all files, add to directory
        for file in os.listdir(self.directory_path):
            # make sure we are looking at a file, not a folder or something else in the the current directory
            if os.path.isfile("{}\\{}".format(self.directory_path, file)):
                self.all_files.append(file)
                # here we assume that filenames will NOT contain . as a character for anything other than to denote file
                #   extension. If they do then this totally breaks. Luckily most cameras do not use periods in their
                #   default naming schemes
                filename, file_extension = file.split(".")
                if file_extension not in self.file_types:
                    self.file_types.append(file_extension)
        print("\nFound files: {}".format(self.all_files))
        print("\nFound file types: {}".format(self.file_types))

    def create_type_folders(self):
        print("\nCreating folders...")
        # ensure we are working in the correct directory
        os.chdir(self.directory_path)
        # create the file type folders
        for filetype in self.file_types:
            if not os.path.isdir("{}".format(filetype)):
                os.mkdir("{}".format(filetype))

    def move_files(self):
        print("\nMoving files...")
        # for each file
        for file in self.all_files:
            # get filename and type
            filename, file_extension = file.split(".")
            old_path = "{}\\{}".format(self.directory_path, file)
            # create new path for file in new dir
            new_path = "{}\\{}\\{}".format(self.directory_path, file_extension, file)
            # move file
            os.rename(old_path, new_path)
        print("All files moved successfully!")


org = Organizer(r"C:\Users\18jsw\Desktop\christmas eve eve")
org.organize()
