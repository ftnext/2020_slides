## 繰り返すブラウザ操作をPythonにやらせよう
## 〜Introduction of Helium〜
#### みんなのPython勉強会 #57 2020/05/14 nikkie

---

### お前、誰よ (About nikkie)

- ハンドルネーム「にっきー」 (@fa[twitter] [@ftnext](https://twitter.com/ftnext))
- Python🐍歴2年ほど。仕事ではPythonで機械学習 & Web API開発
- みんなのPython勉強会スタッフ 兼 4代目LT王子

+++

### お知らせ：PyCon JP 2020
### 8/28（金）,29（土） オンライン開催
### トーク募集中 5/31(日)まで

https://sessionize.com/pyconjp2020/

---

### LTの本題：stapy スタッフ活動

- 今回はLT希望者をアンケートで募集
- **LT希望者が何名いるか**を定期的に集計したい

+++

### LT希望者を集計する手順

1. CSVをconnpassからダウンロード
2. LT希望者を集計（PythonスクリプトでCSV処理を自動化）

+++

### 繰り返すブラウザ操作をPythonにやらせよう

- ダウンロードしたCSVからの集計は自動化した（けれどそんなに便利じゃない）
- CSVをconnpassからダウンロードするのもPythonにやらせよう！

+++

# Demo

---

### 仕組み

- 使ったパッケージ @fa[github] [mherrmann/selenium-python-helium](https://github.com/mherrmann/selenium-python-helium)
- 導入：`pip install helium`

+++

### Helium

- Seleniumをラップしている
- → 非常に簡単にブラウザ自動化ができる
- ChromeとFirefoxをサポート

+++

### Helium is awesome!

```python
from helium import click, start_firefox, write

start_firefox("connpass.com/login")
write('username', into='ユーザー名')
write('password', into='パスワード')
click("ログインする")
```

+++

### Firefoxでダウンロードの設定

- Firefoxではデフォルトでポップアップが出る（消したい）
- `from selenium.webdriver import FirefoxOptions`
- FirefoxOptionsの設定例：https://github.com/mherrmann/selenium-python-helium/issues/19#issuecomment-623253607

---

### まとめ：繰り返すブラウザ操作をPythonにやらせよう

- stapyのスタッフ活動にPythonを使った例を紹介
- connpassからの参加者のダウンロードをHeliumで自動化した
- Heliumはブラウザ自動化を**劇的に簡略化**する印象。よろしければ！

+++

### ご清聴ありがとうございました
### Enjoy browser automation!

Contact: [@fa[twitter] @ftnext](https://twitter.com/ftnext)／[匿名質問箱](https://peing.net/ja/ftnext)
