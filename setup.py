from setuptools import setup, find_packages

with open("readme.rst", encoding="UTF-8") as f:
    readme = f.read()

    setup(
        name="pgbackup",
        version="0.1.0",
        description="Database backup",
        long_description=readme,
        author="tvminh",
        author_email="tvminh1701@gmail.com",
        packages=find_packages("src"),
        package_dir={"": "src"},
        install_requires=["boto3"],
        entry_points={"console_scripts": ["pgbackup=pgbackup.cli:main"]},
    )
