### Appendix

- 本編の補足説明（1-1など）
- 追加の説明

---

### 1-1：インターネットとWeb

- インターネット：世界中のコンピュータがつながるネットワーク🌐
- Web（World Wide Webの略）はインターネットの使い方の1つ
- インターネットの別の使い方として、電子メールもある

+++

### 1-2：HTMLの補足説明

- 情報の意味付けには**タグ**を使う
- 例：見出し、段落、箇条書き、画像、表（詳しくは[HTMLの基本 | MDN web docs](https://developer.mozilla.org/ja/docs/Learn/Getting_started_with_the_web/HTML_basics)）
- ブラウザはHTMLを解析して描画している（part2で説明するレスポンスに含まれるのはあくまで**文字列**）

+++

### 2-1：プロジェクトとアプリケーションの関係

- プロジェクトは**1つ**。その中に**1つ以上のアプリケーション**を持つ
- ブログアプリの場合、2つのアプリケーション
  - ブログ記事を管理するための機能（アプリケーション）
  - ユーザ管理をするための機能（アプリケーション）

[参考：ドキュメント](https://docs.djangoproject.com/ja/3.0/intro/tutorial01/#creating-the-polls-app)

+++

### 2-2：URLはパスの他にホストがある

例：https://nikkie-pycon-shizu-django-blog.herokuapp.com/post/1/

- `https`：プロトコル
- `nikkie-pycon-shizu-django-blog.herokuapp.com`：ホスト（インターネット上のコンピュータ）
- `post/1/`：パス（ホスト上のどこにアクセスするかの指定）

+++

### 2-3：Webアプリの見た目に関わるのはテンプレート（HTML）以外にもある

- CSS（見た目の指定）
- JavaScript（動きをつける）
- どちらも**Webアプリ一般**で登場する

+++

### 3-1：Djangoで再読み込み不要なアプリを作る

- [Django Channels](https://channels.readthedocs.io/en/latest/index.html)を使うという方法もある
- PyCon JP 2018「Djangoだってカンバンつくれるもん」（[スライド](https://speakerdeck.com/denzow/djangotovuedezuo-rukanbanapurikesiyon)・[YouTube](https://youtu.be/RTIPoW21K3U)）

---

### URL設定の追加説明

- URLconfとも呼ばれる（URL configurationの略）
- プロジェクトの`urls.py`からアプリケーションの`urls.py`を`include`
- ＝アプリケーションごとの**URL設定を参照**する
- アプリケーションごとにURLの**変更が楽**

+++

### Django Girlsとは

- 女性がプログラミングに出会う機会を提供するワークショップ
- Tech業界における女性の割合が少ないという問題意識から発足
- 2014年にベルリンから始まり、世界各地で開催（[Tokyo](https://djangogirls.org/tokyo/)でも）
- また、Tokyoでは毎月勉強会を開催（[connpassグループ](https://djangogirls-org.connpass.com/)）
