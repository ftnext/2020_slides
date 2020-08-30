## 野良プロジェクト：トークと出会えるようにしたい！
#### TFIDFを使ったトーク紹介ブログ
#### PyCon JP Sprinnt成果発表会（2020/08/30）nikkie

---

### お前、誰よ (About nikkie)

- ハンドルネーム「にっきー」 (@fa[twitter] [@ftnext](https://twitter.com/ftnext))
- PyCon JP 2020 コンテンツチームリーダー

+++

### 野良プロジェクト：トークと出会えるようにしたい！

- Sprint期間の裏でスタッフ活動の一環で作成
- フィードバックがほしい🙏+少しでも盛り上げられればとSprint成果発表会にジョイン

+++

### トークと出会えるように2つの施策

- **TFIDFを使ったトーク紹介ブログ**
- [トーク検索アプリ](https://search-talks-pyconjp2020.herokuapp.com/talk/)（工数足りず😭）

---

### TFIDFを使ったトーク紹介ブログ

読みました？（感想をチャットにお願いします🙏）

- [PyCon JP 2020 トーク紹介 8/28(金)](https://pyconjp.blogspot.com/2020/08/pyconjp2020-day1-talk-lineup.html)
- [PyCon JP 2020 トーク紹介 8/29(土)](https://pyconjp.blogspot.com/2020/08/pyconjp2020-day2-talk-lineup.html)

![](pyconjp_Aug_sprint_talk_tfidf/assets/images/pyconjp_2020_talk_keyword_blog.png)

+++

### なぜ出会えるようにしたいのか

- 今年はトーク検索機能にまで手が回らなかった（下図は[2019の一覧](https://pycon.jp/2019/sessions)）
- 検索できない → 探せない＝素晴らしいトークに出会えない懸念

![](pyconjp_Aug_sprint_talk_tfidf/assets/images/pyconjp_2019_talk_search.png)

+++

### なぜブログを書いたのか

- nikkieは2020サイトに検索機能を追加できない（Vue, Nuxt未入門）
- 仮説：タイトル以上の情報を伝えられれば少しは出会える？
- タイトル以上の情報＝トークのキーワード

+++

### トークのキーワードとは？

- トークのテキストに含まれる各語について、TFIDFという値を算出
- TFIDFが高い語はキーワードと考えられる
- TFIDFが高い語＝そのトークのテキストに頻繁に登場し、他のプロポーザルにはあまり登場しない

---

### 使用パッケージ類

詳しくは[8/29の池田さんの発表](https://speakerdeck.com/taishii/pycon-jp-2020?slide=107)を参照

- 形態素解析はMeCabで (※`mecab-python3`に代えて`fugashi`)
- `scikit-learn`の`TfidfVectorizer`でTFIDF値を算出

+++

### 初期実装

- トークのテキストは日本語も英語もある→全トークで見たTFIDFにしたいので混ぜて扱う

```
I can't believe it's still here!: the, a, to, it, deprecated, function, ex
PythonでXBRL形式の財務情報を扱おう: xbrl, arelle, の, edinet, を, 情報, は
```

Pythonはどのトークにもあるのでキーワードにならない  
deprecatedやxbrlなどそのトークで扱う語がキーワードになる

+++

### 工夫したこと

- 形態素解析した後、助詞（例：を）・助動詞・記号を除く
- 英語のaやitなどを除く（`TfidfVectorizer`に`stop_word`指定）

```
PythonでXBRL形式の財務情報を扱おう: xbrl, arelle, edinet, する, 情報, データ, 有価証券報告書
```

+++

### さらに工夫したこと

- 「する」などよく出る語対策：`TfidfVectorizer`に`max_df`指定
- マークダウン中の箇条書きやリンクURLの削除
- 数字を0にまとめる

+++

### キーワードとしてリリース

![](pyconjp_Aug_sprint_talk_tfidf/assets/images/pyconjp_2020_talk_keyword_blog.png)

+++

### Future works

目検してキーワードにならないものを抜きながらブログを執筆

- 「為」と「ため」など表記ゆれ（発表者の文体として独特だが、トークの内容は伝えない）
- カスタム辞書（jig-pyやfastapi、インメモリーが分解されているため）
- タイムラインに現れる分、minの削除

---

### まとめ

- トークと出会えるようにTFIDFを使って各トークのキーワードを抜き出した（求ム、フィードバック🙏）
- そもそもnikkieが検索を追加できればよかった→JS力磨いていきます💪

+++

### ご清聴ありがとうございました

参考：『現場で使える！Python自然言語処理入門』（[日本百名湯のキーワード](https://github.com/makaishi2/python-text-anl-book-info/blob/master/samples/ch03-04/ch03-04-01.ipynb)）
