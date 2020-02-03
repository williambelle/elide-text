Contributing
============

Welcome, so you are thinking about contributing?
Awesome, this a great place to start.

Setup
-----

```bash
git clone git@github.com:williambelle/elide-text.git
cd elide-text
```

Test
----

```bash
tox
```

Release
-------

1. Bump the correct version
1. Update the file [CHANGELOG.md](CHANGELOG.md)
1. Create the tag (`git tag -a v<version> -m "Tagging the v<version> release"`)
1. Prepare the package with `python setup.py sdist bdist_wheel`
1. Publish with `twine upload dist/*`

License
-------

The MIT License (MIT)

See the [LICENSE](LICENSE) file for more details.
