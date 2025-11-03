# Master script for other python scripts from current folder
import argparse, sys, importlib

def main():
    parser = argparse.ArgumentParser(description="Master script for osctl python scripts")
    parser.add_argument("command", choices=["sysinfo", "config_manager", "execute", "save_settings"], help="Specify which script to run")

    args, remaining = parser.parse_known_args()

    module_map = {
        "sysinfo": "sysinfo",
        "config_manager": "config_manager",
        "execute": "execute",
        "save_settings": "save_settings"
    }

    module_name = module_map[args.command]
    mod = importlib.import_module(module_name)

    sys.argv = [sys.argv[0]] + remaining
    mod.main()

if __name__ == "__main__":
    main()
