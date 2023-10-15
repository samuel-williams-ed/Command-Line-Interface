# sys module allows command line arguments
import sys
import subprocess
# argparse sets flags (that can be passed as arguments)
import argparse


def git_init():
    subprocess.run(['git', 'init'])

def git_status():
    subprocess.run(['git', 'status'])

def git_add_all():
    subprocess.run(['git', 'add', '.'])
    git_status()
    print("All changes staged")

def main():

    # Create instance of an ArgumentParser object which can hold flags as properties
    argumentParser = argparse.ArgumentParser(description="A few quality of life improvements for the CLI.")

    # Possible flags
    argumentParser.add_argument("-n", "--name", default="User", help="Give a name to print at lion_CLI initialisation.")
    argumentParser.add_argument("--age", help="Give an age you'd like to be displayed in the CLI")
    argumentParser.add_argument("gst", help="Get the Git repository status")

    # Parse the flags
    args = argumentParser.parse_args()

    # Execute at initialisation
    print(f"Hello, {args.name}")

    # flag conditionals 
    if args.age:
        print(f"My records show you are {args.age} years old.")

    if args.gst:
        git_status()
        addOption = input("Would you like to add all? \n ('y' for yes | 'n' for no | 'q' for exit ) \n")
        if addOption == "y":
            git_add_all()
        elif addOption == 'n':
            print("Which file would you like to add?")
            # TODO: complete adding logic


    
# call the main() function when script is run directly.
if __name__=="__main__":
    main()