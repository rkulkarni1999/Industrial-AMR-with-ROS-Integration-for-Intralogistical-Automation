#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
waypoints = [
[(6.0, -15.0, 0.0), (0.0, 0.0, 1.0, 0.124)],
[(5.0, -15.0, 0.0), (0.0, 0.0, 0.75, 0.664)],
[(4.0, -11.0, 0.0), (0.0, 0.0, 1.0, 0.124)],
[(-3.0, -11.0, 0.0), (0.0, 0.0, 0.75, 0.769)] ]
#[(-6.0, -6.0, 0.0), (0.0, 0.0, -0.1, 0.079)],
#[(-12.0, -6.0, 0.0), (0.0, 0.0, 0.75, 0.682)],
#[(-8.2, 6.0, 0.0), (0.0, 0.0, 0.0, 1.0)]
#]

def goal_pose(pose):
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = pose[0][0]
    goal_pose.target_pose.pose.position.y = pose[0][1]
    goal_pose.target_pose.pose.position.z = pose[0][2]
    goal_pose.target_pose.pose.orientation.x = pose[1][0]
    goal_pose.target_pose.pose.orientation.y = pose[1][1]
    goal_pose.target_pose.pose.orientation.z = pose[1][2]
    goal_pose.target_pose.pose.orientation.w = pose[1][3]
    return goal_pose

while not rospy.is_shutdown():

    rospy.init_node('patrol')
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()
    while True:
        for pose in waypoints:
            goal = goal_pose(pose)
            client.send_goal(goal)
            client.wait_for_result()


