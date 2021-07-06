<%inherit file="../layout.mako"/>

<div class="row justify-content-center">
    <h1 class="display-2 text-center">All Posts</h1>
</div>

<br>

<div class="row row-cols-1 row-cols-md-3">
    % for post in posts:
        <div class="col mb-4">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">${post.title}</h5>
                    <p class="card-text">By ${post.creator.username}</p>
                    <a href="${request.route_url('view_post', id=post.id)}" class="card-link">View</a>
                </div>
            </div>
        </div>
    % endfor
</div>