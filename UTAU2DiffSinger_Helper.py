import subprocess
import sys

def run_script(script_name):
    """Runs the specified Python script."""
    try:
        subprocess.run(["python", script_name], check=True)
        print(f"Script '{script_name}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running script '{script_name}': {e}")

def install_pandas():
    """Installs the Pandas library using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
        print("Pandas installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing pandas: {e}")

def main():
    """Prompts the user and runs the selected scripts."""

    try:
        import pandas  # Check if pandas is already installed
        print("Pandas is already installed.")
    except ImportError:
        print("Pandas not found. Installing...")
        install_pandas()

    choice = input("Do you want to convert filenames from Hiragana to Romaji and/or remove any unneeded files? (y/n): ")
    if choice.lower() == "y":
        run_script(r"scripts\Hiragana2Romaji.py")

    choice = input("Do you want to write transcription files for your recordings? (y/n): ")
    if choice.lower() == "y":
        run_script(r"scripts\Gen_Trans.py")

if __name__ == "__main__":
    main()
