import subprocess

def install_chatterbot():
    try:
        subprocess.run(["pip3", "uninstall", "-y", "chatterbot"])
        subprocess.run(["pip3", "install", "chatterbot"])
        print("ChatterBot reinstalled successfully.")
    except Exception as e:
        print(f"Error reinstalling ChatterBot: {e}")

if __name__ == "__main__":
    install_chatterbot()

