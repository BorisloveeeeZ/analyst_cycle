# Разработать класс, которому на вход будет приходить разобранный запрос от пользователя. Запрос имеет вид:
# будет приходить запрос в виде словаря:
# request = {
#  "cookies": {key_1: value_1, key_2: value_2, ...},
#  "body": "a long time ago, in a Galaxy far, far away",
# "headers": {"content-type": "application/json", "Accept": "application/json"}
# }

# Разным классам в приложении потребуется разная функциональность: кому-то потребуется проверять, есть ли в headers ключ "Accept", 
# кому-то потребуется читать body, а кому-то понадобится проверять пустоту cookies. Будут и классы, которым потребуется несколько возможностей сразу.
# Напишите классы ParsesCookies, ParsesBody, ParsesHeaders, JsonHandler( Если need_json() дает False, то возвращать None
# Иначе получать тело через body(), пытаться считать его как json.loads(...) и возвращать число ключей в словаре. Если считать не удалось, то вернуть None),
# SecureTextHandler Если is_authed() дает False, то возвращать None. Иначе получать тело через body() и возвращать его длину.

import json
class ParsesCookies:
    
    def __init__(self, request):
        self.request = request
    
    def cookies(self):
        return self.request['cookies']


    def is_authed(self):
        return 'auth_key' in self.request['cookies'].keys()


class ParsesBody:
    
    def __init__(self,request):
        self.request = request

    def body(self):
        return self.request['body']


class ParsesHeaders:
    
    def __init__(self, request):
        self.request = request


    def headers(self):
        return self.request['headers']

    def need_json(self):
        return self.request['headers'].get("content-type") == "application/json"


class JsonHandler(ParsesBody,ParsesHeaders):

    def __init__(self, request):
        self.request = request

    def process(self):
        if self.need_json() == False:
            return None
        else:
            try:
                res = json.loads(self.body())
                return len(res.keys())
            except:
                return None


class SecureTextHandler(ParsesBody, ParsesHeaders, ParsesCookies):

    def __init__(self, request):
        self.request = request

    def process(self):
        if not self.is_authed():
            return None
        else:
            return len(self.body())
