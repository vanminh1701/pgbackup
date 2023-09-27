learn-python
============

CLI for backup remote PosgreSQL database either locally or S3

Preparing the Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clon repository
3. ``cd`` into the repository.
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``


Usage
-----
Pass in a full database URL, the storage driver, and the destination

S3 Example w/ bucket name:

::
  
        $ pgbackup posgresql://minh:password@localhost:5432/minh --driver s3 backups

Local Example w/ local path:

::

        $ pgbackup postgresql://minh:password@localhost:5432/minh --driver local ./dump.sql



Running Tests
-------------
