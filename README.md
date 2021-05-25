# WSL2+Docker+VSCodeのRemote Containersで環境構築

- https://cpp-learning.com/wsl2-docker-vscode/



## フォルダ構成

docker-ml
│──**Dockerfile  #  pyproject.toml で定義した各パッケージを自動でインストールするようにしたDockerfile**

│──**pyproject.toml  # poetryでパッケージ依存を管理。使ってるpoetry環境のpyproject.tomlに置き換えたらいい**

│──docker_run.sh  # Dockerfileたたくシェルスクリプト

│──code

　│──main.py  # サンプル機械学習ソースコード(sklearn)

　│──model  # モデル保存用フォルダ

　└──run_model.sh  # main.py実行するシェルスクリプト



## コマンドラインからコンテナ起動する手順

- wsl2のコマンドプロンプト起動
```bash
$ cd /mnt/c/Users/81908/MyGitHub/docker_ml/docker_ml
$ ./docker_run.sh  # イメージ作成+コンテナ起動
$ cd code/  # コード置いてるディレクトリに移動
$ ./run_model.sh  # モデル学習実行
$ exit  # コンテナから出る
```



## VS Code から Docker に接続する手順（できなかった…）

- VS Codeの左下の「><」で「WSL: Ubuntu」選択（wsl2のもの選ぶ）
- VS Codeの上部のメニューからターミナル開く
- ディレクトリ移動 cd /mnt/c/Users/81908/MyGitHub/docker_ml/docker_ml
- VS Code左下の「><」をクリック
- Reopen in Container を選択
- From Dockerfile を選択
- 左下が「Dev Container: Existing Dockerfile」になったら接続成功



## 前提条件

- windows10
- WSL2インストール済み
- Visual Studio Codeインストール済み
  - VS Code 拡張機能の 「Remote - Containers 」をインストール済み
- Docker Desktopインストール済み
  - WSL2 を利用するチェック入ってる
  <img src="image/docker_desktop.png" alt="docker_desktop" style="zoom:50%;" />



## 環境構築でつまずいたところ

- **vscodeのターミナルは「>< WSL: Ubuntu」を指定しないと WSL2 に接続できない**（他に「>< WSL: Ubuntu-20.04」も選べるがこれはWSL2ではない。これ選択するとdocker コマンドエラーになる）
  ![vscode](image/vscode.png)

