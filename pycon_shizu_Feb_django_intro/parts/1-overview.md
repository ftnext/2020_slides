### Djangoで始めるWeb開発の世界

1. 前提：Webアプリ、フレームワーク、Djangoについて（5分）
2. Django Girls Tutorialで学ぶDjangoの使い方（12分）
3. Django Girls Tutorialから飛び出そう（10分）

+++

### Webアプリ、フレームワーク、Djangoについて

1. Webアプリとは
2. フレームワークとは
3. Djangoとは

---

### 1. Webアプリとは

- Webアプリ＝Webアプリケーション
- 「Web」：**ブラウザから**使う（アプリのインストール不要）
- アプリケーション＝**特定の作業**のためのプログラム

+++

### Webアプリの例

TODO：connpassに差し替え

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

### インターネットとWeb

- インターネット≒ネットワークで繋がったコンピュータ群
- コンピュータ間で情報共有の仕組みとして、World Wide Web（単にWeb）

+++

### Webの根幹：HTTP

- Web（World Wide Web）はインターネットを覆っている
- Webでコンピュータ同士がする**通信**は、HTTPという**取り決め**に則る

+++

### HTTPでの通信の登場人物

<span class="eighty-percent-img">
![クライアント（＝Webブラウザ。ChromeやFirefox）とサーバ（＝Djangoで作ったWebアプリ）が通信する](spzcolab_Jan_django/assets/images/1/4-client_server.png)
</span>

+++

### HTTP通信（ざっくり）

<span class="eighty-percent-img">
![クライアントはリクエストを送信。サーバはリクエストに応じた処理をしてレスポンスを返却。クライアントはレスポンスを解釈して表示](spzcolab_Jan_django/assets/images/1/5-request_response.png)
</span>

+++

### リクエストを覗く（ブラウザの開発者ツール）

![サポーターズCoLabのサイトを見たときのリクエスト](spzcolab_Jan_django/assets/images/1/2-spzcolab_request.png)

+++

### レスポンスを覗く（ブラウザの開発者ツール）

![サポーターズCoLabのサイトにアクセスしたときのレスポンス](spzcolab_Jan_django/assets/images/1/3-spzcolab_response.png)

+++

### フレームワークとHTTP

- フレームワークは、サーバに置くWebアプリを開発するために使う
- フレームワークを使うことで、開発者は**HTTPを直接扱わなく**て済む
- フレームワークの「流儀」に沿って、プログラムを書いて開発する

---

### 3. Djangoとは

- Pythonで書けるフレームワークの1つ
- 「締切がある完璧主義者のためのフレームワーク」と標榜

+++

### 締切がある完璧主義者向け

- 😄Webアプリに必要な機能は一通り用意されている
- 😄どんな規模のWebアプリでも作れる
- 😅多機能な分、学習コストが高い
