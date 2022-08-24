import os
import sys
import hashlib


def rename_md5(full_path):
    md5_value = hashlib.md5(open(full_path, 'rb').read()).hexdigest()
    old_file_name = full_path.split('/', -1)[-1]
    extent_type = old_file_name.split('.', -1)[-1]
    v = f"-MD5:{md5_value}"
    new_file_name = old_file_name.split(f".{extent_type}")[0] + v + "." + extent_type
    new_file_full_path = full_path.split(old_file_name)[0] + new_file_name
    os.rename(full_path, new_file_full_path)


def check_name(full_path):
    md5_value = hashlib.md5(open(full_path, 'rb').read()).hexdigest()
    old_file_name = full_path.split('/', -1)[-1]
    if md5_value in old_file_name:
        return "Check True"
    return "Check False"
    
query = "{query}"
rename_md5(query)



