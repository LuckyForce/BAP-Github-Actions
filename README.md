
# github actions

- Choose a programming language/platform
- Provide a sample project
  - With _at least_ 1 automated test
- Configure github actions
  - So that it verifies _at least_ the test mentioned above
- For bonus points pack more features into your _github actions_

## Notes

As always, document your process/expectations/results here:

_TBD_

## Chosen language/platform
Python

## Sample project
A simple calculator

## Github actions
- Build/Test
- Publish

## Step 1: Create a sample project
- Create a simple calculator
- Create tests for the calculator

## Step 2: Configure github actions build/test
- Create a github action to build/test the project
//Name
name: Python Tests
//When to run. On push and pull request when files are changed in the calculator src folder or the workflow file
on: 
  push:
    paths:
      - 'src/**'
      - '.github/workflows/python-test.yml'
  pull_request:
    paths:
      - 'src/**'
      - '.github/workflows/python-test.yml'
//Jobs
jobs:
  build:
    //Test on ubuntu 3.7 and 3.10
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.7", "3.10"]

    //Steps
    steps:
    //Checkout the code and set up python
      - uses: actions/checkout@v3
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      //Test the code with the in python implemented unittest framework
      - name: Test with unittest
        run: |
          cd src
          python -m unittest unittests.py

### Effects
- The github action is triggered when a push or pull request is made to the src folder or the workflow file
- The github action runs on ubuntu-latest
- The github action runs on python 3.7 and 3.10
- The github action runs the unittests.py file in the src folder

## Step 3: Configure github actions release
- Create a github action to create a release
//Name
name: Create a new patch release
//When to run. On push and pull request when files are changed in the calculator src folder or the workflow file
on:
  push:
    paths:
      - 'src/**'
      - '.github/workflows/python-release.yml'
  pull_request:
    paths:
      - 'src/**'
      - '.github/workflows/python-release.yml'
jobs:
  github:
    runs-on: ubuntu-latest
    steps:
    //Checkout the code and set up python
      - name: Checkout
        uses: actions/checkout@v3
    //Create a new release. Only works when the secret GITHUB_TOKEN is set
      - name: Create new patch release
        run: .github/scripts/release.py
        env:
          GITHUB_TOKEN: ${{ secrets.PERSONAL_ACCESS_TOKEN }}

### Effects
- The github action is triggered when a push or pull request is made to the src folder or the workflow file
- The github action runs on ubuntu-latest
- The github action creates a new release when a push is made to the src folder
- The github action only works when the secret GITHUB_TOKEN is set

## Step 4: Configure github actions create executable
- Create a github action to create an executable



