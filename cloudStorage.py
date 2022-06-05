from os import access
import dropbox

class cloudstorage:
    def __init__(self, accessToken):
        self.accessToken = accessToken


    def uploadFile(self,sourceFolder, DestinationFolder):
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(sourceFolder, 'rb')
        dbx.files_upload(f.read(), DestinationFolder)

def main():
    accessToken = 'sl.BIudSYYl6kaaVeh0i2jgidyaPK-Z4-QiZQaDPO52Mmi49khtO0i7_wmfcU3VqWnWecZKGd4RXI8s9MRBzSuHDoTpCGl0G10PyjxumCnUcObKykkihDKrnnQtmRSXUFyJHcKGeCK6Auuh'
    transferData = cloudstorage(accessToken)
    sourceFolder = input('enter the sourcefile')
    destinationFolder = input('enter the destination file')
    transferData.uploadFile(sourceFolder, destinationFolder)
    print('file has been moved')

main()


