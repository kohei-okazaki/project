# プロジェクトの作り方

## Anaconda navigator を開く

仮想環境を作成。（Environments=app2）  
 django を install

作成した仮想環境で ▶ ボタン押下  
「Open terminal」押下  
 ターミナルが出るので、作成したいプロジェクトまで移動して「django-admin startproject ${project_name}」を入力し、プロジェクトを初期化。  
 「asgi.py」や「settings.py」などがあるはず

# プロジェクト起動方法

1. VSCode で作成したプリジェクトの上位階層を開く（manage.py がある階層）
2. デバッグと実行を押下
3. 起動構成=Django を選択

# アプリケーションの作り方

1. プロジェクトフォルダまで「Anaconda Terminal」で移動
2. 「python manage.py startapp ${application_name}」実行

# URL マッピング

管理アプリ=http://127.0.0.1:8000/admin/login/
勤怠アプリ=http://127.0.0.1:8000/kintai/login/

# DB 設定

pip install mysqlclient
pip3 install PyMySQL

# マイグレーション手順

1. models.py にテーブル定義の Entity を記述
2. プロジェクトフォルダまで「Anaconda Terminal」で移動
3. manage.py makemigrations ${application_name}
4. python manage.py migrate

# 管理ユーザ作成

1. プロジェクトフォルダまで「Anaconda Terminal」で移動
2. python manage.py createsuperuser
3. username=admin, mail_address=admin@gmail.com, password=adminPass
