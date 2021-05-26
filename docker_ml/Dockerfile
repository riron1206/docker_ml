FROM python:3.8

# コンソールのstdout（標準出力）とstderr（標準エラー出力）のバッファーを無効にする設定
ENV PYTHONUNBUFFERED=1

# 各種命令を実行する際のカレントディレクトリを指定
WORKDIR /docker_ml

# poetry のインストール
RUN set -x && \
    curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH /root/.poetry/bin:$PATH

# Poetry は自動で virtualenv を作成し、そこに環境を構築するが Docker内に仮想環境を作ってもしょうがないので virtualenv 作成を falseとする
RUN poetry config virtualenvs.create false

# Poetry で導入したパッケージ(pyproject.toml)を全てインストール
COPY ./pyproject.toml ./
RUN poetry install --no-root --no-dev

# JupyterNotebookの拡張機能を有効化（入力補完, 変数のハイライト機能, 目次）
RUN pip install jupyter_contrib_nbextensions && \
    jupyter contrib nbextension install --user && \
    jupyter nbextension enable highlight_selected_word/main &&\
    jupyter nbextension enable hinterland/hinterland && \
    jupyter nbextension enable toc2/main
