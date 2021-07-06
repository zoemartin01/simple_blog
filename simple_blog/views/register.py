import uuid

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from sqlalchemy import or_

from ..models import User, ActivationToken


@view_config(route_name='register', renderer='simple_blog:templates/users/register.mako')
def register(request):
    next_url = request.params.get('next', request.referrer)
    if not next_url or next_url == request.route_url('login'):
        next_url = request.route_url('frontpage')
    email = ''
    username = ''
    if request.method == 'POST':
        email = request.params['email']
        username = request.params['username']
        password = request.params['password']
        password_confirmation = request.params['password_confirmation']
        session = request.dbsession
        users = session.query(User).filter(
            or_(
                User.username.like(username),
                User.email.like(email)
            )
        ).all()

        if len(users) == 0 and password == password_confirmation:
            user = User(
                email=email,
                username=username,
            )
            user.set_password(password)
            session.add(user)
            session.flush()
            activation_token = ActivationToken(token=str(uuid.uuid4()), user=user)
            session.add(activation_token)
            print(request.route_url("activate", token=activation_token.token))
            request.session.flash('Registration successful. (activation url in console)')
            return HTTPFound(location=next_url)
        request.session.flash('Failed registration')
        request.response.status = 400

    return dict(
        url=request.route_url('register'),
        next_url=next_url,
        email=email,
        username=username
    )
