import numpy as np


def fill_ndarray(t1):
    for item in range(t1.shape[1]):  # 遍历每一列,只有一个数组的shape代表一维,也就是列
        # print(item)
        temp_col = t1[:, item]  # 当前的一列
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:  # 不等于0,说明当前这一列中有nan
            temp_nan = temp_col[temp_col == temp_col]  # 当前一列不为nan的array
            # temp_nan.mean()  # 当前这一列不为nan的均值
            # 选中当前nan的位置,将其赋值为不为nan的均值
            temp_col[np.isnan(temp_col)] = temp_nan.mean()
    return t1


if __name__ == '__main__':
    # 替换nan为均值
    t1 = np.arange(12).reshape((3, 4)).astype("float")
    t1[1, 2:] = np.nan
    print(t1)
    t1 = fill_ndarray(t1)
    print(t1)
