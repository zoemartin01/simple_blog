import uuid

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from ..models import User, ActivationToken


@view_config(route_name='register', renderer='simple_blog:templates/users/register.mako', permission='view')
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
        users_by_mail = session.query(User).filter_by(email=email).all()
        users_by_username = session.query(User).filter_by(username=username).all()

        if len(users_by_mail) == 0 and len(users_by_username) == 0 and password == password_confirmation:
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
        else:
            if len(users_by_mail) != 0:
                request.session.flash('That e-mail already belongs to a user')
            if len(users_by_username) != 0:
                request.session.flash('That username already belongs to a user')
            if password != password_confirmation:
                request.session.flash('The passwords do not match')
        request.response.status = 400

    return dict(
        url=request.route_url('register'),
        next_url=next_url,
        email=email,
        username=username
    )
