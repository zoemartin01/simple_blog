from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPForbidden
)
import uuid
from ..models import Post


@view_config(route_name='new_post', renderer='simple_blog:templates/posts/new_post.mako')
def new_post(request):
    user = request.identity
    if user is None:
        raise HTTPForbidden
    if request.method == 'POST':
        title = request.params['title']
        data = request.params['data']
        post = Post(
            title=title,
            data=data,
            creator=user
        )
        session = request.dbsession
        session.add(post)
        session.flush()
        next_url = request.route_url('view_post', id=post.id)
        request.session.flash('New post created!')
        return HTTPFound(location=next_url)
    return dict()
