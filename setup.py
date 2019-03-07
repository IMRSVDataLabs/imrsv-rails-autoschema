from setuptools import setup


setup(
    name='imrsv-rails-autoschema',
    use_scm_version=True,
    packages=['imrsv.rails_autoschema'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/IMRSVDataLabs/imrsv-rails-autoschema',
    python_requires='>=3.5',
    install_requires=[
        'SQLAlchemy',
        'psycopg2',
        'inflect',
        'IPython',
    ],
    setup_requires=[
        'setuptools_scm',  # for git-based versioning
    ],
    # DO NOT do tests_require; just call pytest or python -m pytest.
    license='License :: Public Domain',
    author='Alex Pilon',
    author_email='alex@imrsv.ai',
    description='IPython/SQLAlchemy/Inflect to mimic `rails c` and'
                ' ActiveRecord DB introspection',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Programming Language :: Python :: 3',
    ],
)
