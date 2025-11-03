from ast import main
import os, argparse, json

def main():
    parser=argparse.ArgumentParser(description="Manage environment variables")
    # group=parser.add_mutually_exclusive_group(required=True)
    subparser=parser.add_subparsers(dest="command", required=True)

    # get parsers
    get_parser=subparser.add_parser("get", help="Get an environment variable")
    get_parser.add_argument("var", help="Environment variable name to get")

    # set parsers
    set_parser=subparser.add_parser("set", help="Set an environment variable")
    set_parser.add_argument("var", help="Environment variable name to set")
    set_parser.add_argument("value", help="Value to set for the environment variable")


    merged_data={}
    for key, value in os.environ.items():
        merged_data[key]=value
        set_parser.add_argument("var", help=f"Set {key} environment variable")
        set_parser.add_argument("value", help=f"Set {value} environment variable")
        # group.add_argument("--"+key, help=f"Set {key} environment variable", type=str)

    with open("data/environment_variables.json", "w") as f:
        json.dump(merged_data, f, indent=4)

    #TODO: Will ask user to get/set the values
    args=parser.parse_args()
    for var, value in vars(args).items():
        if value:
            print(f"Setting {var} environment variable to: {value}")

    # parser=argparse.ArgumentParser(description="Manage environment variables")
    # with open("data/environment_variables.ndjson", "w+") as f:
    #     group=parser.add_mutually_exclusive_group(required=True)
    #     for key, value in os.environ.items():
    #         group.add_argument("-"+key, "--"+key, help=f"Set {key} environment variable", type=str)
    #         json.dump({key: value}, f)
    #         f.write("\n")
    #     f.close()
    # # parser.print_usage()
    # # parser.print_help()

    # #TODO: Add all env var as argument to this program and it will print help and ask user to get/set the values
    # merged_data={}
    # with open("data/environment_variables.ndjson", "r") as f:
    #     for line in f:
    #         if line.strip():
    #             print(line.strip() + "\n")
    #             merged_data.update(json.loads(line.strip()))
    # with open("data/environment_variables.json", "w") as f:
    #     json.dump(merged_data, f, indent=4)
    # with open("data/environment_variables.json", "r") as f:
    #     data=json.load(f)

if __name__ == "__main__":
    main()
