import setuptools

TEST_REQUIRES = [
    # testing and coverage
    'pytest', 'coverage', 'pytest-cov',
]

setuptools.setup(
    name="mypkg",
    version="0.0.1",
    author="Daniel Xu",
    author_email="danielgg.coding@email",
    url="http://www.test.org",
    packages=['mypkg', 'mypkg.transform'],
    extras_require={
        'test': TEST_REQUIRES,
    },
)
