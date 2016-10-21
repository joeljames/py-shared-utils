from setuptools import find_packages, setup


setup(
    name='pysharedutils',
    version='0.4.0',
    description='Some convenient python utils.',
    author='Joel James',
    author_email='joeljames1985@gmail.com',
    url='',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'six==1.8.0',
        'pytz==2015.4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
