from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import (
    HTTPSeeOther,
    HTTPNotFound
)
import markdown2

from .. import models


@view_config(route_name='frontpage', renderer='simple_blog:templates/frontpage.mako')
def frontpage(request):
    posts = request.dbsession.query(models.Post).limit(5).all()
    return dict(posts=posts)


@view_config(route_name='all_posts', renderer='simple_blog:templates/posts/view_all.mako')
def view_all_posts(request):
    posts = request.dbsession.query(models.Post).all()
    return dict(posts=posts)


@view_config(route_name='view_post', renderer='simple_blog:templates/posts/view.mako')
def view_post(request):
    post_id = request.matchdict['id']
    post = request.dbsession.query(models.Post).get(post_id)
    if post is None:
        raise HTTPNotFound('No such post')
    render = markdown2.markdown(post.data)

    return dict(post=post, render=render)


@view_config(route_name='new_post', renderer='simple_blog:templates/posts/new_post.mako')
def new_post(request):
    # if request.method == 'POST':
        # TODO
    return dict()


@view_config(route_name='edit_post', renderer='simple_blog:templates/posts/edit_post.mako')
def edit_post(request):
    # if request.method == 'POST':
        # TODO
    return dict()

