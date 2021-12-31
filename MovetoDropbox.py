import dropbox

class TransferData:
    def _init_(self,access_token):
        self.access_token= access_token

    def upload_file(self,file_from,file_to):
        dbx= dropbox.Dropbox(self.access_token)
        
        with open(file_from,'rh') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.A_LOXKzkJBwWZX6IPJFCDhX1bNmGU1FFEPT-ZU4e-4NzSy_hNQfnaKy2l1nM7Iz4VNzsSLQapRmBjgRXEjw2wOokAexbeXORNwK8irDkQMjTYA6Ua2yzmxHiHxoHnTItUiqW9U4'
    transferData=TransferData(access_token)

    file_from= input("enter the file path to transfer")
    file_to= input("enter the full path to enter to dropbox")

    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()
