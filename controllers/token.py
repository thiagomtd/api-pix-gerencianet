from server.instance import server
from services.pix import PixService

api = server.api


@api.route('/token', methods=['POST'])
class Token():

    def post(self, ):
        pix_service = PixService()
        response = pix_service.get_token()
        return response
