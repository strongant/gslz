 # @soap(String, _returns=String)  # 声明一个服务，标识方法的参数以及返回值
    # # 上传文件和关键词文件信息
    # def uploadFile(self, jsonstr):
    #     # 用于返回的json信息
    #     resultJson = {}
    #     # 用于存放不合法的url
    #     errorUrl = []
    #     # 将批量写入es的集合
    #     builkUrlList = []
    #     # 这里解析json，将json数据中的file字段获取通过base64解密解析成一个csv文件
    #     if (validateuser):
    #         print  jsonstr
    #         jsonfile = json.loads(jsonstr)
    #         filestr = jsonfile['file']
    #         fileata = base64.b64decode(filestr)
    #         hashname = hashlib.md5(fileata).hexdigest()
    #         # 进行文件保存的工作
    #         saveResullt = write('../temp', hashname, fileata)
    #         if (saveResullt):
    #             # 执行文件解析，将解析后的url地址存到es中，
    #             # 并且开启抓取的任务（抓取流程为使用celery调用抓取网页的操作，
    #             # 将抓取后的元文件内容写入到s3云存储，将解析之后的文本信息写入es，
    #             # 同时当某个url地址抓取完成之后调用通过关键字统计网页命中次数的方法）
    #             if fileata is not None and len(fileata) > 0:
    #                 urls = fileata.split('\n')
    #                 # 将第一行的标题去掉，只验证有效的url
    #                 del urls[0]
    #                 # 调用向es中批量插入url信息
    #                 index = 'fetch'
    #                 urlType = 'urls'
    #                 pageType = 'page'
    #                 # 创建临时存放需要插入es中的url集合
    #                 for url in urls:
    #                     # 校验网址的正确性
    #                     if (validateUrl(url)):
    #                         # 根据url抓取网页内容保存到data目录下，如果抓取的网页已经存在，则不进行保存
    #                         urlFileName = getFileName(url)
    #                         filePath = os.path.abspath(os.path.dirname('../data/')) + '/%s' % urlFileName
    #                         print 'filePath:', filePath
    #                         print 'exists:', os.path.exists(filePath)
    #                         existsResult = os.path.exists(filePath)
    #                         if not existsResult:
    #                             # 下载文件并返回当前抓取的内容信息
    #                             # fileNameResult = downloadbyurl.delay(url, os.path.abspath(os.path.dirname('../data/')))
    #                             # fileName = fileNameResult.get()
    #                             # 抓取页面内容保存到本地，将页面内容保存到es
    #                             create_page_info(url, filePath, hashname, index, pageType)
    #                         # 使用url的hash作为es中的_id值
    #                         urlHash = hashlib.md5(url).hexdigest()
    #                         # 创建时间
    #                         createTime = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    #                         tempStr = '{ "index" : { "_id" : "' + urlHash + '" } }\n{ "url":"' + url + '","createDate" :"' + createTime + '" }\n'
    #                         builkUrlList.append(tempStr)
    #                     else:
    #                         errorUrl.append(url)
    #                 # 通过celery进行调度向es插入数据的操作
    #                 result = sendPageDataToEs.delay(index, urlType, builkUrlList)
    #                 print 'celery result:', result
    #             else:
    #                 resultJson['message'] = 'Pass the site information is empty'
    #             # 执行状态
    #             resultJson['status'] = 'success'
    #             # 本次发送的任务编号
    #             resultJson['taskid'] = hashname
    #             # 任务执行消息
    #             resultJson['message'] = 'recevied success'
    #         else:
    #             resultJson['status'] = 'fail'
    #             # 任务执行消息
    #             resultJson['message'] = 'file already exists'
    #
    #     else:
    #         resultJson['status'] = 'fail'
    #         resultJson['message'] = 'check failed'
    #     return str(resultJson)
