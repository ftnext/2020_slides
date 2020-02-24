### Djangoで始めるWeb開発の世界

1. Webアプリについて知ろう
2. **Django Girls TutorialでDjangoを学ぼう**
3. Django Girls Tutorialの外の世界へ

+++

### [Django Girls Tutorial](https://tutorial.djangogirls.org/ja/)とは

- プログラミングに初めて挑戦する人向けのワークショップの教材
- Djangoでブログアプリを作る
- Webに公開されており、誰でも利用可能

+++

### Part2: Django Girls TutorialでDjangoを学ぼう

1. 作るファイルのまとまりについて：プロジェクトとアプリケーション
2. アプリケーションに含まれるファイルについて
    - URL設定、ビュー
    - テンプレート、モデル

---

### Part2: Django Girls TutorialでDjangoを学ぼう

1. **作るファイルのまとまりについて**：プロジェクトとアプリケーション
2. アプリケーションに含まれるファイルについて
    - URL設定、ビュー
    - テンプレート、モデル

+++

### Djangoで扱うファイルのまとまり

以下の2種類

- プロジェクト
- アプリケーション

+++

### Djangoで扱うファイルのまとまり

Djangoの用語としての意味📗

- プロジェクト＝Webアプリ全体の構成
- アプリケーション＝Webアプリの機能1つ1つ

+++

### Djangoではファイルを配置するルール

- Django「プロジェクトにはこれこれのファイルを配置してください」
- ➡️**コマンドを使って**必要なファイルを作ることができる

+++

### mysiteという名前のプロジェクトを作る

`django-admin startproject mysite .`

```plaintext
.
├── manage.py
└── mysite
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

+++

### blogという名前のアプリケーションを作る

`python manage.py startapp blog`

```plaintext
.
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
# プロジェクトは省略
```

+++

### プロジェクトとアプリケーションの関係（👉Appendix 2-1）

- プロジェクトは、Webアプリの設定を持つ。最初に作り、**1つだけ**
- アプリケーションはWebアプリの**機能ごと**に作り、プロジェクトに追加

---

### Part2: Django Girls TutorialでDjangoを学ぼう

1. 作るファイルのまとまりについて：プロジェクトとアプリケーション
2. **アプリケーションに含まれるファイルについて**
    - **URL設定、ビュー**
    - テンプレート、モデル

+++

### アプリケーションに含まれるファイル

```plaintext
.
├── blog
│   │ # URL設定とテンプレートのファイルは作成します
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py  # モデル
│   ├── tests.py
│   └── views.py  # ビュー
```

+++

### URL設定とビュー

- この2つがあれば、Djangoのアプリケーションは動作する
- ＝最小限のWebアプリが作れる
- ➡️それぞれの説明に必要なので、Webの構成要素を簡単に紹介

---

### Webの構成要素

- リクエスト
- レスポンス

📌構成要素はWebアプリ全般に当てはまります

+++

### リクエスト

- WebブラウザにURLを入力（Firefoxでは、"Googleで検索、またはURLを入力します"）
  - 例：https://nikkie-pycon-shizu-django-blog.herokuapp.com/post/1/
- URLの一部からWebアプリを動かすコンピュータ（サーバ）を特定
- URLやブラウザに入力したデータを**リクエスト**としてサーバに送信

+++

### レスポンス

- サーバで動くWebアプリはリクエストに応じた処理をする
- Webアプリは処理結果を**レスポンス**として、Webブラウザに返す
- Webブラウザはレスポンスに含まれるHTMLを解釈して表示

+++

### リクエストとレスポンス

<span class="eighty-percent-img">
![Webブラウザはリクエストを送信。サーバはリクエストに応じた処理をしてレスポンスを返却。Webブラウザはレスポンスを解釈して表示](pycon_shizu_Feb_django_intro/assets/images/2/1-browser_server_request_response.png)
</span>

+++

### リクエストとレスポンスを覗く

Webブラウザの**開発者ツール**で見られます

- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools?hl=ja)
- [Firefox 開発ツール](https://developer.mozilla.org/ja/docs/Tools)

+++

### 開発者ツールで見たリクエスト🔍

<span class="ninety-percent-img">
![デモアプリの記事1つのURLをWebブラウザに入力したときのリクエスト](pycon_shizu_Feb_django_intro/assets/images/2/2-demo_app_request.png)
</span>

+++

### 開発者ツールで見たレスポンス🔍

<span class="seventy-percent-img">
![デモアプリの記事1つのURLのリクエストに対応するレスポンス](pycon_shizu_Feb_django_intro/assets/images/2/3-demo_app_response.png)
</span>

---

### 🔙Djangoの話に戻ります🔙

1. 作るファイルのまとまりについて：プロジェクトとアプリケーション
2. **アプリケーションに含まれるファイルについて**
    - **URL設定**、ビュー
    - テンプレート、モデル

+++

### URL設定とは

- アプリケーションの中に作る`urls.py`というファイルを指す
- Webブラウザに入力するURLに関係（URLはリクエストにも含まれる）

+++

### URL設定の動き

1. リクエストに含まれるURLのパスの部分を見る
    - https://nikkie-pycon-shizu-django-blog.herokuapp.com/post/1/ であれば、パスは `post/1/`（👉Appendix 2-2）
2. 設定を元に、パスに対応するビューを呼び出す

+++

### URL設定のコード

```python
urlpatterns = [
    # パスが''であれば、ビューの中のpost_listを呼び出すという設定
    path('', views.post_list, name='post_list'),
    # パスが'post/1/'や'post/108/'であれば、ビューの中のpost_detailを呼び出すという設定
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # ...
]
```

+++

### URL設定のイメージ

<span class="eighty-percent-img">
![URL設定に該当するビューを呼び出す](pycon_shizu_Feb_django_intro/assets/images/2/4-urlconf.png)
</span>

---

### Part2: Django Girls TutorialでDjangoを学ぼう

1. 作るファイルのまとまりについて：プロジェクトとアプリケーション
2. **アプリケーションに含まれるファイルについて**
    - URL設定、**ビュー**
    - テンプレート、モデル

+++

### ビュー

- アプリケーションに含まれる`views.py`というファイルを指す
- 空のファイルができており、編集していく
- Django Girls Tutorialの範囲では、`views.py`に**関数**を追加

+++

### ビューの動き

1. URL設定から呼び出される（リクエストの情報も渡る）
2. リクエストの情報を使った処理をする（送信されたデータを使うなど）
3. レスポンスを返す

+++

### Django ビューのコード例

@fa[github] [blog/views.py (Tag: 1-url_and_view)](https://github.com/ftnext/explain-how-django-works-for-beginner/blob/8f1eaa0856cbfb499d05fdcdb2adb4fb997665ea/blog/views.py)

```python
def post_list(request):  # 関数として用意する
    # 引数requestはリクエスト。request.methodのようにリクエストの持つ情報を処理で使える
    if request.method == 'GET':  # ブラウザにURLを入力してアクセスした場合を表す
        # レスポンスを返す
        return HttpResponse('GETリクエストへのレスポンスです')
    # else以下は省略
