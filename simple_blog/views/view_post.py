from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPNotFound
)
import uuid
import markdown2
from ..models import Post


@view_config(route_name='view_post', renderer='simple_blog:templates/posts/view.mako')
def view_post(request):
    post_id = request.matchdict['id']
    post = request.dbsession.query(Post).get(post_id)
    if post is None:
        raise HTTPNotFound('No such post')
    render = markdown2.markdown(post.data)

    return dict(post=post, render=render)
