import json
import time
import urllib
import os
import re
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return json.dumps(data_generate())


def data_generate():
    gfwlist_url = 'https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt'
    gfwlist_txt = urllib.request.urlopen(gfwlist_url).read().decode()

    with open('gfwlist.txt', 'w', encoding='utf-8') as fout:
        for line in gfwlist_txt:
            fout.write(line)

    os.system(
        'genpac --format=pac --gfwlist-url - --gfwlist-local gfwlist.txt --pac-proxy="SOCKS5 127.0.0.1:8080" -o pac.txt')

    with open("pac.txt", "r", encoding='utf-8') as pacfile:
        pac_data = pacfile.read()
        
    rule_data = re.search(r'var rules = ([\S\s]*?]);', pac_data).group(1)
    rule_data = json.loads(rule_data)
    domains = rule_data[1][1]

    rules = []
    for domain in domains:
        item = {
            "action": "PROXY",
            "pattern": domain,
            "type": "URL",
            "order": "0"
        }
        rules.append(item)

    rule_set = {
        'is_official': False,
        'description': '由GFWList生成的规则',
        'id': '596f7275-7368-696b-6100-6f776e706163',
        "rules": rules,
        'name': 'GFWList',
    }

    rule_set_list = [rule_set]
    result = {
        "ruleSets": rule_set_list,
    }

    return result


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
