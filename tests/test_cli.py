import pytest

from pgbackup import cli

# pgbackup postgres://min@localhost:5432/min --driver s3 backups

url = "postgres://minh@localhost:5432/minh"


@pytest.fixture
def parser():
    return cli.create_parser()


def test_parser_without_driver(parser):
    """Without a specified driver the parser will exit"""
    with pytest.raises(SystemExit):
        parser.parse_args([url])


def test_parser_with_driver():
    """The parser will exit if it receive a driver without destination"""
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(
            [url, "--driver", "local"],
        )


def test_parser_with_driver_and_destination():
    """The parser will not exit if it receives a driver and destination"""
    parser = cli.create_parser()
    args = parser.parse_args(
        [url, "--driver", "local", "/some/path"],
    )

    assert args.url == url
    assert args.driver == "local"
    assert args.destination == "/some/path"
