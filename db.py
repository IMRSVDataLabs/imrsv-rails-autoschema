#! /usr/bin/env python3

'''
Fully automatic SQLAlchemy introspection of Rails DB.
'''

# Dependencies:
# - SQLAlchemy
# - psycopg2
# - IPython
# - inflect

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


if __name__ == '__main__':
    from argparse import ArgumentParser

    import IPython

    argument_parser = ArgumentParser(
        description='IPython shell to SQLAlchemy/Rails DB')
    argument_parser.parse_args()

    # Simple:
    #     IPython.start_ipython(user_ns=locals())
    # No namespace pollution:
    ns = {k: v
          for k, v
          in locals().items()
          if k in __all__}
    # except for all the junk with which IPython pollutes the local namespace.
    ns['session'] = Session()
    IPython.start_ipython(user_ns=ns)
