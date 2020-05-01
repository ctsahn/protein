import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="protein", 
    version="1.0.5",
    scripts=['protein'],
    author="Curtis S. Ahn",
    author_email="ctsahn@gmail.com",
    license = "MIT",
    keywords="protein bioinformatics uniprot",
    description="Quick UniProt protein search for the command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ctsahn/protein",
    packages=setuptools.find_packages(),
    install_requires=['xmltodict','requests'],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
)
