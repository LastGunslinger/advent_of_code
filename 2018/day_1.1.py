from pathlib import Path


def calibrate(input_file: Path, initial_freq: str = 0, ) -> int:
    result_freq = initial_freq
    with open(input_file) as f:
        for freq in f.readlines():
            result_freq += int(freq)
    return result_freq


if __name__ == '__main__':
    freq = calibrate(Path.cwd() / '2018/day_1.txt')
    print(freq)
