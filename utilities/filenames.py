from time import time

def get_upload_file_name(folder, instance=None, filename=None):
    if not filename:
        return f"{folder}"
    return f"{folder}/{str(time()).replace('.','_')}_{filename}"