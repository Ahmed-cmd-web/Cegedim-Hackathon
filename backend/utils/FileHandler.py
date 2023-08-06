import dataclasses
from django.core.files.uploadedfile import InMemoryUploadedFile
from typing import Optional
import os
import tempfile

@dataclasses.dataclass(frozen=True)
class FileHandler:
    file:InMemoryUploadedFile
    temp_file_name:Optional[str]

    def create_temp_file(self)->None:
        '''
        This method creates a temporary file locally to simplify
        dealing with files.
        '''
        target=open(self.temp_file_name,'wb+')
        for chunk in self.file.open().chunks():
            target.write(chunk)
        target.close()

    def delete_file(self)->bool:
        try:
            os.remove(self.temp_file_name)
            return True
        except FileNotFoundError:
            return False