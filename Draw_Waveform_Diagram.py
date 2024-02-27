import h5py
import numpy as np
import matplotlib.pyplot as plt

# SCM_path = r"D:\postgraduate\project\whistler_SVD\MatLab_SVD\data\new_h5\CSES_01_SCM_2_L02_A2_129180_20200601_014651_20200601_022217_000.h5"
SCM_path = r"E:\data\SCM\CSES_01_SCM_2_L02_A2_109751_20200125_063920_20200125_071453_000.h5"
dataset = h5py.File(SCM_path)

scm_data = dataset['A243_W']
waveform_data = scm_data[3580:3590, :]
waveform_data = waveform_data.flatten()
# 采样率
sampling_rate = 10240

# 计算时间轴
t = np.arange(0, 40960) / sampling_rate

plt.figure(figsize=(10, 6))

# 绘制波形图
plt.plot(t, waveform_data)

# 添加标题和标签
plt.title('Waveform Plot')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude(T)')

# 显示图形
plt.show()
