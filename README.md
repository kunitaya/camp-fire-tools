# camp-fire-tools

##### for Windows

+ Python 3.10.1 のインストール

    + [公式サイト](https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe)からダウンロードしてインストール
    + 「Optional Features」で、「pip」にチェック
    + 「Advanced Options」で、「Add Python to environment variables」にチェック

+ pipenv のインストール

    ```
    pip install pipenv
    ```

+ 仮想環境の構築

    ```
    pipenv --python 3.10.1
    pipenv install --dev
    copy .vscode\settings.json.sample .vscode\settings.json
    ```

+ Terminal の再起動
+ デバッグ設定の作成

    + .vscode/launch.json.sample をコピーして .vscode/launch.json を作成
    + launch.json の中の環境変数を適宜変更


### JSON から CSV への変更
```
jq -r '["project","projectName","displayUserName","url","time","comment"],(.[]|[.project,.projectName,.displayUserName,.url,.time,.comment])|@csv' result.json > result.csv
```