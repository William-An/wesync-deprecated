# Wesync
A simple python project that automatically synchronizes wechat files to Google Drive/Any Cloud Drive save PanBaidu   
一个神奇的Python项目, 同步你的微信文件

# 原理
- 用[itchat](https://github.com/littlecodersh/ItChat)第三方微信API登陆
- 当接收到图片或文件时, 调用下载并将文件储存在内存
- 推送到[integromat](https://integromat.com) 然后自动推送至云端储存
- 推送status_code与fileName至文件传输助手
	- 400
		- integromat 错误, 建议查看History
	- 200
		- 请求成功
		- 同时返回下载连接

# 配置
## Integromat
自动化配置
1. [https://www.integromat.com/](https://www.integromat.com/) 注册
2. 新建Scenario
	- Webhooks: Custom Webhook
		- Add webhook
			- Add Data Structure
				- Add item
					- data
						- Name: data
						- Type: text
					- filename
						- Name: filename
						- Type: text
		- Copy webhook url
	- Google Drive
		- Choose a folder
		- File name: filename
		- Data: toBinary(data; base64)
		- Error Handler (right click this module)
			- Webhook Response
				- Status: 400
			- Ignore
	- Webhooks: Webhook Response
		- Status: 200
		- Body: Share Link

## Windows
    git clone https://github.com/William-An/wesync
    wesync/Scripts/activate
    # 预先将webhook的URL在sync.py中赋值为integromat
    python sync.py
    # enableCmdQR一定要为True
更多信息详见[itchat](https://github.com/littlecodersh/ItChat)文档

## Linux
TO BE Continue

# 注意事项
- 云端储存并不一定要Google Drive, 可以使用其他的云端服务像Dropbox
- 上传到Google Drive的文件是默认**开放**查看权限的, 拥有**链接**的人就可以查看或下载, 请自行衡量 