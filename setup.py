from setuptools import setup, find_packages

setup(
    name='auto_dungeon_master',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        dnd=auto_dm.scripts.dnd:cli
    ''',
)