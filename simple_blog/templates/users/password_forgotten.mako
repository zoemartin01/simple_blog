<%inherit file="../layout.mako"/>

<div class="row justify-content-center">
    <h1 class="display-2 text-center">Password Forgotten?</h1>
</div>

<br>

<div class="row justify-content-center">
    <div class="col-auto justify-content-center">
        <form action="${ request.url }" method="post">
            <div class="form-group">
                <label for="email">Email address</label>
                <input type="email" class="form-control" id="email" name="email" value="${ email }">
            </div>
            <input type="hidden" name="csrf_token" value="${ get_csrf_token() }">
            <div class="row justify-content-center">
                <button type="submit" class="btn btn-primary text-center">Reset</button>
        </form>
    </div>
</div>