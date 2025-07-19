extension = {
    "gif" : "image/gif",
    "jpg" : "image/jpeg",
    "jpeg" : "image/jpeg",
    "png" : "image/png",
    "pdf" : "application/pdf",
    "txt" : "text/plain",
    "zip" : "application/zip"
}

str = input("File name: ").lower().strip().split(".")[-1]
try:
    print(extension[str])
except KeyError:
    print("application/octet-stream")
