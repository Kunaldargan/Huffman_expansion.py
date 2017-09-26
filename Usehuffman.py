from huffman import HuffmanCoding

#input file path
path = "C:\\Users\\DELL1\\Desktop\\huffman\\sample.txt"

h = HuffmanCoding(path)

output_path = h.compress()
h.decompress(output_path)
