# WSL2+Docker+poetryで環境構築

- 参考: https://cpp-learning.com/wsl2-docker-vscode/



## フォルダ構成

docker-ml

│──**Dockerfile  #  pyproject.toml で定義した各パッケージを自動でインストールするようにしたDockerfile**

│──**pyproject.toml  # poetryでパッケージ依存を管理。使ってるpoetry環境のpyproject.tomlに置き換えたらいい**

│──docker_run.sh  # Dockerfileたたくシェルスクリプト

│──docker_ml

　│──※環境構築コマンド履歴.txt  # Dockerでpyproject.toml作る手順とかのメモ
　│──code

　　│──main.py  # サンプル機械学習ソースコード(sklearn)

　　│──model  # モデル保存用フォルダ

　　└──run_model.sh  # main.py実行するシェルスクリプト



## コマンドラインからコンテナ起動する手順

- wsl2のコマンドプロンプト起動
```bash
$ cd /mnt/c/Users/81908/MyGitHub/docker_ml/docker_ml
$ ./docker_run.sh  # イメージ作成+コンテナ起動
$ cd docker_ml/code/  # コード置いてるディレクトリに移動
$ ./run_model.sh  # モデル学習予測実行
$ cd ../notebok
$ jupyter lab --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token='' --port=8889  # http://localhost:8889/ からjupyter起動確認
$ exit  # コンテナから出る
```



※wsl2+Dockerはめちゃめちゃメモリを食うので微妙かも…

- https://zenn.dev/takajun/articles/4f15d115548899





-------------------------------------------------------------------------------------------------------------------





## VS Code から Docker に接続する手順（できなかった…）

- VS Codeの左下の「><」で「WSL: Ubuntu」選択（wsl2のもの選ぶ）
- VS Codeの上部のメニューからターミナル開く
- ディレクトリ移動 cd /mnt/c/Users/81908/MyGitHub/docker_ml/docker_ml
- VS Code左下の「><」をクリック
- Reopen in Container を選択
- From Dockerfile を選択
- 左下が「Dev Container: Existing Dockerfile」になったら接続成功



### 前提条件

- windows10
- WSL2インストール済み
- Visual Studio Codeインストール済み
  - VS Code 拡張機能の 「Remote - Containers 」をインストール済み
- Docker Desktopインストール済み
  - WSL2 を利用するチェック入ってる
  <img src="image/docker_desktop.png" alt="docker_desktop" style="zoom:50%;" />



### つまずいたところ

- **vscodeのターミナルは「>< WSL: Ubuntu」を指定しないと WSL2 に接続できない**（他に「>< WSL: Ubuntu-20.04」も選べるがこれはWSL2ではない。これ選択するとdocker コマンドエラーになる）
  ![vscode](image/vscode.png)

