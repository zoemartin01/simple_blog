from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPSeeOther
)
import uuid
from ..models import User, PasswordResetToken


@view_config(route_name='password_forgotten', renderer='simple_blog:templates/users/password_forgotten.mako')
def password_forgotten(request):
    email = ''
    if request.method == 'POST':
        email = request.params['email']
        user = request.dbsession.query(User).filter_by(email=email).first()
        if user:
            token = PasswordResetToken(token=str(uuid.uuid4()), user=user)
            request.dbsession.add(token)
            print(request.route_url('password_reset', token=token.token))
            request.session.flash('A password reset link has been sent to your email address (aka. the console)')
        else:
            request.session.flash('No user exists with that email address!')
    return dict(
        email=email
    )


@view_config(route_name='password_reset', renderer='simple_blog:templates/users/password_reset.mako')
def password_reset(request):
    next_url = request.route_url('frontpage')
    if request.method == 'POST':
        token = request.matchdict['token']
        reset_token = request.dbsession.query(PasswordResetToken).filter_by(token=token).first()
        if reset_token is None:
            request.session.flash('This token does not exist!')
            return HTTPSeeOther(location=next_url)

        password = request.params['password']
        password_confirmation = request.params['password_confirmation']

        if password == password_confirmation:
            reset_token.user.set_password(password)
            request.dbsession.delete(reset_token)
            request.session.flash('Password reset successful!')
            return HTTPFound(location=next_url)
        else:
            request.session.flash('Passwords do not match!')
    return {}
