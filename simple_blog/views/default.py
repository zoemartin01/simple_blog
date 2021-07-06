from pyramid.view import view_config, forbidden_view_config
from pyramid.httpexceptions import HTTPSeeOther

from .. import models


@view_config(route_name='frontpage', renderer='simple_blog:templates/frontpage.mako', permission='view')
def frontpage(request):
    posts = request.dbsession.query(models.Post).order_by(models.Post.id.desc()).limit(6).all()
    return dict(posts=posts)


@view_config(route_name='all_posts', renderer='simple_blog:templates/posts/view_all.mako', permission='view')
def view_all_posts(request):
    posts = request.dbsession.query(models.Post).all()
    return dict(posts=posts)


@forbidden_view_config(renderer='tutorial:templates/403.mako')
def forbidden_view(exc, request):
    if not request.is_authenticated:
        next_url = request.route_url('login', _query={'next': request.url})
        return HTTPSeeOther(location=next_url)

    request.response.status = 403
    return {}
