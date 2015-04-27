=============
social-status
=============

An aggregator for contacts from multiple social networks.

It's a web frontend written in Django.

For users
#########

Prerequisites
=============

- Django
- Python 3
- PostgreSQL

Installation and configuration
==============================

Database
~~~~~~~~

First create a database for the application::

    CREATE DATABASE social_status ENCODING 'UTF8';

Ensure that the name used above matches the one in `settings.DATABASES['default']['NAME']`.

You need create a PostgreSQL role with correct privileges for your database::

    CREATE ROLE social_status LOGIN CREATEDB;
    \password social_status
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO social_status;
    GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO social_status;
    GRANT USAGE ON SCHEMA public TO social_status;

Name of the role used above must match `settings.DATABASES['default']['NAME']` 

The role must be able to create and drop the test database.
Note that in PostgreSQL you can't limit `CREATEDB` privilege to a specific database name.
This means that the newly created role will be able to create and drop any database on your server.

For developers
##############

General rules
=============

- Use `rebase workflow`_.
- Always use `--no-ff` when merging your branch to `master`.

.. _`rebase workflow`: http://randyfay.com/content/rebase-workflow-git

Commit messages
===============

- Capitalized, short summary on the first line, followed by a more detailed description below if needed.
- Written in imperative: "Fix bug" and not "Fixed bug".

Style
=====

- Use 4 spaces for indentation (not only in Python).
- Set up your editor to automatically remove all trailing whitespace.
- Python code must pass through `pep8` without warnings or errors, except for the few we explicitly decide to ignore:

    .. code:: sh

        pep8 . --ignore=E241,E501

    - `E501 line too long`.
        Try to keep lines short but it's not a requirement.
        Prefer long lines where unnatural line breaks would decrease readability.
    - `E241 multiple spaces`.
        Lack of vertical alignment can decrease readability.

License
#######

Released under the `MIT License`_.

.. _`MIT License`: http://opensource.org/licenses/MIT
