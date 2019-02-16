# Prerequisites

To decrease the hassle of installing different versions of dependencies for the project, it is recommended that you use pipenv. Pipenv ships with package management and virtual environment support. To install, just run the command below

`pip install pipenv`

# Getting Started

Follow the steps below to clone and set up the project.

1. `git clone git@github.com:peakshift/event-listener.git`

2. `cd event-listener`


To run the script:
1. `pipenv install`

2. `server= "server url" pipenv run python app.py`
  - eg. `server="http://localhost:8080" pipenv run python app.py`

In these steps pipenv is installing the necessary dependencies for the project and automatically creates a virtual environment for the project. Any other dependencies that you may add would be automatically added to the Pipfile.

# Contributing

### Branches
- A branch name should begin with the issue number, and have short name (2-4 words). New features or fixes should be based off of the `master` branch.
  - `git checkout -b 123-short-name master`

### Testing
When making changes or adding a new feature, to ensure the feature works correctly or the changes made have not broken the code then you can do unit testing using the behave framework and gherkin scenarios.
*[Behave Framework Docs](https://behave.readthedocs.io/en/latest/) 

To begin testing your scenarios
- run `pipenv install behave`
- run `pipenv run behave`
- if it passes
  - commit and push your branch
  - open a pull request for your branch in develop
- if it fails
  - fix the problem so all tests pass

#### Testing CircleCI Locally
Changes to the CircleCI config can be made at `/.circleci/config.yml`. For guidance on how
configs work, see [this documentation](https://circleci.com/docs/2.0/examples/).

To test your config changes locally:
1. Open Terminal and cd to telegram-dogecoin repository
2. `$ cd .circleci`
3. Go to circleci.com and [get a new API token](https://circleci.com/account/api) (for `CIRCLE_TOKEN`)
4. `$ git log`
5. Copy the commit hash (for `COMMIT_HASH`)
6. Copy the branch name (for `BRANCH_NAME`)
7. Set environment variables in Terminal:
    ```
    $ export CIRCLE_TOKEN=<api token>
    $ export COMMIT_HASH=<commit hash>
    $ export BRANCH_NAME=<branch name>
    ```
8. Execute build script:  `$ ./run-build-locally.sh`
9. Go to `https://circleci.com/gh/peakshift/ethereum-address-listener/tree/<branch name>` and confirm tests are running. 

### Pushing Changes
1. Open Terminal.
2. `git pull`
3. `git add file_name.py`
4. `git commit -m "type(component): subject line"`
5. `git push origin 123-short-name `

### Commit Messages

*We follow the [Angular commit guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines) so that we can generate changelogs and have a clean commit history — see Pushing Changes #3 for an example commit.*

- Type, for your commit message commiting you should select a type from this list below:
  - feat: a new features
  - fix: a bug fix
  - docs: documentation only changes
  - style: changes that do not affect the menaing of the code (white-space, formatting, missing semi-colons, etc)
  - refactor: a code change that neither fixes a bug or adds a feature
  - pref: a code change that improves performance
  - test: adding missing tests
  - chore: changes to the build process or auxiliary tools and libraries such as documentation generation
- Components, represent the larger feature / scope of the change
- Subject line, use the imperative form of a verb
  - GOOD "add contributing guidelines"
  - BAD "adding contribuing guidelines"
