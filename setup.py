from distutils.core import setup

setup(
    name='sphinx-example',
    version='0.1',
    description="Testing Sphinx with GitHub Pages and readthedocs",
    license='Apache-2.0',
    install_requires=[],
    packages=[
        'sphinx_auto_embed',
        'sphinx_auto_embed.directives',
    ],
    entry_points="""
        [console_scripts]
        sphinx_auto_embed=sphinx_auto_embed.main:main
    """,
    url='https://github.com/vgandari/sphinx-example',
)
