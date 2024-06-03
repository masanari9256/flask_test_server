# Flaskで作成したテストサーバ

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

## TODO
- コンテナが落ちたときの対策をしていない
- ポートをenvに逃がす
