from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='hand_irb',
    version='0.1.0',
    description='Pacote de exemplo para a HandApplication',
    author='Paulo César M. de Menezes',
    author_email='paulo.moraes@sou.unifal-mg.edu.br',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
)
