def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('frontpage', '/')

    config.add_route('all_posts', '/posts')
    config.add_route('new_post', '/posts/new')
    config.add_route('view_post', '/posts/{id}')
    config.add_route('edit_post', '/posts/{id}/edit')

    config.add_route('login', '/login')
    config.add_route('register', '/register')
    config.add_route('logout', '/logout')
    config.add_route('password_forgotten', '/password_forgotten/')
    config.add_route('password_reset', '/password_forgotten/{token}')
    config.add_route('activate', '/activate/{token}')
