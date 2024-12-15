from setuptools import setup

setup(
    name='mon_projet',
    version='0.1',
    packages=['script_perso.charger', 'script_perso.rapport', 'script_perso.recherche'],  # Remplace avec les packages de ton projet
    include_package_data=True,
    install_requires=[
        'django',
        # Ajoute d'autres dépendances si nécessaire
    ],
    entry_points={
        'console_scripts': [
            'mon_projet = script_perso.main:execute_from_command_line',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)
