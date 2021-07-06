<%inherit file="../layout.mako"/>

<div class="row justify-content-center">
    <h1 class="display-2 text-center">Login</h1>
</div>

<br>

<div class="row justify-content-center">
    <div class="col-auto justify-content-center">
        <form action="${ request.url }" method="post">
            <div class="form-group">
                <label for="email">Email address</label>
                <input type="email" class="form-control" id="email" name="email" value="${ email }">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" name="password">
            </div>
            <input type="hidden" name="csrf_token" value="${ get_csrf_token() }">
            <input type="hidden" name="next" value="${ next_url }">
            <div class="row justify-content-center">
                <button type="submit" class="btn btn-primary text-center">Submit</button>
            </div>
            <div class="row justify-content-center">
                <a href="${ request.route_url('password_forgotten') }" class="text-center">Forgot your password?</a>
            </div>
            <div class="row justify-content-center">
                <a href="${ request.route_url('register') }" class="text-center">No account yet? Register here!</a>
            </div>
        </form>
    </div>
</div>