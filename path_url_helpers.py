import os



def segment_after_last_slash(path):
    return path.rsplit('/',1)[1]



def get_extension(path_and_name):
    fileName, fileExtension = os.path.splitext(path_and_name)

    result = fileExtension

    return result