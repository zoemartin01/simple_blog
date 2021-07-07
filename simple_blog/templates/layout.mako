<!DOCTYPE html>
<html lang="${request.locale_name}">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="pyramid web application">
    <meta name="author" content="Pylons Project">
    <link rel="shortcut icon" href="${request.static_url('simple_blog:static/pyramid-16x16.png')}">

    <title>A Simple Blog</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css"
          integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">

    <!-- Bootstrap core JavaScript -->
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"
            crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-Piv4xVNRyMGpqkS2by6br4gNJ7DXjqk09RmUpJ8jgGtD7zP9yug3goQfGII0yAns"
            crossorigin="anonymous"></script>


    <!-- Custom styles for this scaffold -->
    <link href="${request.static_url('simple_blog:static/theme.css')}" rel="stylesheet">

    <!-- HTML5 shiv and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
    <script src="//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"
            integrity="sha384-0s5Pv64cNZJieYFkXYOTId2HMA2Lfb6q2nAcx2n0RTLUnCAoTTsS0nKEO27XyKcY"
            crossorigin="anonymous"></script>
    <script src="//oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"
            integrity="sha384-ZoaMbDF+4LeFxg6WdScQ9nnR1QC2MIRxA1O9KWEXQwns1G8UNyIEZIQidzb0T1fo"
            crossorigin="anonymous"></script>
    <![endif]-->
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light m-3" style="background-color: #e3f2fd;">
    <a class="navbar-brand" href="#">Simple Blog</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText"
            aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
                <a class="nav-link" href="/">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="${ request.route_url('all_posts')}">Posts</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="${ request.route_url('new_post')}">New Post</a>
            </li>
        </ul>
        <span class="navbar-text">
            % if not request.is_authenticated:
                <p class="pull-right">
              <a href="${ request.route_url('login') }">Login</a>
            </p>
            % else:
                <form class="pull-right" action="${ request.route_url('logout') }" method="post">
              ${request.identity.username}
                    <input type="hidden" name="csrf_token" value="${ get_csrf_token() }">
              <button class="btn btn-link" type="submit">Logout</button>
            </form>
            % endif
        </span>
    </div>
</nav>

<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-12">
            % if request.session.peek_flash():
                <% flash = request.session.pop_flash() %>
                % for msg in flash:
                    <div class="col-md-12 alert alert-info" role="alert">
                        ${ msg }
                    </div>
                %endfor
            % endif
        </div>
    </div>

    <div class="col-auto">
        ${ next.body() }
    </div>
</div>

</body>
</html>

