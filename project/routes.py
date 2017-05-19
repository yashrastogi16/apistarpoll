from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
from project.views import welcome, show_request, show_query_params, show_user_agent

routes = [
    Route('/', 'GET', welcome),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]
