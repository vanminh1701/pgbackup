from argparse import ArgumentParser, Action, Namespace
from collections.abc import Sequence
from typing import Any

known_drivers = ["local", "s3"]


class DriverAction(Action):
    def __call__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = None,
    ) -> None:
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error('Unknown driver. Available drivers are "local" or "s3"')
        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    parser = ArgumentParser()
    parser.add_argument("url", help="URL of the database Postgres")
    parser.add_argument(
        "--driver",
        "-d",
        help="how and where to store dump file",
        nargs=2,
        action=DriverAction,
        required=True,
    )
    return parser


def main():
    import time
    import boto3
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)

    if args.driver == "s3":
        client = boto3.client("s3")
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        print(f"Backing database up to {args.destination} in S3 as {file_name}")
        storage.s3(client, dump.stdout, args.destination, file_name)

    else:
        outfile = open(args.destination, "wb")
        print(f"Backing database to locally as {args.destination}")
        storage.local(dump.stdout, outfile)
