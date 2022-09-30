import setuptools

setuptools.setup(
    name="init-python",
    version="0.0.1",
    author="Cleiton Correa",
    author_email="cleitoncorreadeveloper@gmail.com",
    description="Project Application Course Data Science IBM",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[],
    entry_points={
            'console_scripts': [
                'app = init.bin.app:main'
            ],
        },
)