```

+++

### コード例が返すレスポンス

<span class="sixty-percent-img">
![URL設定とビューからなるコード例が返すレスポンスを開発者ツールで覗く](spzcolab_Jan_django/assets/images/2/4-http_response.png)
</span>

+++

### URL設定とビューのイメージ

<span class="eighty-percent-img">
![URL設定に該当するビューを呼び出し、ビューはリクエストを元にレスポンスを返す](spzcolab_Jan_django/assets/images/2/7-urlconf_view.png)
</span>

---

### Part2: Django Girls TutorialでDjangoを学ぼう

1. 作るファイルのまとまりについて：プロジェクトとアプリケーション
2. **アプリケーションに含まれるファイルについて**
    - URL設定、ビュー
    - **テンプレート**、モデル

+++

### URL設定とビューで動くWebアプリ

- レスポンスを文字列で返した
- connpassのようにHTMLを返したい。ビューにも書けるが、長いHTMLになると書きづらい😑
- **ビューとは別にHTMLのファイルを用意**し、読み込んでレスポンスを作ることにする

+++

### テンプレート

- アプリケーションの中に作る`templates`ディレクトリに置かれるHTMLファイルのこと
- テンプレートは、**HTML+Django独自のタグ**
- HTMLに沿ってWebブラウザに表示されるので、テンプレートはWebアプリの見た目に関わる（👉Appendix 2-3）

+++

### ビューがテンプレートを使う

1. @color[#666666](URL設定から呼び出される)
2. @color[#666666](リクエストの情報を使った処理をする)
3. **テンプレートを読み込み**、レスポンスを作る（処理結果を埋め込むなど）
4. @color[#666666](レスポンスを返す)

+++

### テンプレートのコード例

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
    # 指定したテンプレート（HTML）を使ったレスポンスを、render関数で作って返す。
    # 'blog/post_list.html'は前のスライドで示したテンプレートのこと
    # （templatesディレクトリの下のblog/post_list.html）
    return render(request, 'blog/post_list.html', {})
```

+++

### レスポンスとして返されたHTMLを覗く

