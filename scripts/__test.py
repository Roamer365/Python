import os
import argparse
import json

parser = argparse.ArgumentParser(description="Manage environment variables")
subparser = parser.add_subparsers(dest="command", required=True)

# 'get' command
get_parser = subparser.add_parser("get", help="Get an environment variable")
get_parser.add_argument("var", help="Environment variable name to get")

# 'set' command
set_parser = subparser.add_parser("set", help="Set an environment variable")
set_parser.add_argument("var", help="Environment variable name to set")
set_parser.add_argument("value", help="Value to set for the environment variable")

args = parser.parse_args()

# Load environment into a dictionary
merged_data = dict(os.environ)
print(merged_data)

# Process commands
if args.command == "get":
    value = merged_data.get(args.var)
    if value is not None:
        print(f"{args.var} = {value}")
    else:
        print(f"{args.var} is not set.")
elif args.command == "set":
    merged_data[args.var] = args.value
    print(f"{args.var} set to {args.value}")
