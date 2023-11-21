# コンテナ一覧を表示してみよう
## やること
以下のコマンドを実行してみよう。

```bash
docker container ls -a
docker run --name task-3 hello-world
docker container ls -a
```

### コマンドの解説
- docker container ls -a
    - -a
        - 現在起動していないコンテナも表示するオプション
    - container ls
        - コンテナ一覧を表示するコマンド

## 期待結果
以下のようなメッセージが表示されれば成功です。

```
kawasaki.taiga@HAYATE:~$ docker container ls -a
CONTAINER ID IMAGE  COMMAND CREATED STATUS PORTS NAMES
kawasaki.taiga@HAYATE:~$ docker run --name task-3 hello-world
--中略--
kawasaki.taiga@HAYATE:~$ docker container ls -a
CONTAINER ID   IMAGE         COMMAND    CREATED       STATUS                   PORTS     NAMES
a43c5254d11a   hello-world   "/hello"   5 hours ago   Exited (0) 5 hours ago             task-3
kawasaki.taiga@HAYATE:~$
```

### 出力の解説
- CONTAINER ID
    - コンテナのID
- IMAGE
    - コンテナの元となったイメージ
- COMMAND
    - コンテナ起動直後に実行されるコマンド
- STATUS
    - コンテナの状態
- PORTS
    - コンテナが使用しているポート
    - もしくは、ホストとコンテナのポートのマッピング
- NAMES
    - コンテナの名前


