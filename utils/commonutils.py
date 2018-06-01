import hashlib

def md(text):
    md5=hashlib.md5()
    md5.update(text.encode("utf8"))
    return md5.hexdigest()