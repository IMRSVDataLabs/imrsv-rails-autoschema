'''
Fully automatic SQLAlchemy introspection of Rails DB.
'''

from os import environ
import re

from sqlalchemy.ext.automap import automap_base
import sqlalchemy.orm as orm
import sqlalchemy as sa

import inflect


_pluralizer = inflect.engine()


# Adapted from
# http://docs.sqlalchemy.org/en/latest/orm/extensions/automap.html#overriding-naming-schemes
def _singularize_classname(base, tablename, table):
    return _pluralizer.singular_noun(_camelcase(tablename))


def _camelcase(s):
    return re.sub(r'_(\w)',
                  lambda m: m.group(1).upper(),
                  s.capitalize())


engine = sa.create_engine(environ['DATABASE_URL'])
AutomapBase = automap_base()
AutomapBase.prepare(engine,
                    reflect=True,
                    classname_for_table=_singularize_classname)
Session = orm.sessionmaker(engine)


__all__ = 'Session',


for _class_name, _class in AutomapBase.classes.items():
    if _class_name not in dir():
        locals()[_class_name] = _class
        __all__ = __all__ + (_class_name,)
