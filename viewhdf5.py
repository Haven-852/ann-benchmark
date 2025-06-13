import h5py

def print_hdf5_group(group, prefix=''):
    for key in group.keys():
        item = group[key]
        if isinstance(item, h5py.Group):
            print(f"{prefix}Group: {key}")
            print_hdf5_group(item, prefix=prefix + '  ')
        elif isinstance(item, h5py.Dataset):
            data = item[:]
            print(f"{prefix}Dataset: {key}")
            print(f"{prefix}  Shape: {data.shape}")
            print(f"{prefix}  Data type: {data.dtype}")
            if data.size > 0:
                if len(data.shape) == 1:
                    print(f"{prefix}  First 5 elements: {data[:5]}")
                elif len(data.shape) == 2:
                    print(f"{prefix}  First 5 rows:")
                    print(data[:5, :])
                else:
                    print(f"{prefix}  Dataset has more than 2 dimensions, showing first element:")
                    print(data[0])
            else:
                print(f"{prefix}  Dataset is empty")
            print()

def view_hdf5_contents(hdf5_file):
    with h5py.File(hdf5_file, 'r') as f:
        print_hdf5_group(f)

view_hdf5_contents("mnist-784-euclidean.hdf5")