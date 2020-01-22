"""
2019/12/15
Lectura de datos de tipo JSON
by Igor Remolar 2019
"""

import json
import requests

class EasyGoBandTest:
    def __init__(self):
        self.url = "https://pnny0h3cuf.execute-api.eu-west-1.amazonaws.com/dev/providers/"
        self.id = '1'
        self.headers = {
            'Authorization' : 'Basic cJmAc71jah17sgqi1jqaksvaksda='
        }
        self.json_data = []
        self.data = {}

    def load_data(self, url=None, id_=None, headers=None):
        if not url:
            url = self.url
        if not id_:
            id_ = self.id
        if not headers:
            headers = self.headers
        r = requests.request('GET', url + id_, headers=headers)
        self.json_data = json.loads(r.content)
        for data in self.json_data.copy():
            for session in data['sessions']:
                name = session['name']
                if self.data.get(name):
                    self.data[name].append(data)
                else:
                    self.data[name] = [data]

    def get_session_names(self):
        return list(self.data.keys())

    def show_session_name(self, session_name):
        items = self.data[session_name] if self.data.get(session_name) else []
        if items:
            i = 1
            for item in items:
                print(f"{i:> 6}", item)
                i += 1

    def show_session_names(self):
        for name in self.data:
            print(name)
        print()

    def show_json_data(self):
        print(json.dumps(self.json_data, indent=4))


if __name__ == '__main__':
    easygoband = EasyGoBandTest()
    easygoband.load_data()
    easygoband.show_session_names()
    for name in easygoband.get_session_names():
        print(f"{name} ({len(easygoband.data[name])})")
        easygoband.show_session_name(name)
        print()