# Flaskで作成したテストサーバ

## 概要
localhost:81/test に対してGETリクエストを送ると、疎通確認ができる  
```shell
curl -X GET http://localhost:81/test
```
localhost:81/test に対してPOSTリクエストを送ると、データをPOST投稿できる  
```shell
curl -X POST http://localhost:81/test -H "Content-Type: application/json" -d '{"key1": "value1", "key2": "value2"}'
```
localhost:81/display に対してGETリクエストを送ると、HTMLでデータを確認できる

[http://localhost:81/display](http://localhost:81/display)

## 起動方法
```shell
make setup
```

## システム構成構成
Python 3.11.7  
Flask 3.0.3


## TODO
- コンテナが落ちたときの対策をしていない
- ポートをenvに逃がす
