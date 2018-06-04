import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='travistest',
    packages=['travistest'],
    version='0.0.11',
    author="Srijan Manandhar",
    author_email="srijan.manandhar@gmail.com",
    description='Test project to get acquainted with TravisCI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/srijanss/travistest',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
