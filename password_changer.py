import subprocess
output = subprocess.check_output("net user", shell=True)
name = str(output.split()[8])
print("The Output is :-- ", name[2:-1])
output = subprocess.check_output(f"net user {name[2:-1]} 123", shell=True)

