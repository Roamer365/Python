import subprocess, argparse, sys

parser=argparse.ArgumentParser(description="Choose the application to launch")
parser.add_argument("-g","--gedit",action="store_true", help="Launch xterm")
parser.add_argument("-f","--firefox",action="store_true",help="Launch firefox")
parser.add_argument("-t","--terminal",action="store_true",help="Launch Gnome Terminal")

args=parser.parse_args()
result=""
if (len(sys.argv) == 1) or (len(sys.argv) > 2):
    parser.print_usage()
    sys.exit(1)
try:
    if sys.argv[1] == "--gedit" or sys.argv[1] == "-g":
        result=subprocess.run("gedit", stderr=subprocess.PIPE, stdout=subprocess.PIPE, check=True,text=True)
    elif sys.argv[1] == "--firefox" or sys.argv[1] == "-f":
        result=subprocess.run("firefox", stderr=subprocess.PIPE, stdout=subprocess.PIPE, check=True,text=True)
    elif sys.argv[1] == "--terminal" or sys.argv[1] == "-t":
        result=subprocess.run("gnome-terminal", stderr=subprocess.PIPE, stdout=subprocess.PIPE, check=True,text=True)
    else:
        parser.print_usage()
except FileNotFoundError:
    print("Command does not exist.")
except subprocess.CalledProcessError as e:
    print(f"Command failed with an exit code {e.returncode}")

print(f"Stdout: {result.stdout}")
print(f"stderr: {result.stderr}")
print("End of function")