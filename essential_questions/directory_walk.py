def print_directory_contents(sPath, indent=1):
    """
    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your
    ability to work with nested structures.
    """
    import os
    for child in os.listdir(sPath):
        child_path = os.path.join(sPath, child)
        if os.path.isfile(child_path):
            print('-' * indent + child_path)
        elif os.path.isdir(child_path):
            print('-' * indent + child_path)
            print_directory_contents(child_path, indent+1)

print_directory_contents("/Users/osharabi/Development/projects/personal/interviews/")
