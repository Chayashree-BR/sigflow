import argparse
from sigflow.cli.commands import inspect_command, parse_command, replay_command, validate_command


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sigflow")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("parse")
    p.add_argument("path")
    p.add_argument("--format", choices=["table", "json"], default="table")
    p.set_defaults(func=parse_command)
    v = sub.add_parser("validate")
    v.add_argument("path")
    v.set_defaults(func=validate_command)
    i = sub.add_parser("inspect")
    i.add_argument("path")
    i.set_defaults(func=inspect_command)
    r = sub.add_parser("replay")
    r.add_argument("path")
    r.add_argument("--rate", type=int, default=100)
    r.set_defaults(func=replay_command)
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
