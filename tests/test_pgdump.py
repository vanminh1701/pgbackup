import subprocess

from pgbackup import pgdump

url = "postgres://minh@localhost:5432/minh"


def test_dump_calls_pg_dump(mocker):
    """Utilize pg_dump with the datbase URL

    Args:
        mocker (_type_): _description_
    """
    mocker.patch("subprocess.Popen")
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(["pg_dump", url], stdout=subprocess.PIPE)


def test_dump_file_name_without_timestamp():
    """pgdump.dump_file_name returns the name of the database with timestamp"""
    assert pgdump.dump_file_name(url) == "minh.sql"


def test_dump_file_name_with_timestamp():
    """pgdump.dump_file_name returns the name of the database with timestamp"""

    timestamp = "2023-09-27T08:49:33.438Z"

    assert pgdump.dump_file_name(url, timestamp) == f"minh-{timestamp}.sql"
