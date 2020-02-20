### Djangoで始めるWeb開発の世界

1. 前提：Webアプリ、フレームワーク、Djangoについて（5分）
2. Django Girls Tutorialで学ぶDjangoの使い方（12分）
3. Django Girls Tutorialから飛び出そう（10分）

+++

### Django Girls Tutorialで学ぶDjangoの使い方

1. Django Girls Tutorialとは
2. 流儀その1：プロジェクトとアプリケーション
3. 流儀その2：モデル・URL設定・ビュー・テンプレート

+++

### [Django Girls Tutorial](https://tutorial.djangogirls.org/ja/)とは

- 始めてプログラミングに挑戦するワークショップの教材
- Djangoでブログアプリを作る
- Webに公開されており、誰でも利用可能

+++

### Django Girls Tutorialの特徴

- 初めてプログラミングに挑戦する方向け、平易な語り口
- 知っているところは飛ばして取り組むのをオススメします

---

### 2. 流儀その1：プロジェクトとアプリケーション

Djangoの用語としての意味です

- プロジェクト＝Webアプリ全体
- アプリケーション＝Webアプリの機能1つ1つ

どちらもファイルのまとまりを指します

+++

### Djangoを使った開発

- Djangoではどのようにコードを書くかが決まっている
- Djangoを使った開発では、コマンドを使って必要なファイルを作ることができる

+++

### プロジェクトを作る

`django-admin startproject mysite .`

TODO：ディレクトリツリー

+++

### アプリケーションを作る

`python manage.py startapp blog`

TODO：ディレクトリツリー

+++

### プロジェクトとアプリケーションの関係（[参考：ドキュメント](https://docs.djangoproject.com/ja/3.0/intro/tutorial01/#creating-the-polls-app)）

- プロジェクトは**1つだけ**
- Webアプリの設定と**1つ以上**のアプリケーションを持つ
- 例：ブログ記事を管理するための機能（アプリケーション）、ユーザ管理をするための機能（アプリケーション）

---

### 3. 流儀その2：アプリケーションの4要素

<span class="eighty-percent-img">
![](spzcolab_Jan_django/assets/images/2/1-django_4elements.png)
</span>

+++

![新しいことを4つも覚えないといけません。。](spzcolab_Jan_django/assets/images/2/2-django_many_unknown.png)

+++

### アプリケーションの要素について、以下の順番で紹介していきます

1. URL設定
2. ビュー
3. テンプレート
4. モデル

---

### 3-1. URL設定（URLconf）

- urls.pyというファイルで設定する
- URL設定は、HTTPリクエストのURIに関係

+++

### 開発者ツールで覗く

