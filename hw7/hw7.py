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
        raise ValueError("Not implemented")

    def open_file(self):
        """ Open the file. """
        raise ValueError("Not implemented")

    def close_file(self):
        """ Close the file. """
        raise ValueError("Not implemented")

    def cat(self):
        """ Returns (str): The contents of a file. """
        raise ValueError("Not implemented")

    def redirect(self, input):
        """
        Add input to the end of a file. A file must be open to add to it.

        Args:
            input (str): The input to add to the file

        Returns (bool): True if input was successfully added, False
            otherwise.
        """
        raise ValueError("Not implemented")

    def diff(self, other):
        """
        Create a string that represents the difference between the contents
            of two files.

        Args:
            other (File): the file to compare to

        Returns: (string) difference between two files.
        """
        assert isinstance(other, File), "A file can only be diff'd with another file"
        raise ValueError("Not implemented")

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
        raise ValueError("Not implemented")

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
        raise ValueError("Not implemented")

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
        raise ValueError("Not implemented")

    def cp(self, file_name, origin_dir, destination_dir):
        """
        Copy a file from one directory to another.

        Args:
            file_name (str): the name of the file
            origin_dir (str): the name of the directory
            destination_dir (str): the name

        Returns (bool): True if successful, False otherwise.
        """
        raise ValueError("Not implemented")
