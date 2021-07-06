<%inherit file="../layout.mako"/>

<div class="row">
    <h1>${post.title}</h1>
</div>
<div class="row">
    <h3>By ${post.creator.username}</h3>
</div>

<a href="${ request.route_url('edit_post', id=post.id)}">Edit</a>

<div class="row">
    ${render | n}
</div>