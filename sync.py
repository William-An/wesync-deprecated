import itchat
import requests
import base64
from itchat.content import *

integromatHook = ''

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    # IPython.embed()
    url, params, headers, core = msg.download(msg.fileName)
    file_res = core.s.get(url, params=params, headers=headers)
    # open(msg.fileName,'wb').write(file_res.content)
    res = requests.post(integromatHook,
                        data={"filename":msg.fileName,"data":base64.encodebytes(file_res.content).decode()})
    print(res)

itchat.auto_login(enableCmdQR=False,hotReload=True)
itchat.run(True)
