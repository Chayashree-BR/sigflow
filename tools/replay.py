from sigflow.cli.main import main

if __name__ == "__main__":
    raise SystemExit(main(["replay", *(__import__("sys").argv[1:])]))
