import subprocess


def dump(url):
    return subprocess.Popen(["pg_dump", url], stdout=subprocess.PIPE)


def dump_file_name(url, timestamp=None):
    db_name = url.split("/")[-1]
    db_name = db_name.split("?")[0]

    if timestamp:
        return f"{db_name}-{timestamp}.sql"
    return f"{db_name}.sql"
