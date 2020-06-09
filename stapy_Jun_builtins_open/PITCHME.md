## 組み込み関数openの秘密
#### みんなのPython勉強会 #57 LT
#### 2020/06/10 nikkie

---

### お前、誰よ (About nikkie)

- ハンドルネーム「にっきー」 (@fa[twitter] [@ftnext](https://twitter.com/ftnext))
- Python🐍歴2年ほど。仕事ではPythonで機械学習 & Web API開発
- みんなのPython勉強会スタッフ 兼 4代目LT王子🤴

+++

### お知らせ
### スタッフをしているはPyCon JP 2020
### 8/28(金),29(土) オンライン開催
### スタッフ募集中

---

### ファイルopenしてますか？

```python
# やり方 (1)
f = open('awesome.txt')

# やり方 (2)
with open('awesome.txt') as f:
```

ref: https://pycamp.pycon.jp/textbook/5_module.html

+++

### LTの本題：単に`open`と`with open`、`f`という変数に代入するものに違いはあるのか？

+++

### `with open('awesome.txt') as f:` では

- `open('awesome.txt')`の返り値の`__enter__`メソッドが実行される
  - `with`に渡せるもの：[コンテキストマネージャ](https://docs.python.org/ja/3/reference/datamodel.html#context-managers)
- **`__enter__`メソッドの返り値**が`f`に代入される

[Pythonドキュメント 8. 複合文 8.5 with文](https://docs.python.org/ja/3/reference/compound_stmts.html#the-with-statement)

+++

### fに代入されるものの違いは？

```python
# (1) fはopenの返り値を指す
f = open('awesome.txt')

# (2) fはopenの返り値の__enter__の返り値を指す
with open('awesome.txt') as f:
```

---

# 結論：fに代入されるものに違いはない

+++

### [PEP 3116](https://www.python.org/dev/peps/pep-3116/)

- `__enter__()`は`self`を返す（`self`はコンテキストマネージャ自身）
- `open('awesome.txt')`の返り値を`f`とすると、`f.__enter__()`は`f`を返す
- （余談）PEP3116によると`__exit__`は`close`を呼ぶ（👉`with`を使えば`close`不要）

+++

### 試してみる

```python
>>> f = open('awesome.txt')
>>> f
<_io.TextIOWrapper name='awesome.txt' mode='r' encoding='UTF-8'>
>>> t = f.__enter__()
>>> t
<_io.TextIOWrapper name='awesome.txt' mode='r' encoding='UTF-8'>
>>> f == t  # 同じオブジェクトを指す
True
>>> id(f), id(t)
(4466170368, 4466170368)
```

---

### 実装を見てみる

- @fa[github] https://github.com/python/cpython
- [Lib](https://github.com/python/cpython/tree/master/Lib)以下に標準ライブラリの実体がある
- C実装（`Modules/_io`）とPython実装（`Lib/_pyio.py`）

+++

### 2つの実装がある理由

- Python 3.0でPEP3116を実装したところボトルネックが発生
- Python3.1では**Cで書き直し**、2〜20倍高速化
- Python実装が`_pyio`として残る

https://docs.python.org/ja/3/whatsnew/3.1.html#optimizations

+++

### openのC実装

@fa[github] https://github.com/python/cpython/blob/master/Modules/_io/_iomodule.c#L100

今の私には意味の取れないコードでした。。😢

---

### まとめ：組み込み関数openの秘密

- `f = open('awesome.txt')`の`f`と`with open('awesome.txt') as f:`の`f`で代入されるものに違いはない
- その理由は、コンテキストマネージャの`__enter__`が自身を返すため
- Pythonのソースを読むにはCが必要な箇所もある

+++

### ご清聴ありがとうございました

Contact: [@fa[twitter] @ftnext](https://twitter.com/ftnext)／[匿名質問箱](https://peing.net/ja/ftnext)
