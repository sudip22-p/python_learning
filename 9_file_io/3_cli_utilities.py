import argparse

# Create the ArgumentParser object to handle command line inputs
parser = argparse.ArgumentParser(
    description="A simple CLI greeting tool with options to repeat and shout the greeting"
)

# Positional argument: mandatory input (name)
parser.add_argument("name", help="Your name (required positional argument)")

# Optional argument: custom greeting message, default is "Hello"
parser.add_argument(
    "--greeting", default="Hello", help="Greeting message to use (default: Hello)"
)

# Optional argument: number of times to repeat the greeting (integer)
parser.add_argument(
    "--times",
    type=int,
    default=1,
    help="Number of times to repeat the greeting (default: 1)",
)

# Optional boolean flag: if present, convert greeting to uppercase
parser.add_argument(
    "--shout",
    action="store_true",
    help="If set, convert the greeting message to uppercase",
)

# Parse the arguments provided in the command line
args = parser.parse_args()

# Generate the greeting message
message = f"{args.greeting}, {args.name}!"

# Convert to uppercase if --shout flag is used
if args.shout:
    message = message.upper()

# Print the greeting message the number of times specified by --times
for _ in range(args.times):
    print(message)

# python3 3_cli_utilities.py Sud
# Output: Hello, Sud!
# python3 3_cli_utilities.py Sud --greeting Hola
# Output: Hola, Sud!
# python3 3_cli_utilities.py Sud --times 3
# Output:
# Hello, Sud!
# Hello, Sud!
# Hello, Sud!
# python3 3_cli_utilities.py Sud --greeting Hey --times 2 --shout
# Output:
# HEY, Sud!
# HEY, Sud!
#  python3 3_cli_utilities.py Sud --greeting Hola --times 3 --shout
# HOLA, SUD!
# HOLA, SUD!
# HOLA, SUD!
