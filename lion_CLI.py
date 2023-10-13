# sys module allows command line arguments
import sys
# argparse allows flags to be used
import argparse

def main():

    # Create instance of an ArgumentParser object which can hold flags as properties
    flagHolder = argparse.ArgumentParser(description="A few quality of life improvements for the CLI.")

    # Possible flags
    flagHolder.add_argument("-n", "--name", default="User", help="Give a name to print at lion_CLI initialisation.")
    flagHolder.add_argument("--age", default="Unknown", help="Give an age you'd like to be displayed in the CLI")

    # Parse the flags
    args = flagHolder.parse_args()

    # Execute at initialisation
    print(f"Hello, {args.name}!")

    # flag conditionals 
    if(args.age):
        print(f"My records show you are {args.age} years old.")


# call the main() function when script is run directly.
if __name__=="__main__":
    main()