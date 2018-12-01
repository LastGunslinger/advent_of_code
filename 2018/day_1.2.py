from pathlib import Path


def calibrate(input_file: Path, initial_freq: str = 0, ) -> int:
    with open(input_file) as f:
        freq_inputs = list(f.readlines())

    freq_list = [initial_freq]
    result_freq = initial_freq
    while True:
        for freq in freq_inputs:
            result_freq += int(freq)
            if result_freq in freq_list:
                return result_freq
            else:
                freq_list.append(result_freq)


if __name__ == '__main__':
    freq = calibrate(Path.cwd() / '2018/day_1.txt')
    print(freq)
