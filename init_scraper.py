import modules.scraper as s


def print_element(scraper, element):
    for e in scraper.get_element(element):
        print(e)
    print()


def print_urls(scraper):
    for url in scraper.get_links():
        print(url)
    print()


def print_images(scraper):
    for img in scraper.get_images():
        print(img)
    print()


def print_scripts(scraper):
    for script in scraper.get_scripts():
        print(script)
    print()


def download_images(scraper):
    scraper.download(scraper.get_images(), path='downloads/')


if __name__ == '__main__':
    sc = s.Scraper(input('Introduzca la url de la web \n> '))

    print_element(sc, 'h2')
    print_urls(sc)
    print_images(sc)
    print_scripts(sc)
    download_images(sc)


