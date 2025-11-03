import subprocess, argparse, os, sys, logging
from datetime import datetime

def main():
    parser=argparse.ArgumentParser(description="Choose the application to launch")
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-g","--gedit",action="store_true", help="Launch gedit")
    group.add_argument("-f","--firefox",action="store_true",help="Launch firefox")
    group.add_argument("-t","--terminal",action="store_true",help="Launch Gnome Terminal")
    group.add_argument("-s","--script", help="Launch the script",type=str)
    group.add_argument("-n","--network", action="store_true", help="Show network device status")

    args=parser.parse_args()

    logging.basicConfig(filename="data/launcher.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    logger=logging.getLogger(__name__)

    if args.gedit:
        command=["gedit"]
    elif args.firefox:
        command=["firefox"]
    elif args.terminal:
        command=["xterm"]
    elif args.script:
        if not os.path.isfile(args.script):
            print(f"{args.script} does not exist")
            sys.exit(1)
        command=["bash", args.script]
    elif args.network:
        command=["nmcli", "device", "status"]
    try:
        with open("data/launcher.log","a+") as f:
            f.write(datetime.now().astimezone().strftime('%a, %d %b %Y %H:%M:%S %z'))
            f.write(f"\tExecuting the switch {command[0]}\n")
            f.close()
        result=subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, preexec_fn=os.setsid,text=True)
        stdout, stderr = result.communicate()
        if stdout:
            logger.info(stdout)
        if stderr:
            logger.error(stderr)
    except FileNotFoundError:
        print("Command does not exist.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with an exit code {e.returncode}")
        sys.exit(1)
    # time.sleep(4)
    result.kill()
    result.wait()

if __name__ == "__main__":
    main()