import hashlib
text = input("Enter a String : ")

encoded_text = text.encode()
hash_object = hashlib.md5(encoded_text)
md5_hash = hash_object.hexdigest()

print("Code : ",md5_hash)