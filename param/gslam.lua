------
-- Google Cartographer Configuration
--

-----
-- Includes the default option values.
--
-- Files can be found in
-- $ roscd cartographer/configuration_files/
--
-- pose_graph.lua           : Global SLAM settings (graph optimization, loop closures)
-- trajectory_builder_2d.lua: Local  SLAM settings (submap  creation)
--
include "map_builder.lua"
include "trajectory_builder.lua"

------
-- Documentation for following options
-- https://google-cartographer-ros.readthedocs.io/en/latest/configuration.html
--
options = {
  map_builder        = MAP_BUILDER,
  trajectory_builder = TRAJECTORY_BUILDER,

  ------
  -- Tf
  --
  map_frame       = "map",
  tracking_frame  = "laser",
  published_frame = "base_link",
  odom_frame      = "odom",

  lookup_transform_timeout_sec  = 0.2,
  provide_odom_frame            = false,
  publish_frame_projected_to_2d = true,

  ------
  -- Pose Extrapolator
  --
  -- Used to generate initial guesses for scan matching. The guess can be derived from
  -- different sensor inputs.
  use_pose_extrapolator = false,

  ------
  -- Sensor inputs
  --
  -- Range data (Laser Scans & Point Clouds)
  -- Required topics:
  -- Laser Scans          : scan   (sensor_msgs/LaserScan)
  -- Multi Echo Laser Scan: echo   (sensor_msgs/MultiEchoLaserScan)
  -- Point Clouds         : points (sensor_msgs/PointCloud2)
  -- Multiple inuputs     : <topic>_1, <topic>_2, ...
  num_laser_scans                 = 1,
  num_multi_echo_laser_scans      = 0,
  num_point_clouds                = 0,

  num_subdivisions_per_laser_scan = 1,
  
  -- Odometry
  -- Required topic: odom (nav_msgs/Odometry)
  use_odometry = false,

  -- GPS
  -- Required topic: fix (sensor_msgs/NavSatFix)
  use_nav_sat = false,

  -- Landmarks
  -- Required topic: landmark (cartographer_ros_msg/LandmarkList)
  use_landmarks = false,

  -- IMU
  -- Required topic: ? (sensor_msg/IMU)
  -- De/Activated in the local SLAM settings
  
  ------
  -- Sampling ratios
  --
  rangefinder_sampling_ratio      = 1.,
  odometry_sampling_ratio         = 1.,
  imu_sampling_ratio              = 1.,
  landmarks_sampling_ratio        = 1.,
  fixed_frame_pose_sampling_ratio = 1., 

  ------
  -- Publishing periods
  --
  submap_publish_period_sec     = 0.3,
  pose_publish_period_sec       = 5e-3,
  trajectory_publish_period_sec = 30e-3,
}

------
-- Documentation for following options
-- https://google-cartographer.readthedocs.io/en/latest/configuration.html
--

------
-- Map Builder Options
--
-- 2D maps
MAP_BUILDER.use_trajectory_builder_2d = true

------
-- Global SLAM
--
-- Searches for loop closures and performs optimizations in order to best arrange the submaps
-- into an overall map.
--
-- Global SLAM triggered evary n nodes. Set to 0 to deactivate it.
POSE_GRAPH.optimize_every_n_nodes = 60

------
-- Local SLAM
--
-- Creates submaps.
--
-- Sets whether to use IMU data.
TRAJECTORY_BUILDER_2D.use_imu_data = false
-- Sets how many range scans should be accumulated before scan matching. Set to 1, if you wish to
-- only use laser scans.
TRAJECTORY_BUILDER_2D.num_accumulated_range_data = 1

-- Creates initial guesses for scan matching.
TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching = true
TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.linear_search_window = 0.1
TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.angular_search_window = math.rad(20.)
-- Weights: ? Not documented.
--TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.translation_delta_cost_weight = 1e-1
--TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher.rotation_delta_cost_weight = 1e-1

-- Scan Matching
TRAJECTORY_BUILDER_2D.ceres_scan_matcher.ceres_solver_options.max_num_iterations = 30
TRAJECTORY_BUILDER_2D.ceres_scan_matcher.ceres_solver_options.num_threads = 1
-- Weighting: the higher the number the more costly it is for the matcher to deviate from the initial guess.
--TRAJECTORY_BUILDER_2D.ceres_scan_matcher.translation_weight = 10
--TRAJECTORY_BUILDER_2D.ceres_scan_matcher.rotation_weight    = 10

------
-- Probability Grid
--
-- Set grid type.
TRAJECTORY_BUILDER_2D.submaps.grid_options_2d.grid_type  = "PROBABILITY_GRID"
-- Resolution in meter.
TRAJECTORY_BUILDER_2D.submaps.grid_options_2d.resolution = 0.05
-- Set the range data inserter for the probability grid.
TRAJECTORY_BUILDER_2D.submaps.range_data_inserter.range_data_inserter_type = "PROBABILITY_GRID_INSERTER_2D"


return options