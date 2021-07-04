<%inherit file="layout.mako"/>

% for post in posts:
    <div class="card" style="width: 18rem;">
        <div class="card-body">
            <h5 class="card-title">${post.title}</h5>
            <a href="/posts/${post.id}" class="card-link">View</a>
        </div>
    </div>
% endfor