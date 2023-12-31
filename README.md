# バージョン情報

| 名前   | バージョン |
| ------ | ---------- |
| Python | 3.8.17     |
| pip    | 23.2.1     |
| django | 4.1        |

# プロジェクト構成

## 勤怠管理

勤怠管理アプリ

# プロジェクトの作り方

## Anaconda Navigator を開く

1. 仮想環境を作成。（Environments=app2）  
2. django を install
3. 作成した仮想環境で ▶ ボタン押下  
4. 「Open terminal」押下  
5. ターミナルが出るので、作成したいプロジェクトまで移動して `django-admin startproject ${project_name}` を入力し、プロジェクトを初期化。  
6. 「asgi.py」や「settings.py」などがあるはず。

## Anaconda Prompt を開く

1. 検索窓から`Anaconda Prompt`
2. `activate app2`
3. `D:`
4. `cd app2\project`

# プロジェクト起動方法

1. VSCode で作成したプリジェクトの上位階層を開く（manage.py がある階層）
2. デバッグと実行を押下
3. 起動構成=Django を選択

# アプリケーションの作り方

1. プロジェクトフォルダまで「Anaconda Terminal」で移動
2. `python manage.py startapp ${application_name}` 実行

# URL マッピング

管理アプリ=http://127.0.0.1:8085/admin/login/  
勤怠アプリ=http://127.0.0.1:8085/kintai/login/

# DB 設定

`pip install mysqlclient`  
`pip3 install PyMySQL`

# マイグレーション手順
1. models.py にテーブル定義の Entity を記述
2. プロジェクトフォルダまで「Anaconda Terminal」で移動
3. VSCodeから「Make Migrate」を実行
4. VSCodeから「Migrate」を実行

以下、備忘録として残す
`python manage.py makemigrations ${application_name}`
`python manage.py migrate`

# 管理ユーザ作成

1. プロジェクトフォルダまで「Anaconda Terminal」で移動
2. `python manage.py createsuperuser`
3. `username=admin, password=adminPass`

# Git への反映

1. ファイルを作成後、SourceTree で「Local」->「Create」
2. 作業フォルダ上を選択、リポジトリ名=「project」、「Git」
3. 作成ボタン押下
4. Github で「project」でリモートリポジトリを作成
5. SourceTree から Git ターミナルを開く
6. `$ git add \*`
7. `$ git commit -m 'first commit'`
8. `$ git remote add ${Github から取得したリポジトリ URL}`
9. `$ git push ${Github から取得したリポジトリ URL}`
