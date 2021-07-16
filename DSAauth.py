from Crypto.PublicKey import DSA
from Crypto.Hash import SHA256
from Crypto.Signature import DSS


# 秘密鍵ファイルの読み込み
f_private = open("private_key.pem", 'r')
privateKey = DSA.import_key(f_private.read())

# 公開鍵ファイルの読み込み
f_public = open("public_key.pem", 'r')
publicKey = DSA.import_key(f_public.read())

message = b"TEST MESSAGE"
# hashオブジェクトの生成
hash_obj = SHA256.new(message)
# hash関数と秘密鍵で署名を生成
signature = DSS.new(privateKey, 'fips-186-3').sign(hash_obj)

# 公開鍵で復号する
verifier = DSS.new(publicKey, 'fips-186-3')

# 検証
try:
    verifier.verify(hash_obj, signature)
    print("Authentic")
except ValueError:
    print("Not Authentic")