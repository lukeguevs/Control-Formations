# # mission/launch/bringup.launch.py
# from launch import LaunchDescription
# from launch_ros.actions import Node

# def generate_launch_description():
#     return LaunchDescription([
#         Node(
#             package='mission',
#             executable='mission/main.py: main()',   # mission/colin_drone_node.py : main()
#             name='lucas_solution',
#             output='screen',
#             parameters=[{'look_ahead' : 2.0},
#                         {'takeoff_alt' : 10.0}]
#         ),
#         Node(
#             package='mission_control',
#             executable='balloon',         # mission_control/ballon_pub.py : main()
#             name='ballon',
#             output='screen',
#         ),
#         Node(
#             package='mission_control',
#             executable='monitor',            # mission_control/monitor.py : main()
#             name='monitor',
#             output='screen',
#         ),
#     ])
