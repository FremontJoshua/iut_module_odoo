import csv
import erppeek

url = 'http://localhost:8071'
db = 'odoo'
user = 'admin'
pwd = 'azerty&1785'

client = erppeek.Client(url, db=db, user=user, password=pwd)

with open('devices.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sn = row['serial_number']
        dateA = row['date_allocation']
        dateP = row['date_purchase']
        model = row['model']
        brand = row['brand']
        type = row['type']
        employee = row['employee']

        idBrand = client.search('iut.it.brand', [('name','=',brand)])
        if not idBrand:
            if brand:
                idBrand = client.create('iut.it.brand', {'name': brand, 'warranty_delay_month': 6, 'support_phone': '0202020202'})
            else:
                idBrand = False
        else:
            idBrand = idBrand[0]

        idModel = client.search('iut.it.model', [('name', '=', model)])
        if not idModel:
            if model:
                idModel = client.create('iut.it.model', {'name': model, 'ref': model, 'brand_id': idBrand})
            else:
                idModel = False
        else:
            idModel = idModel[0]

        idType = client.search('iut.model.type', [('name', '=', type)])
        if not idType:
            if type:
                idType = client.create('iut.model.type', {'name': type, 'type_ids': [(4, idModel)]})
            else:
                idType = False
        else:
            idType = idType[0]

        idEmployee = client.search('res.partner', [('name', '=', employee)])
        if not idEmployee:
            if employee:
                idEmployee = client.create('res.partner', {'name': employee})
            else:
                idEmployee = False
        else:
            idEmployee = idEmployee[0]

        try:
            client.create('iut.it.device', {'name': brand+' '+model+'-'+sn, 'serial_number': sn, 'date_allocation': dateA, 'date_purchase': dateP, 'model_id': idModel,
                                            'partner_id': idEmployee})
        except Exception as e:
            print(e)
