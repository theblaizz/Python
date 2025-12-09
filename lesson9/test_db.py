from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://postgres:1@localhost:/postgres"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String)


def test_add_subject():
    session = Session()
    subject = Subject(subject_id=111, subject_title="A_test")
    session.add(subject)
    session.commit()

    saved = session.query(Subject).filter_by(subject_id=111).first()
    assert saved.subject_title == "A_test"

    session.delete(saved)
    session.commit()
    session.close()


def test_update_subject():
    session = Session()
    subject = Subject(subject_id=222, subject_title="B_test")
    session.add(subject)
    session.commit()

    subject.subject_title = "Advanced B_test"
    session.commit()

    updated = session.query(Subject).filter_by(subject_id=222).first()
    assert updated.subject_title == "Advanced B_test"

    session.delete(updated)
    session.commit()
    session.close()


def test_delete_subject():
    session = Session()
    subject = Subject(subject_id=333, subject_title="C_test")
    session.add(subject)
    session.commit()

    session.delete(subject)
    session.commit()

    deleted = session.query(Subject).filter_by(subject_id=333).first()
    assert deleted is None

    session.close()