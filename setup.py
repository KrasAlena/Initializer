from setuptools import setup, find_packages

setup(
    name='project_initializer',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'initialize_project=project_initializer.initializer:create_project_structure',
        ],
    },
    description='A package to initialize a project structure',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/project_initializer',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)