import sys

def main():
    print("🌴 JungleScript")
    print("JungleScript engine is running!")

    if len(sys.argv) > 1:
        filename = sys.argv[1]

        try:
            with open(filename, "r", encoding="utf-8") as file:
                code = file.read()

            print(f"Running: {filename}")
            print(code)

        except FileNotFoundError:
            print(f"File not found: {filename}")

    else:
        print("Usage: junglescript <file.jls>")

if __name__ == "__main__":
    main()
