# ぷよぷよ通

本プロジェクトではPythonとPygameライブラリを使用し、ぷよぷよの連鎖を練習するためのゲームを実装します。

## 基本的なルール

- ぷよは4色（赤、緑、青、黄色）が降ってきます。ただし、ランダムに1色が欠けることがあります。
- 左右移動、左右回転が可能です。
- フィールドは6×14マスで、上2段は画面外で見えません。
- 12段目にぷよが積み上がると、PUYO_LOSE_POSにぷよが配置された時点でゲームオーバーとなります。
- 同じ色のぷよを4つ以上繋げると消えます。


## file
- constant.py: 定数を定義するファイル

### 取り扱わないもの

- お邪魔ぷよ
- 得点計算

## 仕様

### サウンド
- 本ゲームではサウンドは使用しません。

### キー配置

- 左移動: `←`
- 右移動: `→`
- 左回転: `z`
- 右回転: `x`
- 落下: `↓`

### 定数一覧

- `WIDTH`: ウィンドウの幅
- `HEIGHT`: ウィンドウの高さ
- `FPS`: ゲームのFPS
- `CELL_WIDTH`: フィールドのマスの幅
- `CELL_HEIGHT`: フィールドのマスの高さ
- `FIELD_WIDTH`: フィールドの幅（マス数）
- `FIELD_HEIGHT`: フィールドの高さ（マス数）
- `PUYO_COLORS`: ぷよの色とそのRGB値
  - `RED`: `#FF0000`
  - `GREEN`: `#00FF00`
  - `BLUE`: `#0000FF`
  - `YELLOW`: `#FFFF00`
- `PUYO_FALL_SPEED`: ぷよの落下速度
- `PUYO_FAST_FALL_SPEED`: ぷよの落下速度（高速）
- `PUYO_LOSE_POS`: ゲームオーバーとなるぷよの座標
- `PUYO_ROTATE_STATE`: ぷよペアの回転状態
  - `UP`: 上向き
  - `RIGHT`: 右向き
  - `DOWN`: 下向き
  - `LEFT`: 左向き
- `KEY_LEFT`: 左キー
- `KEY_RIGHT`: 右キー
- `KEY_DOWN`: 下キー
- `KEY_Z`: Zキー
- `KEY_X`: Xキー

### クラス一覧

#### Puyo クラス

単体のぷよを扱うクラス。

##### テスト項目
- ぷよの初期化時に指定した色が正しく設定されることを確認する。
- 画面上の指定された座標にぷよが正しく描画されることを確認する。
- ぷよの色がRGB値と一致していることをテストする。

##### メソッド

- `__init__(self, color)`: ぷよを初期化する。
- `draw(self, x, y)`: ぷよを描画する。
  - `x`: ぷよのフィールド上のX座標。
  - `y`: ぷよのフィールド上のY座標。
  - 描画時に画面座標へ変換する。

##### プロパティ

- `color`: ぷよの色。

#### PuyoPair クラス

現在降下中のぷよペアを扱うクラス。

##### テスト項目
- 生成時の2つのぷよがランダムな色で正しく作成されることを確認する。
- 回転操作時にぷよペアが正しく回転し、画面上に反映されることをテストする。
- 移動操作時にぷよペアが指定された方向に正しく移動することを確認する。

##### メソッド

- `__init__(self, puyo_main, puyo_sub)`: ぷよペアを初期化する。
  - ランダムに2つの色を選び、ぷよを生成する。
- `draw(self)`: ぷよペアを描画する。
- `rotate(self, direction)`: ぷよペアを回転させる。
  - `direction`: 回転方向（`LEFT`または`RIGHT`）。
- `move(self, dx, dy)`: ぷよペアを移動させる。
  - `dx`: X方向の移動量。
  - `dy`: Y方向の移動量。

##### プロパティ

- `puyo_main`: メインのぷよ。
- `puyo_sub`: サブのぷよ。
- `x`: フィールド上のX座標。
- `y`: フィールド上のY座標。
- `rotation_state`: 回転状態（`UP`、`RIGHT`、`DOWN`、`LEFT`）。

#### NextPuyo クラス

次に降ってくるぷよペアを扱うクラス。

##### テスト項目
- 次のぷよペアが正しく生成され、画面上に表示されることを確認する。
- ぷよペアの色がランダムで前回と異なる場合をテストする。

##### メソッド

- `__init__(self)`: 次のぷよペアを初期化する。
  - ランダムに2つの色を選び、ぷよを生成する。
- `draw(self)`: 次のぷよペアを描画する。

##### プロパティ

- `puyo_main`: メインのぷよ。
- `puyo_sub`: サブのぷよ。

#### Field クラス

フィールドを扱うクラス。

##### テスト項目
- 指定された座標にぷよが正しく配置されることを確認する。
- 連結した4つ以上のぷよが消去されることをテストする。
- 重力適用後、空白部分に上部のぷよが落下することを確認する。
- ゲームオーバー条件（PUYO_LOSE_POS）が正しく判定されることをテストする。

##### メソッド

- `__init__(self)`: フィールドを初期化する。
- `draw(self)`: フィールドを描画する。
- `set_puyo(self, x, y, puyo)`: フィールドにぷよをセットする。既にぷよがある場合は上書きする。
  - `x`: フィールド上のX座標。
  - `y`: フィールド上のY座標。
  - `puyo`: ぷよ。
- `is_settable(self, x, y)`: 指定した位置にぷよを配置可能かを返す。
  - `x`: フィールド上のX座標。
  - `y`: フィールド上のY座標。
- `delete_puyo(self, x, y)`: フィールドの指定位置のぷよを削除する。
  - `x`: フィールド上のX座標。
  - `y`: フィールド上のY座標。
- `delete_connected_puyo(self)`: 連結しているぷよを探索し、4つ以上繋がっている場合に消去する。
- `apply_gravity(self)`: 空いたスペースがある場合、上のぷよを落下させる。
- `check_game_over(self)`: ゲームオーバーかどうかを判定する。

##### プロパティ

- `field`: フィールドの状態（2次元配列）。

#### Game クラス

ゲーム全体を管理するクラス。

##### テスト項目
- ゲームループが正常に実行され、画面が更新されることを確認する。
- キーイベント（左右移動、回転、落下）が正しく処理されることをテストする。
- ゲームオーバー時やぷよ消去時の挙動が正しいことを確認する。

##### メソッド

- `__init__(self)`: ゲームを初期化する。
- `run(self)`: ゲームを実行する。
- `draw(self)`: ゲーム全体を描画する。
- `update(self)`: ゲームの状態を更新する。
- `handle_key_event(self, event)`: キーイベントを処理する。
  - `event`: `pygame.event.get()`で取得したイベント。

##### プロパティ

- `field`: フィールド。
- `falling_puyo`: 現在降下中のぷよペア。
- `next_puyo`: 次に降ってくるぷよペア。
- `next_next_puyo`: 次の次に降ってくるぷよペア。
