# dockerコンテナを実行してみよう
## やること
以下のコマンドを実行してみよう。

```bash
docker run --name task-1 hello-world
```

### コマンドの解説
- docker run --name task-1 hello-world
    - --name task-1
        - 起動するコンテナの名前をtask-1にするオプション
    - run hello-world
        - hello-worldというコンテナイメージを使用してコンテナを起動するコマンド

## 期待結果
以下のようなメッセージが表示されれば成功。

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
719385e32844: Pull complete
Digest: sha256:c79d06dfdfd3d3eb04cafd0dc2bacab0992ebc243e083cabe208bac4dd7759e0
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

