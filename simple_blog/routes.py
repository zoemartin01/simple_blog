from pyramid.authorization import (
    Allow,
    Everyone,
    Authenticated
)
from pyramid.httpexceptions import HTTPNotFound

from . import models


class Public(object):
    __acl__ = [(Allow, Everyone, 'view')]

    def __init__(self, request):
        pass


class AuthRequired(object):
    __acl__ = [(Allow, Authenticated, 'create')]

    def __init__(self, request):
        pass


class PostResource(object):
    def __init__(self, post):
        self.post = post

    def __acl__(self):
        return [
            (Allow, Everyone, 'view'),
            (Allow, 'u:' + str(self.post.creator_id), 'edit'),
        ]


def post_factory(request):
    post_id = request.matchdict['id']
    post = request.dbsession.query(models.Post).get(post_id)
    if post is None:
        raise HTTPNotFound
    return PostResource(post)


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('frontpage', '/', factory=Public)

    config.add_route('all_posts', '/posts', factory=Public)
    config.add_route('new_post', '/posts/new', factory=AuthRequired)
    config.add_route('view_post', '/posts/{id}', factory=post_factory)
    config.add_route('edit_post', '/posts/{id}/edit', factory=post_factory)
    config.add_route('delete_post', '/posts/{id}/delete', factory=post_factory)

    config.add_route('login', '/login', factory=Public)
    config.add_route('register', '/register', factory=Public)
    config.add_route('logout', '/logout', factory=AuthRequired)
    config.add_route('password_forgotten', '/password_forgotten/', factory=Public)
    config.add_route('password_reset', '/password_forgotten/{token}', factory=Public)
    config.add_route('activate', '/activate/{token}', factory=Public)
