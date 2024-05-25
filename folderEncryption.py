from cryptography.fernet import Fernet
import os
import datetime

class FolderEncrypter:
    def __init__(self, key, folderPath) -> None:
        self.key = Fernet(key)
        self.folderPath = folderPath

        if not os.path.isdir(self.folderPath):
            os.mkdir(self.folderPath)

    def encrypt(self, content):
        return self.key.encrypt(content)

    def decrypt(self, content):
        return self.key.decrypt(content)

    def store(self, content, fileType):
        time = str(datetime.datetime.now()).replace(" ", "-").replace(":", "-")
        with open(f"{self.folderPath}/{time}.{fileType}", "wb") as file:
            file.write(self.encrypt(content))

    def decryptInfo(self):
        resultPath = f"decrypted{self.folderPath}"
        os.mkdir(resultPath)

        for file in os.listdir(self.folderPath):
            with open(f"{self.folderPath}/{file}", "rb") as encryptedfile:
                content = encryptedfile.read()
                decryptedContent = self.decrypt(content)

                with open(f"{resultPath}/{file}", "wb") as decryptionFile:
                    decryptionFile.write(decryptedContent)
def main():
    key = input("key: ")
    folder = input("folder name: ")
    encryptor = FolderEncrypter(key, folder)

    encryptor.decryptInfo()
           
if __name__ == "__main__":
    main()
