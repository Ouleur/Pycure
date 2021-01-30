import setuptools

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymcure",
    version="0.0.1",
    author="Vianney ADOU",
    author_mail="adoujmv@hmail.com",
    descripton="Mercure python module",
    long_description=long_description,
    url="https://github.com/Ouleur/Pymcure",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Os Independent",
    ],
    python_rquires='>=3.6',
)