# JKForum.nwt Downloader
import func
import re
def main(url):
    soup = func.get_url(url)
    folder = soup.find('h1')
    if folder is not None:
        func.make_folder(folder.text)
    func.write_source_url(url)
    image_count = None
    for image_count, image_link in enumerate(soup.find_all(zoomfile=re.compile('.+mymypic.net.+')), 1):
       open('imglink.txt', 'a+').write(image_link['zoomfile'] + '\n' + '  out=' + str(image_count) + '.jpg\n')
