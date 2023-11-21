## dockerコンテナを削除してみよう

## やること
以下のコマンドを実行してみよう。

```bash
docker container rm task-1
```

### コマンドの解説
- docker container rm [コンテナID or コンテナ名]
    - 今回の例だとtask-1という名前のコンテナを削除する

## 期待結果
以下のようなメッセージが表示されれば成功です。

```
kawasaki.taiga@HAYATE:~$ docker container rm task-1
task-1
kawasaki.taiga@HAYATE:~$
```

