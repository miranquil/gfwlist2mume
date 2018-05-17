# gfwlist2mume

[![GenPAC](https://img.shields.io/badge/workwith-genpac-brightgreen.svg)](https://github.com/JinnLynn/GenPAC) [![License](https://img.shields.io/badge/license-GPL--3.0-brightgreen.svg)](https://github.com/yorushika/gfwlist2mume/blob/master/LICENSE)
![Docker Build Status](https://img.shields.io/docker/build/yorushika/gfwlist2mume.svg)

A script transforms gfwlist to rules which can be imported directly to Mume&寒梅 at iOS.

在线获取GFWList并转换为寒梅&Mume规则的脚本，可直接用于App内URL导入功能。

## INSTALL

### 手动安装

```
pip install -r requirements.txt
python main.py
```

### 使用Docker

#### 本地构建

```
docker build -t gfwlist2mume .
docker run --rm -it -p 8000:8000 gfwlist2mume
```

#### Docker Hub

```
docker pull yorushika/gfwlist2mume
docker run --rm -it -p 8000:8000 yorushika/gfwlist2mume
```

## USE

### 寒梅&Mume

```
http://host:port/mume
```

### Surge

```
http://host:port/surge [?] [proxyName=$proxyName] [proxyType=$proxyType]  [final=$final] [browser] [shadowsocks]
```

#### 生成文档示例

> [Proxy]
> $proxyName = $proxyType, 127.0.0.1, 1080, username, password
>
> [Rule]
> DOMAIN-SUFFIX,baidu.com,DIRECT
> DOMAIN-SUFFIX,twitter.com,$proxyName
> FINAL, $final


#### 参数

proxyName: 生成规则中所用代理服务器名称，默认GFWListProxy。

proxyType：代理服务器类别，http、socks5等。

final：Surge 规则集必须包含的FINAL行，规定当前URL未匹配到规则时的行为。默认DIRECT（直连）。*若不想直连，请指定为现有的proxyName*

browser：将输出结果添加浏览器用换行符，适合复制后二次编辑。*不要用来直接导入*

shadowsocks：使用shadowsocks服务器，导入后会提示下载module文件。

* 激活shadowsocks选项后，无论proxyType指定了何种类型，生成的proxyType强制custom。
* 若默认地址失效，请在surge_module文件夹中找到module文件并自行部署。

## Copyrights

感谢[@sofish](https://github.com/sofish)无私分享module文件。

感谢[@JinnLynn](https://github.com/JinnLynn)的genpac工具，由于本人太懒实在不想再做一遍转换了Orz。