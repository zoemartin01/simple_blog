<%inherit file="../layout.mako"/>

<div class="row justify-content-center">
    <h1 class="display-2 text-center">Password Reset</h1>
</div>

<br>

<div class="row justify-content-center">
    <div class="col-auto justify-content-center">
        <form action="${ request.url }" method="post">
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" name="password">
            </div>
            <div class="form-group">
                <label for="password_confirmation">Password Confirmation</label>
                <input type="password" class="form-control" id="password_confirmation" name="password_confirmation">
            </div>
            <input type="hidden" name="csrf_token" value="${ get_csrf_token() }">
            <div class="row justify-content-center">
                <button type="submit" class="btn btn-primary text-center">Save</button>
            </div>
        </form>
    </div>
</div>