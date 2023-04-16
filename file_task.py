import os
from os.path import join


UNPROCESSED_FOLDER: str = "unprocessed"
PROCESSED_FOLDER: str = "processed"
OUTPUT_FOLDER: str = "output"


def file_task(lines: list[str]) -> str:
    """ Process a list of lines and return the result

    Args:
        lines (list[str]): A list of lines to process

    Returns:
        str: The processed lines
    """
    return "\n".join(lines)


class FileTask:
    """ A class to process files in a folder """

    def __init__(self, folder: str) -> None:
        """ Initialize the class

        Args:
            folder (str): The folder to process
        """
        self.folder = folder

        os.makedirs(join(self.folder, UNPROCESSED_FOLDER), exist_ok=True)
        os.makedirs(join(self.folder, PROCESSED_FOLDER), exist_ok=True)
        os.makedirs(join(self.folder, OUTPUT_FOLDER), exist_ok=True)

    def get_files(self) -> list[str]:
        """ Get a list of files in the unprocessed folder

        Returns:
            list[str]: A list of files in the unprocessed folder
        """
        return os.listdir(self.folder)

    def process_file(self, file_name: str) -> None:
        """ Process a file and move it to the processed folder

        Args:
            file_name (str): The name of the file to process

        Returns:
            None
        """
        file_path = join(self.folder, UNPROCESSED_FOLDER, file_name)
        f = open(file_path)
        lines = f.readlines()
        new_content = file_task(lines)

        f.close()

        # Move processed file to processed folder
        os.rename(file_path, join(self.folder, PROCESSED_FOLDER, file_name))

        f = open(join(self.folder, OUTPUT_FOLDER, file_name), "w")
        f.write(new_content)
        f.close()

