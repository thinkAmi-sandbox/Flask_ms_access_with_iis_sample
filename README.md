# Flask_ms_access_with_iis_sample

## Tested environment

- IIS 7.0 64bit
- Microsoft Access Database Engine 2010 Redistributable
- Python 3.4.4 32bit
- Flask 0.10.1
- SQLAlchemy 1.0.12
- sqlalchemy-access 0.8.dev0
- pyodbc 3.0.10

　  
## Setup
### Install MS Access Database Engine
[Download Microsoft Access Database Engine 2010 Redistributable from Official Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=13255)

　  
### IIS settings
#### Install IIS and FastCGI
[CGI <cgi> : The Official Microsoft IIS Site](https://www.iis.net/configreference/system.webserver/cgi)

　  
#### Apply KB980363
(optional) for IIS 7.0

- [Important update for IIS 7.0 FastCGI module | RuslanY Blog](http://ruslany.net/2010/03/important-update-for-iis-7-0-fastcgi-module/)
- [IIS7.0 + Python3 + wfastcgi 構成のWSGIアプリ作成時に発生したエラーのメモ - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/03/28/232319)

　  
#### Add Website
Using IIS Manager

　  
#### Open firewall TCP port
only inbound

　  
### Flask app
#### Create app environment

```
>cd path\to\dir

path\to\dir>git clone https://github.com/thinkAmi-sandbox/Flask_ms_access_with_iis_sample.git


path\to\dir>virtualenv -p c:\python34\python.exe env
path\to\dir>env\Scripts\activate

(env)path\to\dir>pip install -r requirements.txt

(env)path\to\dir>wfastcgi-enable
```

　  
### Edit web.config
Update `scriptProcessor` value using `wfastcgi-enable` results.

　  
then, access your Flask app site.

　  
## Related Blog posts (written in Japanese)

[Python3 + Flask + wfastcgi のアプリを、IISでホストする - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/04/02/083401)