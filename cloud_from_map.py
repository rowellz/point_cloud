import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
# Source: http://www.open3d.org/docs/latest/tutorial/Basic/rgbd_image.html

# monkey patches visualization and provides helpers to load geometries
sys.path.append('..')

#import open3d_tutorial as o3dtut

# Change to true if you want to interact with visualization windows
#o3dtut.interactive = not "CI" in os.environ

# These are the depth mappings prudced by the leres google colab code
#depth_raw_B1 = o3d.io.read_image("/Users/zach/Work/naren/Uconn/midasout_B1C1/depth/13505 - B1 - 2019-11-26 - 14-30.png")
depth_raw = o3d.io.read_image('./depth_map.png')

# These are the depth mappings produced by the MiDAS google colab code
#depth_raw_B1 = o3d.io.read_image("C:\\Users\\nskth.000\\Documents\\GitHub\\Uconn2\\midasout_B1C1\\depth\\37000 - B1 - 2021-04-14 - 14-48.png")
#depth_raw_C1 = o3d.io.read_image("C:\\Users\\nskth.000\\Documents\\GitHub\\Uconn2\\midasout_B1C1\\depth\\37000 - C1 - 2021-04-14 - 14-48.png")


#color_raw_B1 = o3d.io.read_image("/Users/zach/Work/naren/Uconn/images/13505/13505 - B1 - 2019-11-26 - 14-30.jpg")
color_raw = o3d.io.read_image('./image.jpg')

#rgbd_image_B1 = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw_B1, depth_raw_B1)

rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, depth_scale=1000, depth_trunc=20, convert_rgb_to_intensity = False)

print(depth_raw)


print(color_raw)
#print(rgbd_image_C1)

plt.subplot(1, 3, 1)
plt.title('grayscale image')
plt.imshow(rgbd_image.color)


plt.subplot(1, 3, 2)
plt.title('depth image')
plt.imshow(rgbd_image.depth)

plt.subplot(1, 3, 3)
plt.title('depth raw')
plt.imshow(depth_raw)

plt.show()
'''
pcd_B1 = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_image_B1,
    o3d.camera.PinholeCameraIntrinsic(
        o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
'''

pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    rgbd_image,
    o3d.camera.PinholeCameraIntrinsic(
        o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    
# Flip it, otherwise the pointcloud will be upside down
#pcd_B1.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
#pcd_C1.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])

#o3d.visualization.draw_geometries([pcd_B1])
o3d.visualization.draw_geometries([pcd])
