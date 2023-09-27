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
        help="how and where to store dump file",
        nargs=2,
        action=DriverAction,
        required=True,
    )
    return parser
