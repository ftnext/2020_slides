## OORC予告：Pythonでオブジェクト指向
### 画像縮小スクリプトを例に
#### 【代々木】オブジェクト指向LT会 vol.1 2020/02/05 nikkie

---

### お前、誰よ (About nikkie)

- ハンドルネーム「にっきー」 (@fa[twitter] [@ftnext](https://twitter.com/ftnext))
- 2016/04〜 エンジニア（現在4年目）
- Python🐍歴2年。趣味で始めて仕事で書いています
- 2020/03まで週1[ブログ](https://nikkie-ftnext.hatenablog.com/)で自然言語処理のアウトプット中💪

+++

### OORC予告とは

- 2/16(☀️)開催[OOC](https://ooc.dev/)の[リジェクトコン](https://oorc.connpass.com/event/159856/)（2/24(祝・🌕)開催）
- 「[変更しやすいコードを目指して、構造化プログラミングのコードをオブジェクト指向で書き直す（Python編）](https://fortee.jp/object-oriented-conference-2020/proposal/5d4120ad-287a-4cb9-8c30-06cb979f1feb)」で登壇します
- LT駆動登壇準備（「オブジェクト指向はじめました🔰」的LT）

+++

### 目次 OORC予告：Pythonでオブジェクト指向

- 入門書発 構造化プログラミング
- オブジェクト指向っぽく考える
- オブジェクト指向で書き直す

---

### 目次 OORC予告：Pythonでオブジェクト指向

- **入門書発 構造化プログラミング**
- オブジェクト指向っぽく考える
- オブジェクト指向で書き直す

+++

### nikkieのPythonの原点

- 『[退屈なことはPythonにやらせよう](https://www.oreilly.co.jp/books/9784873117782/)』
- Pythonで自動化レシピ集
- 退Py仕込みのコードを実務で書いてきた

+++

### 例）退Py流 画像処理スクリプト

`python shrink.py path/to/target`

- パスで指定した画像を縮小、
- または、パスで指定したディレクトリの中の画像を縮小したい
- 縮小した画像はカレントディレクトリに置く

ref: [退Py中のソースコード](https://automatetheboringstuff.com/chapter17/)

+++

### ファイルが指定された場合の処理

`python shrink.py path/to/target.jpg`

画像を縮小する関数を呼び出す（だけ）

+++

### ディレクトリが指定された場合の処理

`python shrink.py path/to/target_dir`

1. 指定されたディレクトリと同名のディレクトリ（保存先）をカレントディレクトリに作る
2. 指定されたディレクトリの中の各ファイルについて画像を縮小する関数を呼び出す

+++

### ここまでをまとめて、メインの処理

```python
    src_path = args.src
    if src_path.is_dir():  # 指定されたのがディレクトリの場合
        dest_dir = Path(src_path.name)
        dest_dir.mkdir(exist_ok=True)
        for img_path in src_path.iterdir():
            save_path = dest_dir / img_path.name
            shrink_image(img_path, SHRINKED_LENGTH, save_path)
    else:  # 指定されたのがファイルの場合
        shrink_image(src_path, SHRINKED_LENGTH)
```

@fa[github] [shrink.py](https://github.com/ftnext/code-argparse-book/blob/d4292741c67f026299114efbf5c6810a1454584d/argparse-book/shrink.py)

+++

### 大きい関数 `shrink_image`

1. ファイルが画像かどうか判定（拡張子を確認）
2. 画像の場合、縮小する必要があるか判定
3. 縮小する必要がある場合、縮小後のサイズを求める
4. 縮小後のサイズに変換して保存（※保存先のパスが指定されていない場合は指定する）

+++

### 大きい関数 `shrink_image`

```python
def shrink_image(image_path, shrinked_length, save_path=None):
    filename = image_path.name
    if filename.endswith((".png", ".jpg")):
        im = Image.open(image_path)
        width, height = im.size
        if width > shrinked_length and height > shrinked_length:
            if width > height:
                new_width = shrinked_length
                new_height = int((shrinked_length / width) * height)
            else:
                new_width = int((shrinked_length / height) * width)
                new_height = shrinked_length
            resized_im = im.resize((new_width, new_height), Image.BICUBIC)
            if save_path is None:
                save_path = filename
            resized_im.save(save_path)
            print(f"画像を縮小しました: {filename}")
```

@fa[github] [shrink.py](https://github.com/ftnext/code-argparse-book/blob/d4292741c67f026299114efbf5c6810a1454584d/argparse-book/shrink.py)

+++

### 変更しづらい、`shrink_image`関数

- 機能拡張案「保存先をカレントディレクトリではなくて指定できるようにする」
- → 変更に時間がかかる（ムムム🤨）
- 1つの関数が大きすぎる：縮小だけでなく、画像かどうかの判定、保存先の指定まであまりに多くをこなす

Note:

オブジェクト指向で書き直そうと思ったが、構造化プログラミングでも対応できる  
（構造化プログラミングだと呼び出し方を覚えていないといけないという話が必要そう）

---

### 目次 OORC予告：Pythonでオブジェクト指向

- 入門書発 構造化プログラミング
- **オブジェクト指向っぽく考える**
- オブジェクト指向で書き直す

+++

### 見えてきた処理の流れ😃

1. 最初にあるのは、縮小対象のパスと保存先（＝カレントディレクトリ）のパス
2. 縮小対象の**画像**のパスと保存先を列挙する
3. 縮小対象と保存先という1つ1つの組に対して縮小処理を適用する（指定されたサイズより大きければ縮小）

何度も書き直してたどり着いています

+++

### オブジェクト指向で書いてみたコード

```python
    args = p.parse_args()
    destination = Path.cwd()
    # 1. (縮小対象, 保存先)というパスの組のオブジェクト
    path_pair = ph.create_path_pair(args.source, destination)
    # 2. ファイルパスの組を列挙する
    targets = path_pair.list_targets()
    processor = r.create_shrink_processor(shrink_size)  # 3.縮小処理のインスタンス
    processor.process(targets)  # 3.縮小処理適用
```

@fa[github] [`__init__.py`](https://github.com/ftnext/python-image-processor/blob/33a7c5405a56a3907bc47720d6e69ec35ef08cb4/myimageprocessor/__init__.py)

+++

### ここがポイントだと思います

- 入門書におけるクラスの説明は、車や動物など具体的なモノ
- 気づいた：具体的なものでなくてもクラスにしていい！
- →縮小処理を表すクラス、対象・保存先のペアを表すクラス

---

### 目次 OORC予告：Pythonでオブジェクト指向

- 入門書発 構造化プログラミング
- オブジェクト指向っぽく考える
- **オブジェクト指向で書き直す**

+++

### オブジェクト指向実装のヒント

- 『[ThoughtWorksアンソロジー](https://www.oreilly.co.jp/books/9784873113890/)』「オブジェクト指向エクササイズ」
- 全9つ。印象的なものを紹介

+++

## ルール7
## 1つのクラスにつきインスタンス変数は2つまでにすること

+++

### インスタンス変数は2つまで

```python
@dataclass
class PathPair:
    """(縮小対象のパス, 保存先のパス)という組"""
    _source: Path
    _destination: Path 


@dataclass
class SourceDestinationPair:
    """(縮小対象の画像のパス, 保存先のパス)という組"""
    _source: Path
    _destination: Path
```

@fa[github] [path_handler.py](https://github.com/ftnext/python-image-processor/blob/33a7c5405a56a3907bc47720d6e69ec35ef08cb4/myimageprocessor/path_handler.py)

+++

## ルール8
## ファーストクラスコレクションを使用すること

「コレクションを持つクラス」  
「他のメンバ変数を持たせない」  

+++

### ファーストクラスコレクション

```python
@dataclass
class SourceDestinationList:
    """SourceDestinationPairを格納するコレクション"""
    _pairs: List[SourceDestinationPair]

    def __iter__(self):
        return iter(self._pairs)

# __iter__を実装しているので
#   for pair in SourceDestinationList(pairs):
# とSourceDestinationListインスタンスをforで回せる
```

@fa[github] [path_handler.py](https://github.com/ftnext/python-image-processor/blob/33a7c5405a56a3907bc47720d6e69ec35ef08cb4/myimageprocessor/path_handler.py)

+++

### 詳しい話は2/24 OORCで

---

### まとめ：Pythonでオブジェクト指向

- 画像縮小スクリプトを例にLT
- 具体的なモノでなくてもクラスにしていい
- 具体的な実装のヒントは「オブジェクト指向エクササイズ」

+++

### ご清聴ありがとうございました

Contact: [@fa[twitter] @ftnext](https://twitter.com/ftnext)／[匿名質問箱](https://peing.net/ja/ftnext)
