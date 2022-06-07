# e-portem-downloader
Tool that allows you to download all your documents in e-portem portal

## How to use it
1. Log in e-portem (Open developer tools before login and go to network tab).<br />![login](/images/login.png)
2. Copy the ASPXAUTH cookie value.<br />![cookie](/images/cookie-aspxauth.png)
3. create a `.env` file in e-portem-downloader folder.<br />![envfile](/images/env-file.png)
4. run in console -> `docker-compose build`.
5. run in console -> `docker-compose run --rm eportem_downloader sh -c "python main.py"`.
6. Once is finished you will see all your documents.<br />![output](/images/output.png)
