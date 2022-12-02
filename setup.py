from setuptools import setup, find_packages
 

description = "Extract details from a website"
long_description = "Super-scraper is a module that extract essential details from a website."

setup(
    name="super-scraper",
    version="0.0.1",
    description=description, 
    long_description=long_description,
    author="Aashish Upadhyay",
    maintainer="Aashish Upadhyay",
    packages=["super-scraper"] + find_packages("./super-scraper"),
    install_requires=[
        "requests>=2.7.0",
        "selenium>4.7.0",
    ]
)