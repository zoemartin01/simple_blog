from pyramid.csrf import new_csrf_token
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPSeeOther
)
from pyramid.security import forget
from pyramid.view import view_config


@view_config(route_name='logout')
def logout(request):
    next_url = request.route_url('frontpage', permission='view')
    if request.method == 'POST':
        new_csrf_token(request)
        headers = forget(request)
        request.session.flash('Logged out sucesfully')
        return HTTPFound(location=next_url, headers=headers)
    return HTTPSeeOther(location=next_url)