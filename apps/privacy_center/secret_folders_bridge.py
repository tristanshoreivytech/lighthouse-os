import subprocess

CLI = ["/usr/bin/python3", "/usr/local/lighthouse/secret-folders/secret_folder_cli.py"]

def run_cli(*args: str) -> str:
    result = subprocess.run(CLI + list(args), capture_output=True, text=True, check=False)
    return result.stdout.strip() or result.stderr.strip()
