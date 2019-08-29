import urllib.request

def HttpDownload(url, path):
    if url == "" or path == "":
        print("url or path not configured")
        return ""
    result = ""
    try:
        urllib.request.urlretrieve(url, path)
        result += "download from " + url + " to " + path + " successful"
        print("download from " + url + " to " + path + " successful")
    except Exception:
        result += "http download failed"
        print("http download failed")

    return result