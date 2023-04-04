# Brute force

Decrypting ciphertexts is a common task in cryptography.
This problem provides a ciphertext and the key length.
Given the short length of the key, one solution is to try all possible keys and see which one gives a plaintext that makes sense.
However, since I'm too lazy to check all the outputs, let's think about it a bit more.

[Frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis) is a method used to break simple substitution ciphers.
Counting the number of occurrences of each character in the ciphertext and comparing it with the frequencies of the letters in the English language can give some clues about the plaintext.
As 'e' is the most common letter in English, the most common letter in the ciphertext is likely to be 'e'.

To find the key, the first step is to split the ciphertext into blocks of length equal to the key length.
Then, applying XOR to the most common character in each block with 'e' should give each block's key.

The first step is to parse the ciphertext and get a list of integers to apply XOR to.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0059/solution1.py):

```python
def parse_file():
    with open("cipher.txt", "r") as f:
        return [int(x) for x in f.read().split(",")]
```

Using [collections.Counter.most_common](https://docs.python.org/3/library/collections.html#collections.Counter.most_common) to determine the most common character in each block and [itertools.cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle) to iterate over the key repeatedly will be helpful.
Lastly, applying XOR operations between each character in the ciphertext and the corresponding character of the key gives the plaintext.

Due to the nature of the text, the most frequent character is more likely to be ' ' (space) than 'e'.
This is because the ciphertext is an English text, as a result, applying XOR using ' ' to the most common character in each block yields the correct solution.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0059/solution1.py):

```python
def xor_decryption():
    code = parse_file()
    k1 = Counter(code[::3]).most_common(1)[0][0] ^ ord(" ")
    k2 = Counter(code[1::3]).most_common(1)[0][0] ^ ord(" ")
    k3 = Counter(code[2::3]).most_common(1)[0][0] ^ ord(" ")
    key = [k1, k2, k3]
    res = [chr(c ^ p) for (c, p) in zip(parse_file(), itertools.cycle(key))]
    return sum(ord(c) for c in res)
```
