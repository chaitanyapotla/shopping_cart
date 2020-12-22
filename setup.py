import os

from setuptools import setup, find_packages

script_dir = os.path.dirname(os.path.realpath(__file__))

setup(
    name='shoppingcart',
    version='0.0',
    packages=find_packages(),
    package_data={x: ['*.json', '*.txt'] for x in find_packages()},
    include_package_data=True,
    install_requires=open(os.path.join(script_dir, 'requirements.txt')).readlines(),
    entry_points={
        'console_scripts': [
            'addToCart = cart.addtocart:main'
        ]
    }
)
