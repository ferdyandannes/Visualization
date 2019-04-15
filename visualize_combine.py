import cv2
import numpy as np
import os
import glob

f = open("Motion/totalmotion.txt", "r")

i = 0
testsite_array = []
object_motion = []
scaling = 4

ego_prev_rotate1 = 0
ego_prev_rotate2 = 0
ego_prev_rotate3 = 0

ego_next_rotate1 = 0
ego_next_rotate2 = 0
ego_next_rotate3 = 0

obj_prev_rotate1 = 0
obj_prev_rotate2 = 0
obj_prev_rotate3 = 0

obj_next_rotate1 = 0
obj_next_rotate2 = 0
obj_next_rotate3 = 0

size = 1000, 1000, 3
blank_image = np.zeros(size, dtype=np.uint8)
scale = 10

traj = np.zeros((1000,1280,3), dtype=np.uint8)

# Guide to the txt files
# ego
# testsite_array[i][0][1] = translation X
# testsite_array[i][1] = translation Y
# testsite_array[i][2] = translation Z
# testsite_array[i][3] = rotation X
# testsite_array[i][4] = rotation Y
# testsite_array[i][5][0] = rotation Z
# testsite_array[i][5][1] = translation X
# testsite_array[i][6] = translation Y
# testsite_array[i][7] = translation Z
# testsite_array[i][8] = rotation X
# testsite_array[i][9] = rotation Y
# testsite_array[i][10] = rotation Z
# object
# testsite_array[i][11] = translation X
# testsite_array[i][12] = translation Y
# testsite_array[i][13] = translation Z
# testsite_array[i][14] = rotation X
# testsite_array[i][15] = rotation Y
# testsite_array[i][16][0] = rotation Z
# testsite_array[i][16][1] = translation X
# testsite_array[i][17] = translation Y
# testsite_array[i][18] =  translation Z
# testsite_array[i][19] = rotation X
# testsite_array[i][20] = rotation Y
# testsite_array[i][21] = rotation Z

for row in f:
	testsite_array.append(row)

for i in range(len(testsite_array)):
	print('')
	print('Frame ', i)
	# Separate the data ego-motion
	testsite_array[i] = testsite_array[i].strip().split(",")
	testsite_array[i][0] = testsite_array[i][0].split()
	testsite_array[i][5] = testsite_array[i][5].split()
	testsite_array[i][16] = testsite_array[i][16].split()

	print(testsite_array[i][0][1], ' ', testsite_array[i][1], ' ', testsite_array[i][2], ' ', testsite_array[i][3], ' '
		, testsite_array[i][4], ' ', testsite_array[i][5][0], ' ', testsite_array[i][5][1], ' ', testsite_array[i][6]
		, ' ', testsite_array[i][7], ' ', testsite_array[i][8], ' ', testsite_array[i][9], ' ', testsite_array[i][10]
		, ' ', testsite_array[i][11], ' ', testsite_array[i][12], ' ', testsite_array[i][13], ' ', testsite_array[i][14]
		, ' ', testsite_array[i][15], ' ', testsite_array[i][16][0], ' ', testsite_array[i][16][1], ' ', testsite_array[i][17]
		, ' ', testsite_array[i][18], ' ', testsite_array[i][19], ' ', testsite_array[i][20], ' ', testsite_array[i][21])

	# EGO PREVIOUS FRAME
	ego_x_prev = float(testsite_array[i][0][1])*scaling
	ego_y_prev = float(testsite_array[i][1])*scaling
	ego_z_prev = float(testsite_array[i][2])*scaling

	ego_rot1_prev = float(testsite_array[i][3])
	ego_rot2_prev = float(testsite_array[i][4])
	ego_rot3_prev = float(testsite_array[i][5][0])

	ego_prev_rotate1 = ego_prev_rotate1 + ego_rot1_prev
	ego_prev_rotate2 = ego_prev_rotate2 + ego_rot2_prev
	ego_prev_rotate3 = ego_prev_rotate3 + ego_rot3_prev

	# EGO NEXT FRAMES
	ego_x_next = float(testsite_array[i][5][1])*scaling
	ego_y_next = float(testsite_array[i][6])*scaling
	ego_z_next = float(testsite_array[i][7])*scaling

	ego_rot1_next = float(testsite_array[i][8])
	ego_rot2_next = float(testsite_array[i][9])
	ego_rot3_next = float(testsite_array[i][10])

	ego_next_rotate1 = ego_next_rotate1 + ego_rot1_next
	ego_next_rotate2 = ego_next_rotate2 + ego_rot2_next
	ego_next_rotate3 = ego_next_rotate3 + ego_rot3_next

	# OBJ PREVIOUS FRAMES
	obj_x_prev = float(testsite_array[i][11])*scaling
	obj_y_prev = float(testsite_array[i][12])*scaling
	obj_z_prev = float(testsite_array[i][13])*scaling

	obj_rot1_prev = float(testsite_array[i][14])
	obj_rot2_prev = float(testsite_array[i][15])
	obj_rot3_prev = float(testsite_array[i][16][0])

	obj_prev_rotate1 = obj_prev_rotate1 + obj_rot1_prev
	obj_prev_rotate2 = obj_prev_rotate2 + obj_rot2_prev
	obj_prev_rotate3 = obj_prev_rotate3 + obj_rot3_prev

	# OBJ NEXT FRAMES
	obj_x_next = float(testsite_array[i][16][1])*scaling
	obj_y_next = float(testsite_array[i][17])*scaling
	obj_z_next = float(testsite_array[i][18])*scaling

	obj_rot1_next = float(testsite_array[i][19])
	obj_rot2_next = float(testsite_array[i][20])
	obj_rot3_next = float(testsite_array[i][21])

	obj_next_rotate1 = obj_next_rotate1 + obj_rot1_next
	obj_next_rotate2 = obj_next_rotate2 + obj_rot2_next
	obj_next_rotate3 = obj_next_rotate3 + obj_rot3_next