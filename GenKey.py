from Crypto.PublicKey import DSA

# 1024bit DSAで秘密鍵生成
key = DSA.generate(bits=1024)
dammyKey = DSA.generate(bits=1024)

# 秘密鍵のファイル生成
with open("private_key.pem", "w") as f:
    f.write(key.export_key().decode('utf-8'))

#　秘密鍵をもとに公開鍵のファイル生成
with open("public_key.pem", "w") as f:
    f.write(key.publickey().export_key().decode('utf-8'))

#　ダミーの秘密鍵をもとに公開鍵のファイル生成
with open("public_key_dammy.pem", "w") as f:
    f.write(dammyKey.publickey().export_key().decode('utf-8'))