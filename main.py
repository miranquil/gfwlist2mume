import json
import time
import urllib
import os
import re
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/mume')
def mume():
    return mume_data()


@app.route('/surge')
def surge():
    return surge_data()


def export_data():
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

    direct_domains = rule_data[1][0]
    proxy_domains = rule_data[1][1]

    return direct_domains, proxy_domains


def mume_data():
    data = export_data()
    direct_domains = data[0]
    proxy_domains = data[1]
    rules = []
    for domain in direct_domains:
        item = {
            "action": "DIRECT",
            "pattern": domain,
            "type": "DOMAIN-SUFFIX",
            "order": "0"
        }
        rules.append(item)
    for domain in proxy_domains:
        item = {
            "action": "PROXY",
            "pattern": domain,
            "type": "DOMAIN-SUFFIX",
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

    return json.dumps(result)


def surge_data():
    data = export_data()
    proxy_name = request.args.get("proxyName")
    proxy_type = request.args.get("proxyType")
    browser = request.args.get("browser")
    final_value = request.args.get("final")
    shadowsocks = request.args.get("shadowsocks")
    direct_domains = data[0]
    proxy_domains = data[1]

    rules = []

    if not proxy_name:
        proxy_name = 'GFWListProxy'

    if not final_value:
        final_value = 'DIRECT'

    if not proxy_type:
        proxy_type = 'socks5'

    if shadowsocks is not None:
        proxy_type = 'custom'

    rules.append(f"[Proxy]")
    proxy_data = f"{proxy_name} = {proxy_type}, 127.0.0.1, 1080, username, password"
    if shadowsocks is not None:
        proxy_data += ",http://proxy.sofi.sh/SSEncrypt.module"
    rules.append(proxy_data)
    rules.append('')

    rules.append('[Rule]')
    for domain in direct_domains:
        rule_str = f"DOMAIN-SUFFIX,{domain},DIRECT"
        rules.append(rule_str)

    for domain in proxy_domains:
        if proxy_name:
            rule_str = f"DOMAIN-SUFFIX,{domain},{proxy_name}"
        else:
            rule_str = f"DOMAIN-SUFFIX,{domain},GFWListProxy"
        rules.append(rule_str)

    rules.append(f"FINAL,{final_value}")

    if browser is not None:
        return '</br>'.join(rules)
    return '\n'.join(rules)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
