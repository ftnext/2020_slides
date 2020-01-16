## AWS Lambdaで`pip install`したパッケージを使うときにハマったこと
### zipでアップロードといわれても
#### 2020/01/16 stapy #53 LT nikkie

---

### お前、誰よ (About nikkie)

- ハンドルネーム「にっきー」 (@fa[twitter] [@ftnext](https://twitter.com/ftnext))
- みんなのPython勉強会 4代目LT王子 && スタッフ
- 2020/03まで週1[ブログ](https://nikkie-ftnext.hatenablog.com/)で自然言語処理のアウトプット中

+++

### [PyCon JP 2020 staff WANTED!!](https://docs.google.com/forms/d/e/1FAIpQLSfkQtEEAAK8xDFR1dGCQPkU6m0ZxEas3z9l-VVCU_3_wQa6Yw/viewform)

![上記のフォームのスクリーンショット](stapy_Jan_AWS_lambda/assets/images/1-pyconjp_staff_wanted.jpg)

+++

### 1/26に[勉強会](https://rejectpy2019.connpass.com/event/159691/)をやります（13〜17時）

![勉強会のconnpassページのスクリーンショット](stapy_Jan_AWS_lambda/assets/images/2-rejectcon_coming_soon.png)

---

### AWS Lambdaで`pip install`したパッケージを使うときにハマったこと

## ＝AWS Lambdaへのデプロイの話

+++

### このLTで話さないこと

- AWS Lambdaの使い方
- AWS Lambdaにデプロイしたスクリプトの中身の解説

---

### Lambda使ったことある方？🙋‍♂️

### Do you know Lambda?

+++

### AWS Lambdaとは

> サーバーをプロビジョニングしたり管理する必要なくコードを実行できるコンピューティングサービス

ref: https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/welcome.html

+++

### AWS LambdaとPython

- もちろんPythonスクリプトも実行できる
- ＝Pythonスクリプトがあれば、開発者でサーバの管理は不要

+++

### AWS Lambdaで使えるパッケージ

`boto3`など一部のパッケージは`pip install`不要

ref: https://gist.github.com/gene1wood/4a052f39490fae00e0c3#gistcomment-3131227

+++

### Lambdaで`pip install`したパッケージ使ったことある方？🙋‍♂️

（ある方は温かい目で見守っていてください）

---

### nikkie最近のマイブーム✨

## Slackに投稿するPythonスクリプトをLambdaで定期実行

+++

### LambdaからSlack投稿

- LambdaにPythonスクリプトを配置（`urllib`でSlackの投稿用URLを叩く）
- [CloudWatch Event](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)でスケジュール実行（毎日◯時）
- （エンドポイントは作らない）

+++

### 例：勉強会の参加状況を取得

![connpass APIから定期的に参加状況を取得し、Slackに通知するスクリプトをLambdaで動かしています](stapy_Jan_AWS_lambda/assets/images/3-notify_to_slack_everyday.png)

Note:

- urllibで書いた
- connpassのAPIを呼び出し、結果をSlackに投稿

+++

### 今回やりたいこと

- Googleスプレッドシートをタスクリストとしている
- シートの入力内容を取得する
- 条件に該当する行の内容（タスク）をSlack通知

+++

### 実現方法

- 認証に[`authlib`](https://github.com/lepture/authlib)を使う
- Google Sheets APIの呼び出しに[`gspread`](https://github.com/burnash/gspread)を使う

これらはAWS Lambdaには**インストールされていない**

+++

### デプロイ方法

## デプロイパッケージ（zipファイル）にまとめてアップロード

ref: [ドキュメント](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)

+++

### 手順：デプロイパッケージ（zipファイル）にまとめてアップロード

1. `pip install -t .`でカレントディレクトリにパッケージをダウンロードしてインストール
2. カレントディレクトリのファイルからzipファイルを作成（`zip -r awesome.zip *`）
3. ブラウザからLambdaの関数にアップロード

---

### zipでアップロードといわれても

## ハマりました

詳しくは[ブログ](https://nikkie-ftnext.hatenablog.com/entry/2020/01/08/235556)をどうぞ

+++

### ハマって知ったこと

## Pythonパッケージはプラットフォームによって異なる

+++

### Pythonパッケージはプラットフォームによって異なる

- Lambdaの実行環境はAmazonLinux
- nikkieの開発環境はmacOS
- `pip install`して入るパッケージはmacOS向け。それをzipファイルにしていた
- →Dockerを使ってAmazonLinux環境を用意✨

Note:

Lambdaの開発環境にEC2が挙がることがあるのは恐らくこのため。手軽じゃないと思っていたが理由があった

+++

### もう一つハマったシェル（bash）のアスタリスク展開

- `zip -r bundle.zip *`（＝.で始まるファイル類を**除く**）
- 隠しディレクトリの中のファイルが含まれずにエラーとなった
- →`zip -gr bundle.zip .[^.]*`✨（＝.で始まるファイル類を追加）

ref: https://linuxfan.info/bash-path-expansion

---

### LT：AWS Lambdaで`pip install`したパッケージを使うときにハマったこと

- `pip install -t .`してzipファイルを作るといわれても
- AmazonLinux環境で`pip install`しないと、**プラットフォームによるパッケージ差異**でLambdaで動かない
- シェルのアスタリスクは.で始まるファイル類を**除く**

+++

### 今後試してみたい

- `aws-cli`（時間切れです。ブラウザからのアップロードがなくせると見ています）
- [`sam build`](https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/serverless-sam-cli-using-build.html)してみる（ややオーバースペック？エンドポイントまでいらない）

+++

### ご清聴ありがとうございました

Contact: [@fa[twitter] @ftnext](https://twitter.com/ftnext)／[匿名質問箱](https://peing.net/ja/ftnext)
