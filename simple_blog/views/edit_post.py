from pyramid.httpexceptions import (
    HTTPFound
)
from pyramid.view import view_config

from ..models import Post


@view_config(route_name='edit_post', renderer='simple_blog:templates/posts/edit_post.mako', permission='edit')
def edit_post(request):
    post_id = request.matchdict['id']
    post = request.dbsession.query(Post).get(post_id)
    if request.method == 'POST':
        post.title = request.params['title']
        post.data = request.params['data']
        next_url = request.route_url('view_post', id=post_id)
        request.session.flash('Post edited sucessfully!')
        return HTTPFound(location=next_url)
    return dict(
        post_title=post.title,
        post_data=post.data,
        save_url=request.route_url('edit_post', id=post_id)
    )
