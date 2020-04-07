## Scraping Data behind Site Logins

It's How Scraping Data that need requires Login

<a href="https://github.com/MKRyuto/Scraping-Data-behind-Site-Logins/blob/master/">
    <img alt="Aigner" src="https://i.imgur.com/958B2pr.png" target="_blank" />
</a>

A Python library for automating interaction with websites. MechanicalSoup automatically stores and sends cookies, follows redirects, and can follow links and submit forms. It doesn’t do Javascript.

MechanicalSoup was created by M Hickford, who was a fond user of the Mechanize library. Unfortunately, Mechanize is incompatible with Python 3 and its development stalled for several years. MechanicalSoup provides a similar API, built on Python giants Requests (for http sessions) and BeautifulSoup (for document navigation). Since 2017 it is a project actively maintained by a small team including @hemberger and @moy.

Mechanize is an ancestor of MechanicalSoup (getting its name from the Perl mechanize module). It was a great tool, but became unmaintained for several years and didn’t support Python 3. Fortunately, Mechanize got a new maintainer in 2017 and completed Python 3 support in 2019. Note that Mechanize is a much bigger piece of code (around 20 times more lines!) than MechanicalSoup, which is small because it delegates most of its work to BeautifulSoup and requests. More Information : <a href="https://mechanicalsoup.readthedocs.io/en/stable/">
    Click Here
</a>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all Library for using my index.py

```bash
pip install MechanicalSoup
```

## Usage

```python
python index.py
```

### URL_FORM_LOGIN

- Simply submit the URL of the page where you will enter

<img alt="Aigner" src="https://i.imgur.com/XpYYneI.png" target="_blank" />

- Right-click on the Login Form on the Page then select Inspect Element. If you are confused, you can use a filter with .form or .form-input, and then look for Element Form where there will be an Action Attribute and the value in it is URL_FORM_ACTION.

<img alt="Aigner" src="https://i.imgur.com/MEQX4hm.png" target="_blank" />

- You can change browser["username"] = "YOUR_USERNAME" or browser["password"] = "YOUR_PASSWORD" with your Attribute name and "YOUR_USERNAME" with your Username. To get the Attribute used. You can open the Inspact Element then select Network. Then Filter with "method = POST" to get POST data. Then choose Params. For an example of Screen Shot below:

```
browser["identifier"] = "YOUR_USERNAME"
```
```
browser["password"] = "YOUR_PASSWORD"
```

<img alt="Aigner" src="https://i.imgur.com/aYy5d9O.png" target="_blank" />

- please replace URL_THAT_YOU_WANT_ACCESS with the url of the page you want to retrieve data from. You can use the BeautifulSoup method for Web Data Scraping. Because MechanicalSoup = BeautifulSoup + Request.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Copyright © 2020 [MKRyuto](https://github.com/MKRyuto/).
<br/> This project is [MIT](https://github.com/MKRyuto/Scraping-Data-behind-Site-Logins/blob/master/LICENSE) licensed.
