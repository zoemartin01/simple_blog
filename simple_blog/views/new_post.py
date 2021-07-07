import html

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from ..models import Post


@view_config(route_name='new_post', renderer='simple_blog:templates/posts/new_post.mako', permission='create')
def new_post(request):
    if request.method == 'POST':
        user = request.identity
        title = request.params['title']
        data = html.escape(request.params['data'])
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
