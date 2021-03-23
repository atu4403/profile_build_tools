# profile_build_tools

githubプロフィールページのREADMEを自動作成するtools

`build.py`を作成して実行すると、それぞれのAPIから取得した情報からREADME.mdを作成できる。

see `test/build.py`

### APIの種類
1. pypiのパッケージリスト
2. qiitaの投稿記事リスト
3. githubのリポジトリリスト
4. AtCoderのグラフ画像をコピー


### 注意点
- pypiはuserごとのpackageを取得するAPIが無いのでパッケージ名を指定する必要がある。新しくpypiに登録した場合は要追加。
- githubはforkしたリポジトリは除外される
- githubのdescriotionを設定していないリポジトリは除外される
- githubのdescriotionはgithubのサイト右側の設定アイコンで変更できる

