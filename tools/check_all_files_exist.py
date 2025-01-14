import os

if __name__ == '__main__':
    train_filepath = "files/filelists/aurimas_nausedas_train_filelist.txt"
    test_filepath = "files/filelists/aurimas_nausedas_test_filelist.txt"
    val_filepath = "files/filelists/aurimas_nausedas_val_filelist.txt"
    with open(train_filepath, mode='r', encoding='utf-8') as f:
        train_filepaths = [line.strip().split('|')[0] for line in f.readlines()]
    with open(test_filepath, mode='r', encoding='utf-8') as f:
        test_filepaths = [line.strip().split('|')[0] for line in f.readlines()]
    with open(val_filepath, mode='r', encoding='utf-8') as f:
        val_filepaths = [line.strip().split('|')[0] for line in f.readlines()]

    filepaths = train_filepaths + test_filepaths + val_filepaths

    for filepath in filepaths:
        if not os.path.exists(filepath):
            print(f"File does not exist: {filepath}")
