import falcon
from zipfile import ZipFile
import mimetypes



class DownloadPdfResource:

    def on_get(self, req, resp):
        filename="./book.pdf"
        resp.downloadable_as = filename
        resp.content_type = 'application/pdf'

        resp.stream= open(filename, 'rb')
        resp.status = falcon.HTTP_200


class DownloadXlsResource:

    def on_get(self, req, resp):
        filename="./arquivo.xlsx"
        resp.downloadable_as = filename
        resp.content_type = 'application/excel'

        resp.stream= open(filename, 'rb')
        resp.status = falcon.HTTP_200


class DownloadZipResource:

    def on_get(self, req, resp):
        # create a ZipFile object
        zipObj = ZipFile('/app/src/sample.zip', 'w')
        # Add multiple files to the zip
        zipObj.write('/app/src/arquivo.xlsx')
        zipObj.write('/app/src/book.pdf')
        # close the Zip File
        zipObj.close()  
        filename="./sample.zip"
        resp.downloadable_as = filename
        resp.content_type = mimetypes.types_map['.zip']


        resp.stream= open(filename, 'rb')
        resp.status = falcon.HTTP_200


api = falcon.API()
api.add_route('/downloadpdf', DownloadPdfResource())
api.add_route('/downloadxls', DownloadXlsResource())
api.add_route('/downloadzip', DownloadZipResource())


