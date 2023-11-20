## dockerコンテナを削除してみよう

## やること
以下のコマンドを実行してみよう。

```bash
docker container rm task-1
docker container ls -a
```

### コマンドの解説
- docker container rm task-1
    - task-1という名前のコンテナを削除する

## 期待結果
以下のようなメッセージが表示されれば成功です。

```
kawasaki.taiga@HAYATE:~$ docker container rm task-1
task-1
kawasaki.taiga@HAYATE:~$ docker container ls -a
CONTAINER ID IMAGE  COMMAND CREATED STATUS PORTS NAMES
kawasaki.taiga@HAYATE:~$
```

