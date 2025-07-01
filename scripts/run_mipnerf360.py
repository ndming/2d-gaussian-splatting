import os

scene_dir = "/home/zodnguy1/datasets/mipnerf360"

scenes = ["bicycle", "flowers", "garden", "stump", "treehill", "room", "counter", "kitchen", "bonsai"]
factors = [4, 4, 4, 4, 4, 2, 2, 2, 2]

out_dir = "output/mipnerf360"

for scene, factor in zip(scenes, factors):
    print(f"======= Processing scene {scene} with factor {factor} =======")

    cmd = f"python train.py -s {scene_dir}/{scene} -m {out_dir}/{scene} -i images_{factor} --eval --checkpoint_iterations 7000 30000"
    os.system(cmd)

    cmd = f"python render.py -m {out_dir}/{scene} --eval --skip_train --iteration 30000"
    os.system(cmd)

    cmd = f"python metrics.py -m {out_dir}/{scene}"
    os.system(cmd)

    print(f"======= Done with scene {scene_dir}/{scene} =======")
