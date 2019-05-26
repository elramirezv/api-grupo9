from .utils import hashQuery
from bodega.constants.logic_constants import headers, almacen_stock, minimum_stock, prom_request, DELTA, sku_products, REQUEST_FACTOR
from bodega.constants.config import ocURL, almacenes
import requests
import json
import xml.etree.ElementTree as ET
import pysftp


def deleteOc(ocId, reason):
    body = {"anulacion": reason}
    response = requests.delete(
        ocURL + "anular/{}".format(ocId), headers=headers, json=body)
    return response.json()


def newOc(clientId, vendorId, sku, delivery_date, quantity, unitPrice, channel, notes="Default note", notURL="https://tuerca9.ing.puc.cl"):
    body = {
        "cliente": clientId,
        "proveedor": vendorId,
        "sku": sku,
        "fechaEntrega": delivery_date,
        "cantidad": quantity,
        "precioUnitario": unitPrice,
        "canal": channel,
        "notas": notes,
        "urlNotificacion": args[1]
    }
    response = requests.put(ocURL + "crear", headers=headers, json=body)
    return response.json()


def getOc(ocId):
    response = requests.get(ocURL + "obtener/{}".format(ocId), headers=headers)
    return response.json()


def receiveOc(ocId):
    body = {"_id": ocId}
    response = requests.post(
        ocURL + "recepcionar/{}".format(ocId), headers=headers)
    return response.json()

    
def declineOc(ocId, reason):
    body = {"rechazo": reason}
    response = requests.post(ocURL + "rechazar/{}".format(ocId), headers=headers, json=body)
    return response.json()


if __name__ == '__main__':
    watch_server()
