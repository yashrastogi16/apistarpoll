from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
from project.views import welcome, create_poll, polls

routes = [
    Route('/', 'GET', welcome),
    Route('/create_poll', 'POST', create_poll),
    Route('/polls', 'GET', polls),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]
