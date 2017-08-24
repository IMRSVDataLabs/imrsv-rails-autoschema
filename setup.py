from setuptools import setup


setup(
    name='thistoo-autoschema',
    version='0.1',
    install_requires=[
        'SQLAlchemy',
        'psycopg2',
        'inflect',
        'IPython',
    ],
    author='Alex Pilon',
    author_email='alex@miralaw.ca',
    packages=['thistoo_autoschema'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
