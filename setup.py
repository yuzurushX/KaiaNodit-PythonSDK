from setuptools import setup, find_packages

setup(
    name='KaiaNoditSDK',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    author='YuzuRushX',
    author_email='yuzurush.com@gmail.com',
    description='SDK for interacting with Kaia Chain utilizing Nodit API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yuzurushX/KaiaNodit-PythonSDK',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)