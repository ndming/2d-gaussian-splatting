import os
import json
import shutil
from pathlib import Path


base_dir = Path("output/dtu")
dest_dir = Path("C:/Users/ZODNGUY1/OneDrive - Carl Zeiss AG/gaussian/repos/2d-gaussian-splatting/output/dtu")

count = 0
avg_d2s = 0.0
avg_s2d = 0.0
avg_chamfer = 0.0
for scene in base_dir.iterdir():
    if not scene.is_dir():
        continue

    result_file = scene / "eval" / "results.json"
    if not result_file.exists():
        print(f"[WARNING] Missing result file for {result_file}")
        continue

    with open(result_file, "r") as f:
        result = json.load(f)
        print(f"{scene}:\t {result['overall']:0.2f}")
        avg_d2s += result["mean_d2s"]
        avg_s2d += result["mean_s2d"]
        avg_chamfer += result["overall"]
        count += 1
    
    dest_cp = dest_dir/scene.name/"eval"
    if not dest_cp.exists():
        shutil.copytree(scene/"eval", dest_cp)

if count == 0:
    print("No scene to evaluate")
    exit()

avg_chamfer /= count
avg_d2s /= count
avg_s2d /= count
print(f"Average chamfer: {avg_chamfer:0.2f}")

chamfer = {
    "ours_30000" : {
        "mean_d2s": avg_d2s,
        "mean_s2d": avg_s2d,
        "overall": avg_chamfer
    }
}

export_file = dest_dir / "chamfer.json"
with open(export_file, 'w') as f:
    json.dump(chamfer, f, indent=4)