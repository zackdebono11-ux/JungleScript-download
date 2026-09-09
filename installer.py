import os
import shutil
import sys

INSTALL_DIR = os.path.join(
    os.environ.get("LOCALAPPDATA", os.path.expanduser("~")),
    "JungleScript"
)

def install():
    print("🌴 JungleScript Installer")
    print("=========================")

    os.makedirs(INSTALL_DIR, exist_ok=True)

    source = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "junglescript.exe"
    )

    destination = os.path.join(INSTALL_DIR, "junglescript.exe")

    shutil.copy2(source, destination)

    print()
    print("JungleScript installed!")
    print(f"Location: {destination}")
    print()
    input("Press Enter to close...")

if __name__ == "__main__":
    install()
