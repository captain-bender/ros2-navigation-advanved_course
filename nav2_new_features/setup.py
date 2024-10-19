from setuptools import setup

package_name = 'nav2_new_features'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'navigate_to_pose = nav2_new_features.navigate_to_pose:main',
        'navigate_through_poses = nav2_new_features.navigate_through_poses:main',
        'follow_waypoints = nav2_new_features.follow_waypoints:main',
        ],
    },
)
