# Download Xiaoet
> 小鹅通资源下载工具

## 一、安装

#### 1. 安装python 依赖
```
sudo pip3 install ffmpy m3u8 beautifulsoup4
```
#### 2. 安装ffmpeg
```
CentOS
https://download1.rpmfusion.org/free/el/updates/7/x86_64/repoview/letter_f.group.html

Ubuntu
https://launchpad.net/ubuntu/+source/ffmpeg
```

## 二、使用方法示例     

#### 1. 下载单个resource(视频/音频)
```
python3 xiaoet.py <店铺ID> -d <ResourceID>
```
#### 2. 下载一个product(专栏)所有resource(视频/音频)
```
python3 xiaoet.py <店铺ID> -d <ProductID>
```
#### 3. 列出一个app(店铺)所有product(专栏)(部分商铺可能失效)
```
python3 xiaoet.py <店铺ID> -pl
```
#### 4. 列出该product(专栏)下所有resource(视频/音频)
```
python3 xiaoet.py <店铺ID> -rl <ProductID>
```
#### 5. 列出resource(视频/音频)的product_id(专栏ID)
```
python3 xiaoet.py <店铺ID> -r2p <ResourceID>
```
#### 6. ffmpeg合成视频
```
python3 xiaoet.py <店铺ID> -tc <ResourceID>
```
#### 7. 根据rid list批量下载视频 
```
python3 xiaoet.py <店铺ID> -tc <ResourceID>
```
#### 8. 根据rid list批量ffmpeg合成视频
```
python3 xiaoet.py <店铺ID> -tc <ResourceID>
```
备注：
1. 登录需要微信扫码登录，session时效性为4小时，更换店铺需要重新扫码登录
2. 默认下载目录为同级download目录下，下载完成后视频为分段，将自动合成；音频不需要合成。
3. 店铺为`appxxxx`,专栏ID(ProductID)为`p_xxxx_xxx`,资源ID分为视频与音频分别为`v_xxx_xxx`、`a_xxx_xxx`
4. 图文资源ID为`i_xxx_xxx`，图文中有时含有资源链接
5. 直播/回看资源ID为`l_xxx_xxx`，暂不支持下载
6. 仅可下载已购买资源
