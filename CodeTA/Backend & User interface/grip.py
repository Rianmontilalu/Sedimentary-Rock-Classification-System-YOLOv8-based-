import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load gambar
img = cv2.imread('breccia (2).jpg')  # Ganti dengan path file gambar
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Ukuran grid 7x7
h, w = gray.shape
grid_rows, grid_cols = 7, 7
grid_h, grid_w = h // grid_rows, w // grid_cols

# 3. Plot gambar
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# 4. Tambahkan teks dan grid
for row in range(grid_rows):
    for col in range(grid_cols):
        x = col * grid_w
        y = row * grid_h
        roi = gray[y:y+grid_h, x:x+grid_w]
        mean_val = int(np.mean(roi))
        ax.text(x + grid_w // 2, y + grid_h // 2, str(mean_val),
                color='White', ha='center', va='center', fontsize=10)

# 5. Tambahkan garis grid hitam
for i in range(1, grid_rows):
    ax.axhline(i * grid_h, color='white', linewidth=1)
for j in range(1, grid_cols):
    ax.axvline(j * grid_w, color='white', linewidth=1)

# 6. Hilangkan axis
ax.axis('off')

# 7. Simpan hasil ke file
plt.savefig('gambar_dengan_grid.png', bbox_inches='tight')
plt.show()
