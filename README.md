# Peephole Dev Setup

## First setup virtual env
1. `pip install virtualenv`
2. `mkdir ~/.virtualenvs`
3. `virutalenv ~/.virtualenvs/peephole`
4. `. ~/.virtualenvs/peephole/bin/activate`

## Install python dependencies
1. `pip install -r requirements.txt`

## Add python dependencies
1. `pip freeze > requirements.txt`

## DB Migrations
1. After making schema changes, run `flask db migrate` to create migration
2. Inspect migration file (migrations/versions/...) and run `flask db upgrade`
REMEMBER: Always run `flask db upgrade` after pulling someone's migration changes

