from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPSeeOther
)
from ..models import ActivationToken


@view_config(route_name='activate', permission='view')
def activate(request):
    token = request.matchdict['token']
    activation_token = request.dbsession.query(ActivationToken).filter_by(token=token).first()
    if activation_token is None:
        request.session.flash('This token does not exist!')
        return HTTPSeeOther(location=request.route_url('frontpage'))
    activation_token.user.active = True
    request.dbsession.delete(activation_token)
    request.session.flash('Account activated!')
    return HTTPFound(location=request.route_url('frontpage'))
