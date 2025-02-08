from tinydb import TinyDB, Query
from models import User

db = TinyDB('./database.json', indent=2)


def get_all_users() ->list[User]:
    users = db.table('users').all()

    return[User(**user)for user in users]






