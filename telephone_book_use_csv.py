import csv


class UseCSV:
    def __init__(self):
        self.csv_file = 'book_in_csv.csv'

    def get_contacts(self):
        resp_dict = {}
        with open(self.csv_file) as f:
            reader = csv.reader(f)
            for i in reader:
                resp_dict[i[0]] = i[1]
        if 'Name' in resp_dict:
            del resp_dict['Name']
        return resp_dict

    def write_phone_book(self, contacts_in_csv):
        with open(self.csv_file, 'w') as csv_file:
            w = csv.DictWriter(csv_file, fieldnames=['Name', 'Phone number'])
            w.writeheader()
            fields_dict = {}
            for k, v in contacts_in_csv.items():
                fields_dict['Name'] = k
                fields_dict['PhoneNumber'] = v
                w.writerow(fields_dict)
