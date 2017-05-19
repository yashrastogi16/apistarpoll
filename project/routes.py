from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
from project.views import welcome, create_poll, polls, polls_details, create_choices, vote

routes = [
    Route('/', 'GET', welcome),
    Route('/create_poll', 'POST', create_poll),
    Route('/create_choices', 'POST', create_choices),
    Route('/polls', 'GET', polls),
    Route('/polls_details', 'GET', polls_details),
    Route('/vote', 'POST', vote),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]
