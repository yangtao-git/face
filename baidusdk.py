import base64
import urllib

import cv2
import requests

API_KEY = "LrWNA5slYg6S2Bz2MxMR1J45"
SECRET_KEY = "sk78xCV1acxeI4KXFI02AlcA8MrJLc6j"


def baidu_sdk(file_path):
    url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect?access_token=" + get_access_token()

    # image 可以通过 get_file_content_as_base64("C:\fakepath\no (13).jpg",True) 方法获取
    image = get_file_content_as_base64(file_path,True)
    payload = 'image=' + image
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    return response.text


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

def get_image_by_file_path(file_path):
    result_dict_str = baidu_sdk(file_path)
    result_dict = dict(eval(result_dict_str))
    image_o = cv2.imread(file_path)
    image2 = image_o[result_dict['result']['top']:result_dict['result']['top'] + result_dict['result']['height'],
             result_dict['result']['left']:result_dict['result']['left'] + result_dict['result']['width']]
    return image2

if __name__ == '__main__':
    result_dict_str = baidu_sdk()
    result_dict = dict(eval(result_dict_str))
    # print("type ",type(result_dict))
    # {"result": {"top": 101, "left": 2, "width": 713, "height": 1171}, "log_id": 1798189316550029496}
    image_o = cv2.imread('./0624data/guangpan/ok (1).jpg')
    image2 = image_o[result_dict['result']['top']:result_dict['result']['top']+result_dict['result']['height'],result_dict['result']['left']:result_dict['result']['left']+result_dict['result']['width']]
    # cv2.imshow("image2",image2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
