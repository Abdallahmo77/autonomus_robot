from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, RegisterEventHandler
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.event_handlers import OnProcessStart
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import xacro
import os

pkg_name = "diff_bot"


