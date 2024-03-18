from setuptools import setup

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding='UTF-8') as fh:
    requirements = fh.read().split("\n")

setup(
    name="googlesearch-python",
    version="0.1.0",
    license="MIT License",
    author="Amit Bhargav",
    author_email="amitbhargav134@gmail.com",
    description="A Python library for scraping the Google search engine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amitbhargav0408/googlesearch-new",
    packages=["googlesearch"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[requirements],
    include_package_data=True,
)
