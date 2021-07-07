from pyramid.csrf import new_csrf_token
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPSeeOther
)
from pyramid.security import remember
from pyramid.view import view_config

from ..models import User


@view_config(route_name='login', renderer='simple_blog:templates/users/login.mako', permission='view')
def login(request):
    if request.identity:
        return HTTPSeeOther(location=request.route_url('frontpage'))
    next_url = request.params.get('next', request.referrer)
    email = ''
    if not next_url or next_url == request.route_url('login'):
        next_url = request.route_url('frontpage')
    if request.method == 'POST':
        email = request.params['email']
        password = request.params['password']
        user = request.dbsession.query(User).filter_by(email=email).first()
        if user is not None and user.check_password(password) and user.active:
            new_csrf_token(request)
            headers = remember(request, user.id)
            request.session.flash('Login successful')
            return HTTPFound(location=next_url, headers=headers)
        elif not user:
            request.session.flash('User does not exist!')
        elif not user.active:
            request.session.flash('Account not activated!')
        elif not user.check_password(password):
            request.session.flash('Password incorrect!')
        request.response.status = 400

    return dict(
        next_url=next_url,
        email=email
    )
