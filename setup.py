# Install required Python packages
from setuptools import setup, find_packages

setup(
    name='South-Africa-Apartheid-Truth-and-Reconciliation',
    version='0.1',
    url='https://github.com/crown-of-napoleon/South-Africa-Apartheid-Truth-and-Reconciliation',
    author='Author Name',
    author_email='author@gmail.com',
    description='Description of my package',
    packages=find_packages(),    
    install_requires=[
        'numpy >= 1.19.5',
        'pandas >= 1.1.5',
        'scikit-learn >= 0.24.2',
        'Pillow >= 8.2.0',
        'tensorflow >= 2.5.0',
        'matplotlib >= 3.4.2',
        'requests >= 2.25.1',
        'unittest2 >= 1.1.0'
    ],
)
