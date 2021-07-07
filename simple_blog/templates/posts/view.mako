<%inherit file="../layout.mako"/>

<div class="row">
    <h1>${post.title}</h1>
</div>
<div class="row">
    <h3>By ${post.creator.username}</h3>
</div>

% if request.is_authenticated and request.identity == post.creator:
    <a class="btn btn-outline-dark" role="button" href="${ request.route_url('edit_post', id=post.id)}">Edit</a>
    <span class="btn btn-danger" role="button" onclick="del()">Delete</span>

% endif

${render | n}


<script>
    function del() {
        if (confirm("Are you sure?")) {
            $.ajax({
                type: "DELETE",
                url: "${ request.route_url('delete_post', id=post.id)}",
                data: {csrf_token: '${ get_csrf_token() }'},
                success: function (data, textStatus) {
                    if (data.redirect) {
                        window.location.href = data.redirect;
                    } else {
                        window.location.href = '/'
                    }
                }
            })
        }
    }
</script>
