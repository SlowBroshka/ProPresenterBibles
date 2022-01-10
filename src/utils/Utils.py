import os

from pathlib import Path


class Utils:

    @staticmethod
    def clean_dir(path: str):
        [f.unlink() for f in Path(path).glob('*') if f.is_file()]

    @staticmethod
    def prep_path(dest_folder_name: str) -> str:
        cwd = os.getcwd()
        res_path = os.path.join(cwd, dest_folder_name)
        Path(res_path).mkdir(parents=True, exist_ok=True)
        
        Utils.clean_dir(res_path)
        return res_path
