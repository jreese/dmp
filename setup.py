from setuptools import setup

with open("README.md") as f:
    readme = f.read()

with open("dmp/__init__.py") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split('"')[1]

setup(
    name="dmp",
    description="Repackaging of Google's Diff Match and Patch libraries. Offers robust algorithms to perform the operations required for synchronizing plain text.",
    long_description=readme,
    long_description_content_type="text/markdown",
    version=version,
    author="Neil Fraser",
    author_email="fraser@google.com",
    url="https://github.com/jreese/dmp",
    classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: Text Processing",
    ],
    license="Apache",
    packages=["dmp", "dmp.tests"],
    setup_requires=["setuptools>=38.6.0"],
    install_requires=[],
)
