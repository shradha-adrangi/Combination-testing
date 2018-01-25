"""
Installs this project into site packages.
"""

if __name__ == '__main__':
    import os
    import subprocess
    abs_path = os.path.dirname(os.path.abspath(__file__))
    print('Installing `crqasoap` from `{}` to local site packages.'.format(abs_path))
    subprocess.call(['pip', 'install', '--upgrade', '--force-reinstall', '--no-deps', abs_path], shell=True)
