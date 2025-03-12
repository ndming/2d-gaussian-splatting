import os

dtu_scenes = ['scan24', 'scan37', 'scan40', 'scan55', 'scan63', 'scan65', 'scan69', 'scan83', 'scan97', 'scan105', 'scan106', 'scan110', 'scan114', 'scan118', 'scan122']
print(f"Number of scenes: {len(dtu_scenes)}")

model_path  = "C:/Users/ZODNGUY1/OneDrive - Carl Zeiss AG/gaussian/repos/2d-gaussian-splatting/output/dtu"
output_path = "C:/Users/ZODNGUY1/repos/2d-gaussian-splatting/output/dtu"

script_dir  = "C:/Users/ZODNGUY1/repos/2d-gaussian-splatting/scripts"
dataset_dir = "C:/Users/ZODNGUY1/datasets/dtu"

for scene in dtu_scenes:
    print(f"== Processing scene {scene} ==")
    script = f"{script_dir}/eval_dtu/evaluate_single_scene.py"
    scan_id = scene[4:]
    ply_file = f"\"{model_path}/{scene}/train/ours_30000/fuse_post.ply\""
    output_dir =  f"{output_path}/{scene}/eval"
    cmd = f"python {script} --input_mesh {ply_file} --scan_id {scan_id} --output_dir {output_dir} --mask_dir {dataset_dir} --DTU {dataset_dir}/Official_DTU_Dataset"
    os.system(cmd)
    print(f"== Done with scene {scene} ==\n")