import sys, os, json, argparse

parser = argparse.ArgumentParser(description="Manage environment variables")
subparser = parser.add_subparsers(dest="command", required=True)
set_parser = subparser.add_parser("set", help="Set an environment variable")
set_parser.add_argument("key", help="Environment variable name to set   ")
set_parser.add_argument("value", help="Environment variable value to set")

get_parser = subparser.add_parser("get", help="Get an environment variable")
get_parser.add_argument("key", help="Environment variable name to get")

list_parser = subparser.add_parser("list", help="List all environment variables")
reset_parser = subparser.add_parser("reset", help="Reset environment variables to default")

args = parser.parse_args()

# Below code commented as have already collected env vars in json file
# env_vars = {}
# for key, value in os.environ.items():
#     env_vars[key] = value
# with open("data/env_var.json", "w") as f:
#     json.dump(env_vars, f, indent=4)

with open("data/env_var.json", "r") as f:
    env_vars = json.load(f)

if args.command == "set":
    print(f"Set {args.key} to {args.value}")
    env_vars[args.key] = args.value
    with open("data/env_var.json", "w") as f:
        json.dump(env_vars, f, indent=4)

if args.command == "get":
    print(env_vars.get(args.key, f"{args.key} not found"))

if args.command == "list":
    for key, value in env_vars.items():
        print(f"{key}={value}")

if args.command == "reset":
    env_vars.clear()
    for key, value in os.environ.items():
        env_vars[key] = value
    with open("data/env_var.json", "w") as f:
        json.dump(env_vars, f, indent=4)
    print("Reset all environment variables")
