from collections import defaultdict, Counter


def huffman_coding(string: str):
    """
    哈夫曼编码，现代压缩算法的基础
    :param string:
    :return:
    """
    huffman_dict = defaultdict(str)
    huffman_counter = Counter()
    huffman_reverse_counter = Counter()
    huffman_counter.update(string)
    for key, value in huffman_counter.items():
        huffman_reverse_counter[key] = 1 / value

    while len(huffman_reverse_counter) > 1:
        top_item = huffman_reverse_counter.most_common(2)
        top_1_key, top_1_value = top_item[0]
        top_2_key, top_2_value = top_item[1]
        huffman_dict[top_1_key] += '0'
        huffman_dict[top_2_key] += '1'
        huffman_reverse_counter.pop(top_1_key, top_2_key)
    return huffman_reverse_counter


if __name__ == "__main__":
    String = "AAAABBBBBBCCCDDE"
    rst = huffman_coding(String)
