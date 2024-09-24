import numpy as np

for size_b in [7,13]:
    for rank in [8,16,32,64,128]:
        path = f"xin_server_{size_b}b_lora{rank}_a100"
        with open(path) as f:
            lines = [x for x in f.readlines() if "Function load_adapters took" in x]
            times = [float(x.split(" ")[3].strip()) for x in lines]
            print(path, f"\t{np.mean(times):.2f}, {max(times):.2f}, {np.median(times):.2f}")
        
