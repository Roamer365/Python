import json, argparse, sys

def main():
    f = open("data/settings.json","w+")
    parser=argparse.ArgumentParser(description="Command line tool for managing settings.")

    parser.add_argument("-b", "--brightness", help="Set brightness level", type=int)


    args=parser.parse_args()
    if (len(sys.argv) == 1):
        parser.print_usage()
        sys.exit(1)

    json.dump(vars(args), f, indent=4) 

    f.seek(0)

    print(f.read())

if __name__ == "__main__":
    main()