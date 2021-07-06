<%inherit file="../layout.mako"/>

<form action="${ request.url }" method="post">
    <div class="form-group">
        <label for="title">Title</label>
        <input type="text" class="form-control" id="title" name="title" placeholder="Title">
    </div>
    <div class="form-group">
        <label for="data">Blog Post</label>
        <textarea class="form-control" id="data" name="data" rows="5"></textarea>
        <input type="hidden" name="csrf_token" value="${ get_csrf_token() }">
        <button type="submit" class="btn btn-primary m-2">Submit</button>
    </div>
</form>