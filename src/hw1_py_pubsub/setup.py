from setuptools import find_packages, setup

package_name = 'hw1_py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='srooney',
    maintainer_email='srooney@wpi.edu',
    description='Sam Rooney - RBE500 HW1',
    license='N/A',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "talker = hw1_py_pubsub.rooney_publisher:main",
            "listener = hw1_py_pubsub.rooney_subscriber:main",
        ],
    },
)
