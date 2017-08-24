from argparse import ArgumentParser

import IPython

import thistoo_autoschema

argument_parser = ArgumentParser(
    description='IPython shell to SQLAlchemy/Rails DB')
argument_parser.parse_args()

# Simple:
#     IPython.start_ipython(user_ns=locals())
# No namespace pollution:
ns = {k: v
      for k, v
      in thistoo_autoschema.__dict__.items()
      if k in thistoo_autoschema.__all__}
# except for all the junk with which IPython pollutes the local namespace.
ns['session'] = thistoo_autoschema.Session()
IPython.start_ipython(user_ns=ns)
