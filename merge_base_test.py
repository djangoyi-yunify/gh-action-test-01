import subprocess

def run_user_command(cmd):
    return subprocess.call(cmd, shell=True)
