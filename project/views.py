from apistar import http
from apistar.backends import SQLAlchemy
from .models import Poll, Choice

# def show_request(request: http.Request):
# 	return {
# 		'method': request.method,
# 		'url': request.url,
# 		'headers': dict(request.headers)
# 	}

# def show_query_params(query_params: http.QueryParams):
# 	return {
# 		'params': dict(query_params)
# 	}

# def show_user_agent(user_agent: http.Header):
# 	return {
# 		'user-agent': user_agent
# 	}

def welcome(name=None):
	if name is None:
		return {'message': 'Welcome to API Star!'}
	return {'message': 'Welcome to API Star, %s!' % name}

# def create_customer(db: SQLAlchemy, name: str):
# 	session = db.session_class()
# 	customer = Customer(name=name)
# 	session.add(customer)
# 	session.commit()
# 	return {'name': name}

def create_poll(db: SQLAlchemy, question: str):
	session = db.session_class()
	poll = Poll(question=question)
	session.add(poll)
	session.commit()
	return {'question': question}

