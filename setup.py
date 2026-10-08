from setuptools import find_packages, setup

package_name = 'batiproject_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='juan-lopez',
    maintainer_email='jclopezdecastro0201@gmail.com',
    description='Proyecto ROS2 para control de robot por joystick y WiFi',
    license='Apache-2.0',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'control = batiproject_pkg.Joy:main',
            'monitor = batiproject_pkg.monitor:main',
            'wifi = batiproject_pkg.wifi:main',
            'audio = batiproject_pkg.Audio:main',
            'decision = batiproject_pkg.Decision:main',
        ],
    },
)