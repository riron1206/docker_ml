# WSL2+Docker+poetry�Ŋ��\�z

- �Q�l: 
  - https://cpp-learning.com/wsl2-docker-vscode/
  - https://wimper-1996.hatenablog.com/entry/2020/10/14/114458
  - https://qiita.com/yolo_kiyoshi/items/332ae902aeb730fbd068



## �f�B���N�g���\��

```
docker-ml
������Dockerfile      #  pyproject.toml �Œ�`�����e�p�b�P�[�W�������ŃC���X�g�[������悤�ɂ���Dockerfile
������pyproject.toml  # poetry�Ńp�b�P�[�W�ˑ����Ǘ��B�g���Ă�poetry����pyproject.toml�ɒu���������炢��
������docker_ml
�@�����������\�z�R�}���h����.txt  # Docker��pyproject.toml���菇�Ƃ��̃���
�@������tests          # �e�X�g�R�[�h
�@�@������main.py       # �T���v���@�B�w�K�\�[�X�R�[�h(sklearn)
�@�@������model         # ���f���ۑ��p�t�H���_
�@�@������run_model.sh  # main.py���s����V�F���X�N���v�g
�@������my_package     # �p�b�P�[�W�����������W���[��
�@������notebook       # EDA�Ŏg�p����notebook
�@������streamlit_app  # streamlit��app
```



## �R�}���h���C������R���e�i�N������菇

- wsl2�̃R�}���h�v�����v�g�N��
```bash
$ cd ./docker_ml

# �C���[�W�쐬
$ docker build -t docker_ml -f Dockerfile .

# �R���e�i�N��
$ docker run -p 8889:8889 -p 8502:8502 -it -v $PWD/docker_ml:/docker_ml --rm docker_ml /bin/bash

# �e�X�g�R�[�h�u���Ă�f�B���N�g���Ɉړ����ă��f���w�K�\�����s
$ cd tests/
$ ./run_model.sh
 
# http://localhost:8502/ ����streamlit�N���m�F
$ cd ..
$ streamlit run streamlit_app/app.py --server.port 8502

# http://localhost:8889/ ����jupyter�N���m�F
$ jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token='' --port=8889
notebook/test.ipynb ���s�imlflow�̃t�@�C���o�́j

# http://localhost:8502/ ����mlflow�N���m�F
$ cd notebook/
$ mlflow ui --port 8502 --host 0.0.0.0

# �R���e�i����o��
$ exit
```



��wsl2+Docker�͂߂���߂��Ⴡ������H���̂Ŕ��������c

- https://zenn.dev/takajun/articles/4f15d115548899





-------------------------------------------------------------------------------------------------------------------





## VS Code ���� Docker �ɐڑ�����菇�i�ł��Ȃ������c�j

- VS Code�̍����́u><�v�ŁuWSL: Ubuntu�v�I���iwsl2�̂��̑I�ԁj
- VS Code�̏㕔�̃��j���[����^�[�~�i���J��
- �f�B���N�g���ړ� cd /mnt/c/Users/81908/MyGitHub/docker_ml/docker_ml
- VS Code�����́u><�v���N���b�N
- Reopen in Container ��I��
- From Dockerfile ��I��
- �������uDev Container: Existing Dockerfile�v�ɂȂ�����ڑ�����



### �O�����

- windows10
- WSL2�C���X�g�[���ς�
- Visual Studio Code�C���X�g�[���ς�
  - VS Code �g���@�\�� �uRemote - Containers �v���C���X�g�[���ς�
- Docker Desktop�C���X�g�[���ς�
  - WSL2 �𗘗p����`�F�b�N�����Ă�
  <img src="image/docker_desktop.png" alt="docker_desktop" style="zoom:50%;" />



### �܂������Ƃ���

- **vscode�̃^�[�~�i���́u>< WSL: Ubuntu�v���w�肵�Ȃ��� WSL2 �ɐڑ��ł��Ȃ�**�i���Ɂu>< WSL: Ubuntu-20.04�v���I�ׂ邪�����WSL2�ł͂Ȃ��B����I�������docker �R�}���h�G���[�ɂȂ�j
  ![vscode](image/vscode.png)

