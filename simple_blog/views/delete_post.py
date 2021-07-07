from pyramid.httpexceptions import (
    HTTPFound,
    HTTPSeeOther
)
from pyramid.view import view_config

from ..models import Post


@view_config(route_name='delete_post', permission='edit')
def edit_post(request):
    post_id = request.matchdict['id']
    post = request.dbsession.query(Post).get(post_id)
    if request.method == 'DELETE':
        request.dbsession.delete(post)
        request.session.flash('Post deleted successfully!')
        return HTTPFound(location=request.route_url('frontpage'))
    return HTTPFound(location=request.route_url('frontpage'))
