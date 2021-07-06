#!/bin/bash
alembic -c production.ini revision --autogenerate -m "init"
alembic -c production.ini upgrade head
initialize_simple_blog_db production.ini
sqlite3 simple_blog.sqlite
python3 -u /usr/local/bin/pserve production.ini
