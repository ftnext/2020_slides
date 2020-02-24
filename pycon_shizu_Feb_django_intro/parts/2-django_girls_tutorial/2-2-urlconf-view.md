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
