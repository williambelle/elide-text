import io
import setuptools

setuptools.setup(
    name="elide-text",
    version="0.0.1",
    url="https://github.com/williambelle/elide-text",
    author="William Belle",
    author_email="william.belle@gmail.com",
    description="A very simple text truncating function",
    long_description=io.open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
