# point_cloud

The purpose of this repo is to demonstrate how we can use monocular depth estimation to create reltivley accurate point clouds in both real time (at lower accuracy levels) and in delayed time (with significantly more accurate output). See lines 9, 10, & 11 in `depth.py` for more details. 

In order to view the point clouds in the open3d enviornment, please run `depth_image.py`. This program will produce an rgb image and a depth map image from your webcam upon hitting the `enter` key in the terminal. 

Once said images are produced, run `cloud_from_map.py` to view the point cloud in a 3d enviornment. 
