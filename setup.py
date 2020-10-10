import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="taxopedia",
    version="0.2.1",
    author="Shane Drabing",
    author_email="shane.drabing@gmail.com",
    packages=setuptools.find_packages(),
    url="https://github.com/shanedrabing/taxopedia",
    description="Build cladograms from Wikipedia-scraped data.",
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
        "pandas", "tqdm", "bs4", "asyncio", "aiohttp"
    ]
)
