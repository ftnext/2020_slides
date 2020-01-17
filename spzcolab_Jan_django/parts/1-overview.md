### PythonでWeb開発を始めてみよう、Django入門

1. **Webアプリ、フレームワーク、Djangoについて**（5分）
2. Django Girls Tutorialで学ぶDjangoの使い方（20分）
3. Django Girls Tutorialに取り組んでみよう（30分）

+++

### Webアプリ、フレームワーク、Djangoについて

1. Webアプリとは
2. フレームワークとは
3. Djangoとは

---

### 1. Webアプリとは

- Webアプリ＝Webアプリケーション
- アプリケーション＝特定の作業のためのプログラム
- 「Web」：ブラウザから使う（アプリのインストール不要）

Note:

Web = インターネット

+++

### Webアプリの例

[サポーターズCoLab（勉強会のサイト）](https://supporterzcolab.com/)

![サイトのスクリーンショット](spzcolab_Jan_django/assets/images/1/1-example_screenshot.png)

+++

### Webアプリの例：サポーターズCoLab

- できる作業：勉強会の検索や申込み（操作できる）
- ブラウザから使う（WordやExcelとは違って、手元のPCにインストールされていない）

---

### 2. フレームワークとは

- 今回は、**Webアプリケーションフレームワーク**のこと
- Webアプリを開発しやすくするための土台
- フレームワークを使うことでWebアプリを速く開発できる

+++

### Webの根幹：HTTP

- Webはネットワークで繋がったコンピュータ群からなる
- コンピュータ同士が通信する上ではHTTPという取り決めに則る

+++

### HTTPでの通信の登場人物

TODO：表にしたい

- クライアント・リクエスト・ブラウザ
- サーバ・レスポンス・Webアプリ

+++

### リクエストを覗く（ブラウザの開発者ツール）

![サポーターズCoLabのサイトを見たときのリクエスト](spzcolab_Jan_django/assets/images/1/2-spzcolab_request.png)

+++

### レスポンスを覗く（ブラウザの開発者ツール）

![サポーターズCoLabのサイトにアクセスしたときのレスポンス](spzcolab_Jan_django/assets/images/1/3-spzcolab_response.png)

+++

### フレームワークとHTTP

- フレームワークは、サーバに置くWebアプリを開発するために使う
- フレームワークを使うことで、開発者はHTTPを直接扱わなくて済む
- フレームワークの「流儀」に沿って、プログラムを書いて開発する

---

### 3. Djangoとは

- Pythonで書けるフレームワークの1つ
- 「締切がある完璧主義者のためのフレームワーク」と標榜

+++

### Djangoは締切がある完璧主義者向け

- Webアプリに必要な機能は一通り用意されている
- どんな規模のWebアプリでも作れる
- 多機能な分、学習コストが高い