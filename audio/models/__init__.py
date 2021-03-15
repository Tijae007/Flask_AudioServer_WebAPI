from collections import OrderedDict
from json import loads
from pprint import pprint

from psycopg2.extensions import adapt as sqlescape
from sqlalchemy.sql import compiler

from audio import db


# noinspection PyUnresolvedReferences
class HouseKeeping(object):
    def add(self):
        db.session.add(self)
        db.session.commit()

    def named(self):
        return self.__table__.name  # .lower()

    def display(self):
        pprint(loads(json_data(self.__table__.name, self.id)))

    def as_dict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():  # OR self.__table__.columns.keys()
            result[key] = getattr(self, key)
        return result

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.id)

    @classmethod
    def columns(cls):
        return cls.__table__.columns.keys()

    @classmethod
    def relationships(cls):
        """
        Returns a relationship and indicates if it's a list (True) or not
        :return: list
        """
        return [[_, "is_list: {}".format(cls.__mapper__.relationships[_].uselist)] for _ in
                cls.__mapper__.relationships.keys()]

    @classmethod
    def get_field_and_relationships(cls):
        return dict(table_name=cls.__table__.name, columns=cls.columns(), relationships=cls.relationships())


class Base(db.Model, HouseKeeping):
    """Base model that other specific models inherit from"""

    __abstract__ = True

    # BigInteger range: -9223372036854775808 to 9223372036854775807
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)


# noinspection PyArgumentList
def compile_query(query):
    dialect = query.session.bind.dialect
    statement = query.statement
    comp = compiler.SQLCompiler(dialect, statement)
    comp.compile()
    enc = dialect.encoding
    params = {}
    for k, v in comp.params.iteritems():
        if isinstance(v, str):
            v = v.encode(enc)
        params[k] = sqlescape(v)
    return (comp.string.encode(enc) % params).decode(enc)
