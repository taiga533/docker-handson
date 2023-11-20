# コンテナ一覧を表示してみよう
## やること
以下のコマンドを実行してみよう。

```bash
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
CONTAINER ID   IMAGE         COMMAND    CREATED       STATUS                   PORTS     NAMES
a43c5254d11a   hello-world   "/hello"   5 hours ago   Exited (0) 5 hours ago             task-1
kawasaki.taiga@HAYATE:~$
```

