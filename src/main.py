import os
import subprocess

def analyse_code(directory):
    # List Python files in the directory
    python_files = [file for file in os.listdir(directory) if file.endswith('.py')]

    if not python_files:
        print("No Python files found in the specified directory.")
        return

    # Analyze each Python file using pylint and flake8
    for file in python_files:
        print(f"Analyzing file: {file}")
        file_path = os.path.join(directory, file)

        # Run pylint
        print("\nRunning pylint...")
        pylint_command = f"pylint {file_path}"
        subprocess.run(pylint_command, shell=True)

        # Run flake8
        print("\nRunning flake8...")
        flake8_command = f"flake8 {file_path}"
        subprocess.run(flake8_command, shell=True)

if __name__ == "__main__":
    # Update the path to match your macOS directory structure
    directory = "/Users/guynehushtan/Documents/Coding/Instagram/insta-followers/src"
    analyse_code(directory)
