import markdown2
from pyramid.httpexceptions import (
    HTTPNotFound
)
from pyramid.view import view_config

from ..models import Post


@view_config(route_name='view_post', renderer='simple_blog:templates/posts/view.mako', permission='view')
def view_post(request):
    post_id = request.matchdict['id']
    post = request.dbsession.query(Post).get(post_id)
    if post is None:
        raise HTTPNotFound('No such post')
    render = markdown2.markdown(post.data)

    return dict(post=post, render=render)
