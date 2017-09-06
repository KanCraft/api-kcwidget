# api-kcwidget

[艦これウィジェット](https://github.com/otiai10/kanColleWidget)のAPIサーバです。Dockerが使える環境で開発・デプロイができます。

公開版『艦これウィジェット』が利用している公式のAPIインスタンスは[api-kcwidget.herokuapp.com](https://api-kcwidget.herokuapp.com)ですが、イベント中など混雑時にはOOMが発生することがあります。そういう場合には、独自のインスタンスを立ててもらって、そこに向けるのがよいかと思います。

# ローカル開発

```sh
% docker-compose up -d
% open http://localhost:8080
```

# 新規デプロイ

```sh
% heroku create
% heroku container:push web
% heroku open
```
