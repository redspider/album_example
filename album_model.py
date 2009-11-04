
from album.model import get_executor, _dlog
from sqlalchemy.exceptions import IntegrityError

def add_album(actor, name, public, owner):
    conn = get_executor()
    conn.call("add_album", actor, name, public, owner)
    conn.commit()