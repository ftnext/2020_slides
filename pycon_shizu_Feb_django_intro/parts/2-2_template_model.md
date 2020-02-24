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

1. @color[#999999](URL設定から呼び出される)
2. @color[#999999](リクエストの情報を使った処理をする)
3. **テンプレートを読み込み**、レスポンスを作る（処理結果を埋め込むなど）
4. @color[#999999](レスポンスを返す)

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

1. @color[#999999](URL設定から呼び出される)
2. リクエストの情報を使った処理をする（**必要なデータをモデルを通して取得**）
3. @color[#999999](テンプレートを読み込み、レスポンスを作る（処理結果を埋め込むなど）)
4. @color[#999999](レスポンスを返す)

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
