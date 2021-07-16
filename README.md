# DSAauth
------------------------
Projectの署名かいてみようのプログラム

## GenKey.py 
1. 秘密鍵
　private_key.pem

2. 公開鍵
　public_key.pem
　public_key_dammy.pem

を生成する

## DSAauth.py
ハッシュ関数と秘密鍵を使った署名の作成、復号

公開鍵読み込みの際には、ダミーの公開鍵を指定することで検証失敗の動作が確認できる
## Package
- dsa
- pycryptodome