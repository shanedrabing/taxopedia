import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="taxopedia",
    version="1.1.3",
    author="Shane Drabing",
    author_email="shane.drabing@gmail.com",
    packages=setuptools.find_packages(),
    url="https://github.com/shanedrabing/taxopedia",
    description="Taxonomic trees (cladograms) from Wikipedia-scraped data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    data_files=[
        ("", ["LICENSE.txt"])
    ],
    install_requires=[
        "bs4", "aiohttp"
    ]
)
