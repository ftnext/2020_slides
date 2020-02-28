### Djangoで始めるWeb開発の世界

1. Webアプリについて知ろう
2. Django Girls TutorialでDjangoを学ぼう
3. **Django Girls Tutorialの外の世界へ**

+++

### Part3: Django Girls Tutorialの外の世界へ

1. 続編：Django Girls Tutorial Extensions
2. Webアプリでよく見るユーザ管理の機能を作るには
3. Django 3系アップデート

---

### Part3: Django Girls Tutorialの外の世界へ

1. **続編：Django Girls Tutorial Extensions**
2. Webアプリでよく見るユーザ管理の機能を作るには
3. Django 3系アップデート

+++

### [Django Girls Tutorial Extensions](https://tutorial-extensions.djangogirls.org/ja/)とは

- Django Girls Tutorialの次の教材
- Tutorialで作ったアプリに**機能追加**していく（コメント機能、ドラフト機能）

+++

### 特筆！ログイン機能を追加

![デモアプリのログイン画面](pycon_shizu_Feb_django_intro/assets/images/3/1-demo_app_login.png)

+++

### ログイン

- **本人かどうかを確認**するための仕組み（認証 Authentication）
- Webアプリにたいてい備わっている

+++

### ログインの仕組み 1/2

- ログインページに**本人しか知らないデータ**（ユーザ名とパスワードの組合せ）を入力
- Webブラウザはリクエストに入れてサーバに**送信**
- サーバでWebアプリがデータベースに保持するユーザ情報と**照合**

+++

### ログインの仕組み 2/2

- 照合できたら、"合言葉"を含めたレスポンスを返す
    - Webブラウザは以降のリクエストに"合言葉"を含めるようになる（ログアウトするまで）
- リクエストに**"合言葉"が含まれれば、本人のアクセスと判断**できる
    - connpassの場合、申込済みの勉強会の情報を表示

+++

### Djangoでログイン機能を追加（[Extensions](https://tutorial-extensions.djangogirls.org/ja/authentication_authorization/)）

- ログインに使うビューとモデルはDjangoに用意されているのでそれを使う
- **URL設定**にログイン用のURLを追加
- **テンプレート**：ログインに使うHTMLを追加
- +α プロジェクトの`settings.py`にログインの設定を追加

+++

### 本格的な開発へ

- 規模が大きなWebアプリで使われるデータベース(PostgreSQL)に切り替え
- herokuへのデプロイを紹介

---

### Part3: Django Girls Tutorialの外の世界へ

1. 続編：Django Girls Tutorial Extensions
2. **Webアプリでよく見るユーザ管理の機能を作るには**
3. Django 3系アップデート

+++

### Webアプリでよくみるユーザ管理機能 その1

パスワードが思い出せない🤨→[connpass パスワード再設定](https://connpass.com/account/password_reset/)

![connpassのパスワード再設定画面](pycon_shizu_Feb_django_intro/assets/images/3/2-connpass_password_reset.png)

+++

### ユーザのパスワードに関する機能

- ログアウトしていてパスワードが思い出せず変更
- ログインしている状態でパスワードを変更

これらもDjangoが用意している（[認証ビュー](https://docs.djangoproject.com/ja/3.0/topics/auth/default/#module-django.contrib.auth.views)）

+++

### 認証ビューを使う前に：ビューの書き方は2通り

- Django Girls Tutorialで学ぶのは関数によるビュー
- Djangoのビューは**クラス**でも書ける
- Djangoが用意している認証ビューはクラスで書かれたビュー

+++

### クラスで書かれた認証ビューを使う

📌URL設定で`as_view()`メソッドの返り値と対応づける

```python
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ...,
    path('password_reset/', auth_views.PasswordResetView.as_view()),
    # ...,
]
```

+++

### Webアプリでよくみるユーザ管理機能 その2

[connpass ユーザ登録](https://connpass.com/signup/)

<span class="seventy-percent-img">
![connpassのユーザ登録画面](pycon_shizu_Feb_django_intro/assets/images/3/3-connpass_signup.png)
</span>

+++

### ユーザ登録を自作する

- Djangoは**Webアプリで共通する処理向けのビュー**（ジェネリックビュー）も用意している
- これらはクラスで書かれている
- データの作成処理向けの[CreateView](https://docs.djangoproject.com/ja/3.0/ref/class-based-views/generic-editing/#createview)を使ってユーザ登録用のビューを作る

+++

### ジェネリックビューでユーザ作成機能を作る （views.py）

```python
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
class Register(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('post_list')
```

+++

### なぜビューの書き方を2通り知る必要がある？

- Djangoの機能は豊富で1つのチュートリアルではカバーしきれない➡️検索して調べていく
- 関数ではなくクラスを使ったビューの書き方もあると知っていると**参照できる情報が広がる**
- ※ジェネリックビューの利用には賛否あり（早く開発できる一方で、複雑な処理の実装は大変らしい）

---

### Part3: Django Girls Tutorialの外の世界へ

1. 続編：Django Girls Tutorial Extensions
2. Webアプリでよく見るユーザ管理の機能を作るには
3. **Django 3系アップデート**

+++

### Django 3系のアップデートの1つ

- プロジェクトを作成すると、`asgi.py` ができるようになった
- その他は[Django 3.0 リリースノート](https://docs.djangoproject.com/ja/3.0/releases/3.0/)

+++

### `asgi.py` がもたらすもの

- Webブラウザの**再読み込みがいらない**Webアプリが作れる
- 例えば、Slack（チャットアプリ）は、ページを再読み込みせずに新しい投稿が見られる（👉Appendix 3-1）

+++

### 再読み込み不要なWebアプリに向けて開発進行中！

- 現在は試験的。ビューはまだサポートされていない（ref: [非同期サポート](https://docs.djangoproject.com/ja/3.0/topics/async/)）
- 再読み込み不要なWebアプリが作れるようにする提案：[DEP 0009](https://github.com/django/deps/blob/master/accepted/0009-async.rst#sequencing)。承認され、実装進行中
