TODO
- command to calculate coverage
- command to run tests
- command to run markers
- example to handle cassette
- migrate existing tests

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/GamestonkTerminal/GamestonkTerminal">
    <img src="../images/gst_logo_lockup_rGreen_with_letters.png" alt="Logo" width="800" height="276">
  </a>

  <h3 align="center">Gamestonk Terminal 🚀</h3>

  <p align="center">
    The next best thing after Bloomberg Terminal. #weliketheterminal
    <br />
    <a href="https://github.com/GamestonkTerminal/GamestonkTerminal/blob/master/ROADMAP.md"><strong>≪  ROADMAP</strong></a>
    &nbsp · &nbsp
    <a href="https://github.com/GamestonkTerminal/GamestonkTerminal/tree/master/gamestonk_terminal/README.md">
    <strong>FEATURES »</strong></a>
    <br />
    <br />
    <a href="https://github.com/GamestonkTerminal/GamestonkTerminal/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBug%5D">
    Report Bug</a>
    ·
    <a href="https://github.com/GamestonkTerminal/GamestonkTerminal/issues/new?assignees=&labels=enhancement&template=enhancement.md&title=%5BIMPROVE%5D">
    Suggest Improvement</a>
    ·
    <a href="https://github.com/GamestonkTerminal/GamestonkTerminal/issues/new?assignees=&labels=new+feature&template=feature_request.md&title=%5BFR%5D">
    Request Feature</a>
  </p>
</p>

# 1. Gamestonk tests

The purpose of this document is to explain how tests should be handled in the library GamestonkTerminal.

Gamestonk strive to solve the following issues regarding tests :  
- Having tests
- Maintain tests
- Running tests

# 2. Having tests

Here we will see how to build tests for GamestonkTerminal.

In order to build tests we need to know :
- What to test ?
- Where to put those tests ?
- How maintain tests ?

## 2.1. What to test ?
Every classes and methods which can be publicly accessed should be tested.

The purpose here, is not to verify the soundness (testing every possible variation) of a code but to :

    A. Run the python interpreter through every parts of the code
    B. Automate the common sense tests that the user or developer would have done manually

*Can I inject a bug in the code and still pass the tests ?*

If the answer is yes, then it's probably a good idea to add test for this case.

## 2.2. Where to put those tests ?

In the `tests` folder.

NOTES
- how should it be organised
- one test file for each class seems easy to track
- keeping the same folder structure than the `gamestonk_terminal` module seems to make sense
- what happend to slow tests ?
- what happend to network tests ?
- wheat happend to logged in tests ?

# 3. Maintain tests

The PR process should force tests to be written in the case that :
- coverage is reduced (we need a coverage indicator)
- a bug is was undetected

## 3.1. What are the indicators ?

NOTES
- Do we have coverage indicator running ?
- We can use pytest-cov

Everytime a PR is made a coverage indicator should be displayed.

## 3.2. What is the PR checklist ?

A tests update might be asked whenever the answer to one of the following question is `yes` :

    A. Is this PR fixing bug which was not detected by the current tests ?
    B. Is this PR reducing code coverage ?
    C. Is this PR adding features ?
    D. Is this PR updating features ?

# 4. Running tests

Provided that the tests where properly built and maintained.

Running them will allow you testing in matter of minutes : dozens of cases that would requires hours to check manually.

This is a powerfull tool : here we will see how to run it.

## 4.1. How to run all the tests ?

TODO
- put the command

## 4.1. How to run specific features ?

Markers can be used to run specific parts of the 

|**Markers**|**Description**|
|:-|:-|
|slow|Tests which are slow to run.|
|net|Tests which require network connectivity.|
|login|Tests|

Section `[tool.pytest.ini_options]` of this document contains full list of markers :
- [pyproject.toml](pyproject.toml)

One can also select run invidual folder or files.

TODO
- explain how to run invidual folder or file
- explain how to run specific markers
- list the avaialble tags
- put the command : slow, network