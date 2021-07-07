# Simple Blog

A simple blog made with Python 3.9, Pyramid, Mako, SQLAlchemy.

Blog posts fully support Markdown.

## Run
### The simpler way with docker:
You'll need docker and docker-compose
```shell
$ git clone https://github.com/zoemartin01/simple_blog.git
$ cd simple_blog
$ docker-compose build
$ docker-compose up
```
then open http://localhost

### or the not-as-simple way:

You'll need these programs:
- python3
- pip3
- sqlite3

```shell
$ git clone https://github.com/zoemartin01/simple_blog.git
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install --upgrade pip setuptools
$ pip3 install -e .
$ touch simple_blog.sqlite
$ alembic -c production.ini revision --autogenerate -m "init"
$ alembic -c production.ini upgrade head
$ initialize_simple_blog_db production.ini
$ pserve production.ini
```

then open http://localhost:6543