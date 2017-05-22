# apistarpoll

Tutorial to run poll app similar to django poll using APISTAR.

Django app tutorial.

https://docs.djangoproject.com/en/1.11/intro/tutorial01/

Step 1: Install Apistar and its dependencies

https://github.com/tomchristie/apistar
 
or

pip install apistar

Step 2: Create new project using apistar

apistar new .

Step 3: The newly created project looks like.

project
|-routes.py
|-views.py
app.py

All the settings can be congigured in app.py

Run the application:

$ apistar run

Running at http://localhost:8080/


Step 4: Install sqlalchemy, for database related stuff.

pip install sqlalcemy 

Step 5: Create a new file in project directory as models.py

Add these lines to the file models.py.

from sqlalchemy.sql import func
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()

class Poll(Base):
	__tablename__ = "Poll"
	id = Column(Integer, primary_key=True)
	question = Column(String)
	pub_date = Column(DateTime(timezone=True), default=func.now())
	# Gives the flexibilty to access child table's object.
	choice = relationship("Choice")

class Choice(Base):
	__tablename__ = "Choice"
	id = Column(Integer, primary_key=True)
	poll = Column(Integer, ForeignKey("Poll.id"), nullable=False)
	choice_text = Column(String)
	votes = Column(Integer)

Configure database settings in app.py

from project.models import Base

settings = {
    "DATABASE": {
    	"URL": "sqlite:///db.sqlite3",
        "METADATA": Base.metadata
    }
}

app = App(routes=routes, settings=settings)

Step 6: Create tables to your database.

$ apistar create_tables

Step 7: You can write logic in views and routing the logic using routes file.

Note:

You can change your port and host using apistar by 
$ apistar run --port <some port> --host <some host>

Default is localhost:8000







