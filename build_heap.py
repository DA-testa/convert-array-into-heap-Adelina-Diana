# python3
# Adelīna Diāna Mālija 221RDB230

def build_heap(data):
    swaps = []
    size = len(data)

    def sift_down(i):
        min_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < size and data[left_child] < data[min_index]:
            min_index = left_child

        if right_child < size and data[right_child] < data[min_index]:
            min_index = right_child

        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]
            swaps.append((i, min_index))
            sift_down(min_index)

    for i in range(size // 2 - 1, -1, -1):
        sift_down(i)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
