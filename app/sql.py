from app.models import *


def create_certification(get_id):
    get_all = Certification.query.all()
    for i in get_all:
        db.session.delete(i)

    new_c = Certification(get_id)
    db.session.add(new_c)
    db.session.commit()


def delete_certification():
    get_C = Certification.query.first()
    db.session.delete(get_C)
    db.session.commit()

def get_certification():
    get_C = Certification.query.first()
    if get_C:
        return get_C.id
    else:
        return ''