import os

scene_dir = "C:/Users/ZODNGUY1/datasets/zeiss"
scenes = ["brain-transparent", "brain-background"]

out_dir = "C:/Users/ZODNGUY1/OneDrive - Carl Zeiss AG/gaussian/repos/2d-gaussian-splatting/output/zeiss"

for scene in scenes:
    print(f"======= Processing scene {scene} =======")
    cmd = f"python train.py -s {scene_dir}/{scene} -m \"{out_dir}/{scene}\" -r 2 --checkpoint_iterations 7000 30000 --depth_ratio 1.0 --lambda_dist 1000"
    print("[>] " + cmd)
    os.system(cmd)
    cmd = f"python render.py -m \"{out_dir}/{scene}\" -s {scene_dir}/{scene} -r 2 --skip_test --depth_ratio 1 --num_cluster 1 --voxel_size 0.004 --sdf_trunc 0.016 --depth_trunc 3.0"
    print("[>] " + cmd)
    os.system(cmd)
    cmd = f"python metrics.py -m \"{out_dir}/{scene}\""
    print("[>] " + cmd)
    os.system(cmd)
    print(f"======= Done with scene {scene_dir}/{scene} =======\n")