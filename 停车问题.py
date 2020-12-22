import numpy as np


def smart_method(n, m, ratio=10):
    # N表示把路分成N份
    n = n / (m / ratio)
    n = int(n)
    m = int(ratio)
    f = np.ones(n, dtype=np.float32) * -1

    def go(x):
        x = int(np.clip(x, 0, n - 1))
        if f[x] != -1:
            return f[x]
        if x <= 0:
            return 0
        s = 0
        for i in range(x):
            s += go(i - m // 2) + go(x - i - m // 2) + 1
        f[x] = s / x
        return f[x]

    return go(n)


print(smart_method(1, 0.01, ratio=10))
