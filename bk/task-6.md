# Dockerイメージを利用してhttpサーバを立ち上げよう

## やること
以下のコマンドを実行してみよう。

```bash
docker exec -it [コンテナID or コンテナ名] bash
curl http://localhost
exit
```

### コマンドの解説
- docker exec -it [コンテナID or コンテナ名] bash
   - 指定したコンテナ内でコマンドを実行するためのオプション
   - -i
      - 入力をbashに渡すためのオプション
   - -t
      - 出力をターミナルに表示するためのオプション
   - bash
      - ここではコンテナ内で実行するコマンドとしてbashを指定している
- curl http://localhost
   - http://localhostにHTTP GETリクエスト送ってレスポンスを表示するコマンド
- exit
   - コンテナ内で実行されているbashを終了するためのコマンド

## 期待結果
以下のようなメッセージが表示されれば成功。

```
kawasaki.taiga@HAYATE:~$ docker exec -it nervous_hugle bash
root@d80478295182:/# curl http://localhost
<!DOCTYPE html>
<html>
--中略--
</html>
root@d80478295182:/# exit
exit
```

