# init database
from .db import init_db, db_session
from .models import User
init_db()

u = User('admin2', 'admin2@localhost')
db_session.add(u)
db_session.commit()

print(User.query.all())
print(User.query.filter(User.name == 'admin').first())