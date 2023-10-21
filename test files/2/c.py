import subprocess

def run():
    subprocess.run(["runas", "python b.py"])

if __name__ == "__main__":
    run()