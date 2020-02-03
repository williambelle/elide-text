elide-text
==========

[![Build Status][travis-image]][travis-url]
[![Coverage Status][codecov-image]][codecov-url]
[![Requirements Status][requires-image]][requires-url]

A very simple text truncating function.

Install
-------

```bash
pip install elide-text
```

Usage
-----

```python
from elidetext import elide_text

text = elide_text("A brand new tool devoted to complex neuron models", 25)
print(text) #=> A brand new tool devoted…

text = elide_text("🍺📰📚🍮🌵📴🎯🌿👂👓👌", 6)
print(text) #=> 🍺📰📚🍮🌵…
```

Contributing
------------

Contributions are always welcome.

See [Contributing](CONTRIBUTING.md).

Developer
---------

* [William Belle](https://github.com/williambelle)

License
-------

The MIT License (MIT)

[travis-image]: https://travis-ci.org/williambelle/elide-text.svg?branch=master
[travis-url]: https://travis-ci.org/williambelle/elide-text
[codecov-image]:https://codecov.io/gh/williambelle/elide-text/branch/master/graph/badge.svg
[codecov-url]:https://codecov.io/gh/williambelle/elide-text
[requires-image]:https://requires.io/github/williambelle/elide-text/requirements.svg?branch=master
[requires-url]:https://requires.io/github/williambelle/elide-text/requirements/?branch=master
