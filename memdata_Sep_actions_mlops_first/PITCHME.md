## GitHub Actionsを使ったMLOpsの一歩目
#### TFIDFによるキーワード抽出スクリプトを例に
#### Members.data #4（2020/09/25）nikkie

---

### 🙋‍♀️アンケート🙋‍♂️

ふだんどんなデータを扱っていますか？（コメントしてください）

- テーブルデータ（表）
- 画像
- 自然言語
- 時系列データ
- その他

+++

### 🙋‍♀️アンケート🙋‍♂️ その2

以下の中で聞いたことのない言葉をコメントしてください

- GitHub Actions
- MLOps
- TFIDF

+++

### お前、誰よ (About nikkie)

- ハンドルネーム「にっきー」 (@fa[twitter] [@ftnext](https://twitter.com/ftnext))
- 2019/04〜 自然言語処理に従事するデータサイエンティスト
- Love Python ❤️🐍

+++

### 続・お前、誰よ (About nikkie)

- PyCon JP 2020（Pythonのカンファレンス）のスタッフ（コンテンツチームリーダー）
- Love Anime ❤️ ＠　🎺🎷🔥　🌸🌹🌻💃　💌📮📨　🍎🍋🥝🍇🧺

+++

### スタッフ活動で自然言語処理の知見

- TFIDFを使ってカンファレンスのトークのキーワードを表示
- 例：「PythonでXBRL形式の財務情報を扱おう」➡xbrl, arelle, edinet, 情報, データ, 有価証券報告書
- [PyCon JP 2020 トーク紹介 8/28(金)](https://pyconjp.blogspot.com/2020/08/pyconjp2020-day1-talk-lineup.html)

---

### 機械学習していて最近思うこと

- Pythonスクリプトで機械学習（Jupyter Labってすごそう）
- コードを変更したら、簡単に訓練が始まって、自動で結果を知らせてもらえたらいいな🤩

+++

### 簡単に訓練が始まる

- MLOpsと呼ばれる分野（Machine Learning Operations）
- その中の**実験管理**の領域
- 様々なツールがあり、「自動で訓練」も実現されている

+++

### このLTで扱う例

- GitHub Actionsを使って訓練を半自動化する例を紹介
- 先のTFIDFを出したスクリプト、これを変更したらキーワードがどう変わったかを見たい

+++

# Demo

+++

### 動きの流れ

- GitHubリポジトリにプルリクエストがあります
- プルリクエストに`/test-trigger-comment`とコマンド風のコメントをします
- あるGitHub Actionsが実行されます
- 別のGitHub Actionsが連鎖します
- キーワードが確認できます（ログとして表示）

---

### GitHub Actionsとは

- 「GitHubが提供するCI/CDシステム」（[Software Design 10月号](https://gihyo.jp/magazine/SD/archive/2020/202010)の特集より）
- **C**ontinuous **I**ntegration / **C**ontinuous **D**elivery
- CI/CDの例：自動でテストコードの実行、自動でデプロイ

+++

### GitHub Actionsの特徴

- **リポジトリで起こったイベントをトリガーにして**決まった処理を実行できる
- 例：プルリクエストが作られたら、そのコードに対してテストコードを実行する（[Pythonの例](https://github.com/actions/starter-workflows/blob/master/ci/python-package.yml)）
- 今回の例：プルリクエストにラベルが付いたら、モデルを訓練する（`TFidfVectorizer`を`fit_transform`）

+++

### 今回の例の構成

- GitHub Actions（2つ）
- AWS CodeBuild

+++

### GitHub Actions その1 🏷

- トリガー：プルリクエストへのコメント
- やること：そのプルリクエストに**ラベルを付ける**

+++

### GitHub Actions その2 🤖

- トリガー：その1がプルリクエストにラベルを付ける
- やること：AWS CodeBuildで**実験スクリプトを実行**

+++

### Why AWS CodeBuild? 1/2

- GitHub Actionsには[使用制限](https://docs.github.com/ja/github/site-policy/github-additional-product-terms#5-actions-and-packages)がある

>アクションは次の用途には使用しないでください。（中略）gitHubアクションが使用されるリポジトリに関連するソフトウェアプロジェクトの製造、テスト、デプロイ、公開に関連しないその他の行為

+++

### Why AWS CodeBuild? 2/2

- 実験スクリプトの実行は使用制限の範囲内？
- 判断つかなかったので、**別の実行環境**としてCodeBuildを利用（[そのためのAction](https://github.com/aws-actions/aws-codebuild-run-build)）
- 注：CodeBuild自体はCI/CD目的で使われるビルド環境という理解（[ドキュメント](https://docs.aws.amazon.com/ja_jp/codebuild/latest/userguide/welcome.html)）

+++

### 動かせて思うこと

- [参考例](https://github.blog/2020-06-17-using-github-actions-for-mlops-data-science/)（GitHub Universe 2019）があったが、ハードル高かった
- 参考例では、[Argo](https://argoproj.github.io/)でk8s環境で実行している（Argoが初めてなので今後触っていきたい）

+++

### キーワードが出ただけでも嬉しいが、もっとやりたいこと😤

- Issueのコメントとして記録に残したい（先の参考例ではやっている）
- 暫定ベストのキーワードリストと比較して差分が分かるとテンション上がる

---

### まとめ🌯：GitHub Actionsを使ったMLOpsの一歩目

- プルリクエストのコメントをトリガーにMLOpsした
- ラベルが付いたことをトリガーにGitHub Actionsを連鎖させる
- GitHub Actions以外のツール（特にArgo）触っていきたい

+++

### ご清聴ありがとうございました

- 実装の参考（PyCon JP Sprintでの[成果発表スライド](https://gitpitch.com/ftnext/2020_slides/master?p=pyconjp_Aug_sprint_talk_tfidf)）
- ここで紹介したGitHub Actionsの設定について、[拙ブログの記事](https://nikkie-ftnext.hatenablog.com/entry/github-actions-mlops-first-step)
