# README
This main purpose of this repo is to illustrate the current level of Python proficiency of the author rather than being actually usable for real world usecases. This is only magnified by the fact, that this repo was created while working with https://catalog.data.gov/dataset/lottery-powerball-winning-numbers-beginning-2010 dataset.

## Task
1. Create a python package which would provide a custom ETL solution. Demonstrate the knowledge of OOP.
2. The data to be downloaded and worked with is dataset from https://catalog.data.gov/dataset/lottery-powerball-winning-numbers-beginning-2010. Download the data in any format you see fit or implement more solutions for different formats.
3. Pick a destination, e.g. S3, database, local filesystem, and have the ETL pipeline upload to this destination. Destination can be replaced/mocked with a docker container.
4. Make sure your code follows the best practices and is properly tested.
5. Provide a simple way to run the whole orchestration and clearly document every step needed to be able to run it.

## Solution
I created a `Makefile` to have every command and part of the process streamlined and easy to use.
1. Create a new virtual environment
```
make venv
```
2. Activate the virtual environment
```
make venv-activate
```
3. Install the python package called `etl_tools`
```
make install
```
4. To run the whole orchestration just to see if everything is working
```
make etl
```
5. To run tests, first install the test requirements and then run them
```
make install-test
make test
```

## Discussion
Please bear in mind this task was created with a certain time pressure and therefore there wasn't enough time to implement everything what and ideal production solution should include.  
To name a few unfinished points of work - no credentials handling, transform part of ETL was not implemented, integration tests are missing, the application is not general enough, etc.