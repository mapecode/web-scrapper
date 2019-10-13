from bs4 import BeautifulSoup
import urllib3
import urllib


class Scraper:
    def __init__(self, url):
        self.url = url
        self.http = urllib3.PoolManager()
        self.request = self.connect()

    def connect(self):
        try:
            """ Realiza una peticion http y almacena la respuesta"""
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            r = self.http.request("GET", self.url)
            return r
        except Exception as e:
            print('Se ha producido un error al conectar: \n', e)
            self.url = input("Vuelva a introducir la url \n> ")
            return self.connect()

    def get_element(self, element):
        try:
            """ Devuelve las ocurrencias del elemento que se haya introducido"""
            soup = BeautifulSoup(self.request.data, "html5lib")
            return soup.find_all(element)
        except Exception as e:
            print('Se ha producido un error al obtener el elemento ' + element + ': \n', e)

    def get_images(self):
        try:
            """ Devuelve las urls de las imagenes encontradas en la web """
            soup = BeautifulSoup(self.request.data, "html5lib")
            list_img = []

            for img in soup.find_all('img'):
                if img:
                    list_img.append(img.get('src'))

            return list_img

        except Exception as e:
            print('Se ha producido un error al obtener imagenes: \n', e)

    def get_scripts(self):
        try:
            """ Devuelve los scripts de la url que se introduzca """
            soup = BeautifulSoup(self.request.data, "html5lib")
            list_scripts = []

            for s in soup.find_all('script'):
                if s.get('src'):
                    list_scripts.append(s.get('src'))

            return list_scripts

        except Exception as e:
            print('Se ha producido un error: \n', e)

    def get_links(self):
        try:
            """ Devuelve los links encontrados en la web """
            soup = BeautifulSoup(self.request.data, "html5lib")
            links = soup.find_all('a')

            list_urls = []

            for link in links:
                if link:
                    list_urls.append(link.get('href'))

            return list_urls

        except Exception as e:
            print('Se ha producido un error al obtener enlaces: \n', e)

    @staticmethod
    def download(links, path=''):
        """ Descarga a partir de los enlaces suministrados """
        for link in links:
            try:
                r = urllib.request.urlopen(link)
                file = str(link).split('/')[-1]
                f = open(path+file, "wb")
                f.write(r.read())
                f.close()
                print(file, 'descargado correctamente')

            except Exception as e:
                print('Se ha producido un error al descargar', link, ':\n', e)
