# ann-benchmark
将现有的向量的测试数据集转化为csv，用于大家直接获取相关的数据内容：
使用viewwhdf5.py查看各个hdf5里面具体的数据内容，使用hdf5tocsv.py将hdf5转化为csv内容。
数据集内容为：
- train：为总的向量数据集
- test：为查询的数据集内容
- neighbors：用于测试回召率，包括前100个相近的向量数据id
- distance：前100个相似的向量数据之间的距离
