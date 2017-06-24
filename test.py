
import os

Dir_path = os.path.abspath(__file__ + "/../")

def test_gitannex():
    with open(os.path.join(Dir_path, "git_annex.txt")) as f:
        con = f.read()

    assert "this should be saved on s3 using git annex" in con

def test_gitonly():
    with open(os.path.join(Dir_path,"git_file.txt")) as f:
        con = f.read()

    assert "this will be just a git file" in con
