Nothing to see here since it's all introspected.
This needn't be a private repo.

You could adapt this to another project, and probably will want to if your
relationships are not trivial. This is meant for stupid Rails schemas.

## Installation ##

```sh
pip install --user git+https://github.com/IMRSVDataLabs/imrsv-rails-autoschema
```

## Usage ##

Enjoy inside your Rails environment with `DATABASE_URL` set to the
PostgreSQL DB URL.

```sh
DATABASE_URL=postgres://… python -m imrsv.rails_autoschema
# or, if already exported
python -m imrsv.rails_autoschema
```

## Compatibility ##

Should work with Rails 4 and Rails 5. Not tested on previous
versions. Well, should work with any DB for which SQLAlchemy and your
installed dependencies support introspection.

The DB schema must use plural, underscored (no `PascalCase`, no `camelCase`, no
whatever). Rails does that for you. E.g.:

	people
	users
	posts
	comments
