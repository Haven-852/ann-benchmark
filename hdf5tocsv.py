import h5py
import pandas as pd
import numpy as np

# HDF5 文件路径
hdf5_file = "sift-128-euclidean.hdf5"

# 打开 HDF5 文件
with h5py.File(hdf5_file, 'r') as f:
    # 遍历所有顶级键（dataset 名称）
    for dataset_name in f.keys():
        print(f"正在处理数据集: {dataset_name}")
        
        # 读取整个 dataset 到内存
        data = f[dataset_name][:]
        
        # 转换为 Pandas DataFrame
        df = pd.DataFrame(data)
        
        # 构造 CSV 文件名并保存
        csv_filename = f"{dataset_name}.csv"
        df.to_csv(csv_filename, index=False)
        
        print(f"已保存到 {csv_filename}，形状为 {data.shape}")

print("转换完成！")