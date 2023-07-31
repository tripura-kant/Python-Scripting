import subprocess


def read_packages_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def install_packages(packages):
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.run(['pip', 'install', package], check=True)
            print(f"Successfully installed {package}!\n")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}\n")


if __name__ == "__main__":
    packages_file = "list"
    packages_to_install = read_packages_from_file(packages_file)

    if packages_to_install:
        install_packages(packages_to_install)
        print("All packages installed successfully.")
    else:
        print("No packages found in the file.")
