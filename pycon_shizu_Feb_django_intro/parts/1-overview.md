### Djangoで始めるWeb開発の世界

1. **Webアプリについて知ろう**
2. Django Girls TutorialでDjangoを学ぼう
3. Django Girls Tutorialの外の世界へ

+++

### Part1: Webアプリについて知ろう

1. Webアプリとは
2. Webアプリを作ってみよう

---

### Part1: Webアプリについて知ろう

1. **Webアプリとは**
2. Webアプリを作ってみよう

+++

### Webアプリ（ウェブアプリ）

- Web + アプリ
- アプリはアプリケーション（＝**特定の作業**のためのプログラム）の略

+++

### 🕸️Web🕸️ 1/2

- インターネットを使った**情報共有**の仕組み（👉Appendix 1-1）
- **HTML**で書いて情報に意味づけ（ここがタイトル、ここが本文、、、）（👉Appendix 1-2）

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>PyCon mini Shizuoka</title>
  </head>
  <body>
    <section id="content" class="body page-section">
    </section>
  </body>
</html>
```

+++

### 🕸️Web🕸️ 2/2

- Webブラウザ（Google Chrome, Firefoxなど）がHTMLを解釈して表示
- ➡️**Web**アプリは、**Webブラウザ**から使うアプリ
- （PCにインストールするのはWebブラウザのみ）

+++

### 皆さんが使ったことのあるWebアプリ

[connpass](https://connpass.com/)

- Webブラウザから使う（connpassはWordやExcelのように手元のPCにインストールされていない）
- 作業として、勉強会の検索や申込みができる

+++

### 勉強会のページを見る

https://pycon-shizu.connpass.com/event/152678/

<span class="eighty-percent-img">
![connpassにあるPyCon mini 静岡のページ](pycon_shizu_Feb_django_intro/assets/images/1/1-connpass_pycon_shizu.png)
</span>

+++

### 勉強会に申し込む

参加枠などブラウザに入力したデータをconnpassが処理します

<span class="sixty-percent-img">
![connpassで勉強会に申し込む（PyCon JP スタッフmtgを例に）](pycon_shizu_Feb_django_intro/assets/images/1/2-connpass_application_form.png)
</span>

---

### Part1: Webアプリについて知ろう

1. Webアプリとは
2. **Webアプリを作ってみよう**

+++

### Webアプリは作れる！

- 皆さんの知っているPython🐍で作れます！
- デモ用のブログアプリ：https://nikkie-pycon-shizu-django-blog.herokuapp.com/
- 今回話すチュートリアルを最後までやると同様のWebアプリが作れます

+++

### [デモアプリ](https://nikkie-pycon-shizu-django-blog.herokuapp.com/)の操作

1.記事を選択 ➡️ 2.コメントを入力

<span class="eighty-percent-img">
![記事にコメントが増えていきます](pycon_shizu_Feb_django_intro/assets/images/1/3-demo_app_comment.png)
</span>

+++

### Webアプリをどう作るか？

- 1つの方法として**フレームワーク**を使う
- このトークでは、フレームワーク＝*Webアプリケーション*フレームワーク

+++

### フレームワークとは

- Webアプリに必要なコードがすでに用意された土台
- 開発者はフレームワークの**流儀に従って**コードを追加する
- フレームワークを使うことでWebアプリを**速く開発**できる

+++

### Djangoとは

- Pythonで書けるフレームワークの1つ
- 「締切がある完璧主義者のためのフレームワーク」と標榜

+++

### 締切がある完璧主義者向け

- 😄Webアプリに必要な機能は一通り用意されている
- 😅多機能な分、学習コストが高い
- 😄Webに精通していなくてもDjangoの流儀に反しなければ、**安全**で**拡張可能**なWebアプリが作れる

+++

### Webアプリの実態は大量のファイル📁

```plaintext
.
├── blog
├── db.sqlite3
├── manage.py
├── mysite
├── myvenv
└── requirements.txt
```

+++

### DjangoでWebアプリを作る

- Djangoの流儀に沿ってファイルを配置する
- ファイルの中には、Djangoの流儀に従ってPythonを書く

+++

### Webアプリ開発＝ファイルを作る

- **エディタ**を使って`.py`や`.html`ファイルを作る
- エディタの例：Visual Studio Code, Atom, Sublime Textなど
- ❗️Jupyter Notebookはエディタではないため、Webアプリ開発では使いません