<span class="seventy-percent-img">
![テンプレートを使ったコード例が返すHTMLを含むレスポンスを覗いた例](spzcolab_Jan_django/assets/images/2/5-html_response.png)
</span>

+++

### URL設定、ビュー、テンプレートのイメージ

<span class="seventy-percent-img">
![URL設定→ビューはこれまで通り。ビューはテンプレートを使ってHTMLを含んだレスポンスを作り、それを返す](spzcolab_Jan_django/assets/images/2/8-urlconf_view_template.png)
</span>

---

### Part2: Django Girls TutorialでDjangoを学ぼう

1. 作るファイルのまとまりについて：プロジェクトとアプリケーション
2. **アプリケーションに含まれるファイルについて**
    - URL設定、ビュー
    - テンプレート、**モデル**

+++

### HTMLが返せるようになったWebアプリ

- URLに対して決まったHTMLを返している
- 例えばconnpassには、勉強会が10万以上ある（冒頭の例のパス `event/152678/`）
- 10万ものHTMLを個別に用意する？ 流石に厳しい😖

+++

### connpassを観察する

- 勉強会のページのレイアウトが同じ（共通のHTML）
- 勉強会の名前など、勉強会ごとにデータが異なる箇所がある（個別のデータ）

+++

### データベース

**データをテンプレートから切り出し**て管理する

1. ブラウザからのリクエストに応じて、データベースから対応するデータを取得
2. 取得したデータを埋め込んだHTMLをレスポンスとして返す

+++

### データベースのイメージ

表計算ソフトの表（例：**ブログ記事**に必要な列があり、行が追加されていく）

著者 | タイトル | 本文 | 作成日 | 公開日
----- | ----- | ----- | ----- | ----- 
nikkie | ... | ... | 2/24 | 2/24

+++

### モデル

- データベースのデータを取得・作成に使われる
- アプリケーションに含まれる`models.py`というファイルを指す
- 空のファイルができており、編集していく（クラスを追加）

+++

### ビューがモデルを使う

1. @color[#666666](URL設定から呼び出される)
2. リクエストの情報を使った処理をする（**必要なデータをモデルを通して取得**）
3. @color[#666666](テンプレートを読み込み、レスポンスを作る（処理結果を埋め込むなど）)
4. @color[#666666](レスポンスを返す)

+++

### モデルのコード例

@fa[github] [blog/models.py (Tag: 3-url_view_model_template)](https://github.com/ftnext/explain-how-django-works-for-beginner/blob/3b0133546c8a8a565de5a0427f164b666b5378e0/blog/models.py)

```python
class Post(models.Model):  # ブログ記事が持つデータ項目を表す
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 著者
    title = models.CharField(max_length=200)  # タイトル
    text = models.TextField()  # 本文
    created_date = models.DateTimeField(default=timezone.now)  # 作成日時
    published_date = models.DateTimeField(blank=True, null=True)  # 公開日時
```

+++

### ビューがモデルを使うコード例

@fa[github] [blog/views.py (Tag: 3-url_view_model_template)](https://github.com/ftnext/explain-how-django-works-for-beginner/blob/3b0133546c8a8a565de5a0427f164b666b5378e0/blog/views.py)

```python
def post_list(request):
    # ブログ投稿のうち、published_date（公開日時）が現在以前のものを取得し。
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

+++

### URL設定、ビュー、テンプレート、モデルの連携

<span class="seventy-percent-img">
![URL設定に対応するビューが呼び出され、必要なモデルにアクセス、取得した結果をテンプレートに埋め込み、HTMLを生成して返す](spzcolab_Jan_django/assets/images/2/9-urlconf_view_model_template.png)
</span>

---

### Part2ではDjango Girls Tutorialを見てきました

1. @color[#666666](作るファイルのまとまりについて：プロジェクトとアプリケーション)
2. @color[#666666](アプリケーションに含まれるファイルについて)
    - @color[#666666](URL設定、ビュー)
    - @color[#666666](テンプレート、モデル)

+++

### [Django Girls Tutorial](https://tutorial.djangogirls.org/ja/)のアプローチ

- URL設定、ビュー、モデル、テンプレートを1つずつ順番に追加
- Djangoのアプリケーションには4つ必要なので、**4つ揃うまではエラーが出る**
- エラーの解決策を学び、開発手順を身につける

+++

### 📌[Django Girls Tutorial](https://tutorial.djangogirls.org/ja/)の取り組み方案

- Pythonのインストールや文法から始まります。知っているところは飛ばしてください
- Djangoが初めてでしたら**「デプロイ」に関係する部分は飛ばす**のをオススメします
- 1周めでDjangoに慣れる、2周めでデプロイに挑戦するというように**何周も**してみてください
