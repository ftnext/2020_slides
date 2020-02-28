### Djangoで始めるWeb開発の世界

1. Webアプリについて知ろう
2. **Django Girls TutorialでDjangoを学ぼう**
3. Django Girls Tutorialの外の世界へ

+++

### [Django Girls Tutorial](https://tutorial.djangogirls.org/ja/)とは

- プログラミングに初めて挑戦する方向けのワークショップの教材
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

### Djangoで扱うファイルのまとまりは2種類

Djangoの用語としての意味📗

- プロジェクト＝Webアプリ全体の構成
- アプリケーション＝Webアプリの機能1つ1つ

+++

### Djangoはルールに沿ってファイルを配置してほしい

- Django「プロジェクトにはこれこれのファイルを配置してください」
- ➡️用意された**コマンドを使って**必要なファイルを作ることができる

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
    - URL設定、ビュー
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

### 最小限のWebアプリ

- URL設定とビューがあれば、Djangoのアプリケーションは動作する
- ➡️それぞれの説明に必要なので、Webの構成要素を簡単に紹介

---

### Webの構成要素

- リクエスト
- レスポンス

📌構成要素はWebアプリ全般に当てはまります

+++

### リクエストとレスポンス

<span class="eighty-percent-img">
![Webブラウザはリクエストを送信。サーバはリクエストに応じた処理をしてレスポンスを返却。Webブラウザはレスポンスを解釈して表示](pycon_shizu_Feb_django_intro/assets/images/2/1-browser_server_request_response.png)
</span>

+++

### リクエスト

- WebブラウザにURLを入力（Firefoxでは、"Googleで検索、またはURLを入力します"）してEnter
  - 例：https://nikkie-pycon-shizu-django-blog.herokuapp.com/post/1/
- ブラウザはURLの一部からWebアプリを動かすコンピュータ（サーバ）を特定
- URLやブラウザに入力したデータを**リクエスト**としてサーバに送信

+++

### レスポンス

- サーバで動くWebアプリはリクエストに応じた処理をする
- Webアプリは処理結果を**レスポンス**として、Webブラウザに返す
- Webブラウザはレスポンスに含まれるHTMLを解釈して表示

+++

### 再掲：リクエストとレスポンス

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
