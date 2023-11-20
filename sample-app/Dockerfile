# コンテナイメージの元になるコンテナイメージを指定
FROM python:3.12.0-slim-bullseye

# 作業するディレクトリを指定
WORKDIR /usr/src/app

# アプリに必要な依存関係が書かれたテキストファイルをコピー
COPY requirements.txt ./
# pipを使って依存関係をインストール
RUN pip install -r requirements.txt

# アプリをコピー
COPY . .

# コンテナ起動時に実行するコマンドの指定
CMD [ "python", "./app.py"]