![http://example.com/ にアクセスした時のリクエスト](spzcolab_Jan_django/assets/images/2/3-examplecom_request.png)

+++

### HTTPリクエストの一部

```
GET http://example.com/ HTTP/1.1
(以下略)
```

- URI：http://example.com/

+++

### DjangoのURL設定（URLconf）

- 前提：HTTPリクエストをDjango流のオブジェクトに変換している
- HTTPリクエストのURIを見る
- URIの一部（パス）と一致する**ビューを呼び出す**（HTTPリクエストを渡す）

+++

### 補足：URIのパスとは

例：http://www.example.com/index

- `http`：プロトコル
- `www.example.com`：ホスト（インターネット上のコンピュータ）
- `index`：パス（ホスト上のどこにアクセスするかの指定）

+++

### URL設定のコード例

@fa[github] [blog/urls.py (Tag: 1-url_and_view)](https://github.com/ftnext/explain-how-django-works-for-beginner/blob/8f1eaa0856cbfb499d05fdcdb2adb4fb997665ea/blog/urls.py)

```python
urlpatterns = [
    # リクエスト中のURIが 127.0.0.1:8000/ のときは、
    # パスが''（空文字）となる。
    # blog/views.py の post_list 関数を呼び出す
    path('', views.post_list, name='post_list'),
    # リクエスト中のURIが 127.0.0.1:8000/ 以外の場合は
    # 設定していないのでエラー
]
```

+++

### 3-2. ビュー

- URL設定から呼び出される
- HTTPリクエストの情報を使った処理（例：HTTPメソッド）
- HTTPに則ってリクエストにレスポンスを返す（＝最小限のWebアプリ）

+++

### 再掲：HTTPリクエストの一部

```
GET http://example.com/ HTTP/1.1
(以下略)
```

- HTTPメソッド：GET

+++

### HTTPレスポンス

2つのポイント

- ステータスコード
- メッセージボディ

+++

### 開発者ツールで覗く

<span class="sixty-percent-img">
![この後紹介する単純なレスポンスを覗いた例](spzcolab_Jan_django/assets/images/2/4-http_response.png)
</span>

+++

### Django ビュー

- HTTPレスポンスを返す
- 単純なレスポンス：`HttpResponse`
- ステータスコードは指定不要
- メッセージボディを指定して返す

+++

### Django ビューのコード例

@fa[github] [blog/views.py (Tag: 1-url_and_view)](https://github.com/ftnext/explain-how-django-works-for-beginner/blob/8f1eaa0856cbfb499d05fdcdb2adb4fb997665ea/blog/views.py)

```python
def post_list(request):
    # 引数requestはHttpRequest（Django流のHTTPリクエストの扱い方）
    # request.methodでHTTPメソッドを確認できる
    if request.method == 'GET':
        # メッセージボディを指定して，HttpResponseを返す（→ブラウザに表示される）
        return HttpResponse('GETリクエストへのレスポンスです')
    # 以下略
```

+++

### URL設定とビューのイメージ

<span class="eighty-percent-img">
![URL設定に該当するビューを呼び出し、ビューはリクエストを元にレスポンスを返す](spzcolab_Jan_django/assets/images/2/7-urlconf_view.png)
</span>

---

### 3-3. テンプレート

- レスポンスとして**HTML**を返すWebアプリになる（CoLabのようなWebアプリに近づく）
- レスポンスのメッセージボディにHTMLを文字列として含める

+++

### HTML

- タグを使って構造を指定する
- 例：見出し、段落、箇条書き、画像、表（詳しくは[HTMLの基本 | MDN web docs](https://developer.mozilla.org/ja/docs/Learn/Getting_started_with_the_web/HTML_basics)）
- ブラウザはHTMLを解析して描画している（レスポンスはあくまで文字列）

+++

### レスポンスとして返されたHTMLを覗く

<span class="seventy-percent-img">
![この後紹介するHTMLを含むレスポンスを覗いた例](spzcolab_Jan_django/assets/images/2/5-html_response.png)
</span>

+++

### Django テンプレート

- Webアプリの見た目に関わる
- テンプレート≒HTML（テンプレートにはDjango独自のタグがある）
- 仲間：CSS（見た目の指定）、JavaScript（動きをつける）

+++

### URL設定、ビュー、テンプレートのイメージ

<span class="seventy-percent-img">
![URL設定→ビューはこれまで通り。ビューはテンプレートを使ってHTMLを含んだレスポンスを作り、それを返す](spzcolab_Jan_django/assets/images/2/8-urlconf_view_template.png)
</span>

+++

### Django テンプレートのコード例

@fa[github] [blog/templates/blog/post_list.html (Tag: 2-url_view_template)](https://github.com/ftnext/explain-how-django-works-for-beginner/blob/1db8d0827afac7514725db489fc21efcf82bf25d/blog/templates/blog/post_list.html)

```html
<div>
  <p>公開日: 2014/06/14, 12:14</p>
  <h2><a href="">最初の投稿</a></h2>
  <p>こんにちは！ よろしくお願いします！ </p>
</div>
```

+++

### ビューがテンプレートを返す コード例

@fa[github] [blog/views.py (Tag: 2-url_view_template)](https://github.com/ftnext/explain-how-django-works-for-beginner/blob/1db8d0827afac7514725db489fc21efcf82bf25d/blog/views.py)

```python
def post_list(request):
    # 指定したテンプレート（HTML）をメッセージ本文に入れた
    # HTTPレスポンス（HttpResponse）を、render関数で作って返す
    return render(request, 'blog/post_list.html', {})
    # URL設定に対してテンプレートが対応する形になる
```

---

### 3-4. モデル

- 決まったHTMLをレスポンスとして返せる（しかし、勉強会100000回分は作りたくない。。）
- データをWebアプリとは別で管理する（データベース）
- リクエストに応じてデータを取り出したり保存したりする

+++

### データベースとモデル

- データベースのイメージは、ExcelやGoogleスプレッドシートの表
- モデルを通してデータベースにアクセスする

+++

### データを埋め込んでレスポンスを作る

- ビューがモデルを使って該当するデータを取得
- 取得したデータをテンプレートで表示する

+++

### URL設定、ビュー、テンプレート、モデルの連携

<span class="seventy-percent-img">
![URL設定に対応するビューが呼び出され、必要なモデルにアクセス、取得した結果をテンプレートに埋め込み、HTMLを生成して返す](spzcolab_Jan_django/assets/images/2/9-urlconf_view_model_template.png)
</span>

+++

### ビューがモデルを使うコード例

@fa[github] [blog/views.py (Tag: 3-url_view_model_template)](https://github.com/ftnext/explain-how-django-works-for-beginner/blob/3b0133546c8a8a565de5a0427f164b666b5378e0/blog/views.py)

```python
def post_list(request):
    # ブログ投稿のうち、published_date（公開日）が現在より前のものを取得し。
    # 公開日の昇順（以前に公開されたものほど上）に並べ替える
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 取得した投稿データpostsをテンプレートでpostsという名前で扱えるように渡す
    return render(request, 'blog/post_list.html', {'posts': posts})
```

+++

### データをテンプレートに表示するコード例

@fa[github] [blog/templates/blog/post_list.html (Tag: 3-url_view_model_template)](https://github.com/ftnext/explain-how-django-works-for-beginner/blob/3b0133546c8a8a565de5a0427f164b666b5378e0/blog/templates/blog/post_list.html)

```html
{# データベースから取り出した投稿を1つずつ繰り返し処理する。 #}
{# 投稿の公開日やタイトル、本文を入れたHTMLを作る（ここまでコメント） #}
{% for post in posts %}
  <div class="post">
    <div class="date">
      <p>公開日: {{ post.published_date }}</p>
    </div>
    <h2><a href="">{{ post.title }}</a></h2>
    <p>{{ post.text|linebreaksbr }}</p>
  </div>
{% endfor %}
```
