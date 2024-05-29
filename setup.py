import sys
import os

def setup():
    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the absolute path of the project's root directory
    project_root = os.path.abspath(os.path.join(current_dir, "src"))

    # Add the project's root directory to sys.path
    sys.path.append(project_root)

if __name__ == "__main__":
    setup()
