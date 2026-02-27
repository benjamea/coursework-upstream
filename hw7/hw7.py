"""
CMSC 14100
Winter 2026
Homework #7

We will be using anonymous grading, so please do NOT include your name
in this file.

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

class File:
    def __init__(self, name, contents):
        """
        Construct a File object with four attributes:
            name (str): The name of the file
            __contents (private str): The contents of the file
            is_open (bool): Whether the file is open or not
            size (int): The size of the file in number of characters

        Args:
            name (str): The name of the file
            contents (str): The contents of the file
        """
        self.name = name
        self.__contents = contents
        self.is_open = False
        self.size = len(contents)

    def open_file(self):
        """ Open the file. """
        self.is_open = True

    def close_file(self):
        """ Close the file. """
        self.is_open = False

    def cat(self):
        """ Returns (str): The contents of a file. """
        return self.__contents

    def redirect(self, input):
        """
        Add input to the end of a file. A file must be open to add to it.

        Args:
            input (str): The input to add to the file

        Returns (bool): True if input was successfully added, False
            otherwise.
        """
        if not self.is_open:
            return False
        self.__contents += input
        self.size = len(self.__contents)
        return True

    def diff(self, other):
        """
        Create a string that represents the difference between the contents
            of two files.

        Args:
            other (File): the file to compare to

        Returns: (string) difference between two files.
        """
        assert isinstance(other, File), "A file can only be diff'd with another file"
        result = ""
        c1 = self.__contents
        c2 = other.__contents
        length = max(len(c1), len(c2))
        for i in range(length):
            if i >= len(c1) or i >= len(c2):
                result += "-"
            elif c1[i] == c2[i]:
                result += c1[i]
            else:
                result += "-"
        return result


class Directory:
    def __init__(self, name):
        """
        Construct a Directory with two attributes:
            name (str): The name of the directory
            files (dict[str, File]): A dictionary that maps file names to
                files in the directory

        Args:
            name (str): The name of the directory
        """
        self.name = name
        self.files = {}

    def add_file(self, f):
        """
        Add a file to the directory. File names in a directory
            can't be repeated.

        Args:
            f (File): the file to add
        """
        assert isinstance(f, File), "Only files can be stored in a directory"
        assert f.name not in self.files, "File names in a directory can't be repeated"

        self.files[f.name] = f

    def touch(self, file_name, contents, replace):
        """
        Create a new file.

        Files in a directory must have unique names.

        Args:
            file_name (str): The name of the file to create
            contents (str): The contents of the file
            replace (bool): Whether or not to replace an existing file with
                with a new file

        Returns (bool): True if new file was successfully created, False
            otherwise.
        """
        if file_name in self.files and not replace:
            return False
        self.files[file_name] = File(file_name, contents)
        return True


class FileSystem:
    def __init__(self):
        """
        Construct a FileSystem with one attribute:
            dirs (dict[str, Directory]): A dictionary that maps directory names
                to directories in the file system
        """
        self.dirs = {}

    def add_directory(self, d):
        """
        Add a directory to the file system. Directory names in a file system
            can't be repeated.

        Args:
            d (Directory): the directory to add
        """
        assert isinstance(d, Directory), \
            "Only directories can be stored in a file system"
        assert d.name not in self.dirs, \
            "Directory names in a file system can't be repeated"
        self.dirs[d.name] = d

    def ls(self):
        """
        Create a list of all file names in the file system.

        Returns (list of str): A list of file names, sorted.
        """
        result = []
        for dir_name, directory in self.dirs.items():
            for file_name in directory.files:
                result.append(dir_name + "/" + file_name)
        return sorted(result)

    def cp(self, file_name, origin_dir, destination_dir):
        """
        Copy a file from one directory to another.

        Args:
            file_name (str): the name of the file
            origin_dir (str): the name of the directory
            destination_dir (str): the name

        Returns (bool): True if successful, False otherwise.
        """
        if origin_dir not in self.dirs or destination_dir not in self.dirs:
            return False
        if file_name not in self.dirs[origin_dir].files:
            return False
        original = self.dirs[origin_dir].files[file_name]
        new_file = File(file_name, original.cat())
        self.dirs[destination_dir].files[file_name] = new_file
        return True