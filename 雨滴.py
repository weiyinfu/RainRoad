import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

"""
长为1m的路，半径为1cm的雨滴，雨滴在路上随机分布，问多少个雨滴才能把路淋湿？
答案应该在725附近
"""


def model_solve(n, m, ratio=10):
    # 路的长度为n，雨滴宽度为m,ratio表示一个雨滴的离散化长度
    n = n / (m / ratio)
    n = int(n)
    m = int(ratio)
    a = np.zeros(n, dtype=np.bool)
    drop = 0
    while np.count_nonzero(a) < n:
        x = np.random.randint(0, n)
        beg = x - m // 2
        end = x + m // 2
        end = min(n, end)
        beg = max(0, beg)
        a[beg:end] = True
        drop += 1
    return drop


def bruteforce_manytimes(n, m, ratio, times):
    ans = []
    for i in tqdm(range(times)):
        ans.append(model_solve(n, m, ratio))
    mu = np.mean(ans)
    sigma = np.std(ans)
    print(f"mu={mu} sigma={sigma}")
    plt.hist(ans, bins=100)
    plt.show()
    return mu


print(bruteforce_manytimes(1, 0.01, ratio=100, times=1000))
