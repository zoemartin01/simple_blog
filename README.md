# Simple Blog

A simple blog made with Python 3.9, Pyramid, Mako, SQLAlchemy.

Blog posts fully support Markdown.

## Run
### The easy way with docker:
1. Clone the repository: 
   
`$ git clone https://github.com/zoemartin01/simple_blog.git`
2. Build with docker-compose:
   
`$ docker-compose build`
3. Then run it: 

`$ docker-compose up`

4. goto

http://localhost

### or the not-as-easy way:

You'll need these programs:
- python3.9
- sqlite3

```
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

then goto http://localhost:6543