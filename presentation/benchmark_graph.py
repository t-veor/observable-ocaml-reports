import matplotlib.pyplot as plt
import numpy as np

labels = ["sieve", "nbody", "mandelbrot", "fibonacci", "collatz"]
asm_means = np.asarray([1.696, 0.285, 1.669, 1.034, 0.43])
gcc_means = np.asarray([0.0, 1.257, 3.388, 1.402, 0.599])
clang_means = np.asarray([1.703, 1.243, 1.561, 1.343, 0.615])

ind = np.asarray([0.25, 1., 2., 3., 4])
width = 0.25

fig, ax = plt.subplots()

ax.grid(True, axis="y", linestyle="--", zorder=0, alpha=0.5)

asm_rects = ax.bar(ind, asm_means, width, zorder=3)
clang_rects = ax.bar(ind + width, clang_means, width, zorder=3)
gcc_rects = ax.bar(ind + 2 * width, gcc_means, width, zorder=3)

ax.set_xticks([0.375, 1.25, 2.25, 3.25, 4.25])
ax.set_xticklabels(labels)

ax.legend([asm_rects[0], clang_rects[0], gcc_rects[0]],
          ["ocamlopt", "clang -O3", "gcc -O3"])

ax.set_ylabel("Average execution time (s)")
ax.set_title("Benchmark execution times")

plt.show()
