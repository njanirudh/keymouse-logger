from setuptools import setup, find_packages

setup(
    name='keymouse_logger',
    version='0.1.0',
    description='A background key and mouse input logger with heatmap visualization',
    author='Anirudh',
    author_email='anijaya9@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pynput',
        'matplotlib',
        'seaborn',
    ],
    entry_points={
        'console_scripts': [
            'keymouse-logger=key_mouse_logger:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
)
