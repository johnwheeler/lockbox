from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]
setup(
    version='0.1',
    name='lockbox',
    url='https://github.com/johnwheeler/lockbox',
    author='John Wheeler',
    author_email='john@johnwheeler.org',
    description='User-friendly symmetric-key cryptography',
    packages=find_packages(),
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'lockbox = lockbox.cli:cli',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
)
