# https://www.tutorialspoint.com/peewee/peewee_field_class.htm
from peewee import *
from datetime import date

db = MySQLDatabase(
    "freedb_test55",
    user="freedb_youssef99",
    password="y6tr!gm?kZ8U6$p",
    host="sql.freedb.tech",
    port=3306,
)


class benzene_price(Model):
    date = DateField()
    solar_price = CharField()
    ben80_price = CharField()
    ben92_price = CharField()
    ben95_price = CharField()

    class Meta:
        database = db


class benzene(Model):
    date = DateField()
    trumba_number = IntegerField()
    trumba_type = CharField()
    start = IntegerField()
    end = IntegerField()
    total = IntegerField()

    class Meta:
        database = db


class oil(Model):
    oil_name = CharField()
    price = CharField()

    class Meta:
        database = db


class oil_storage(Model):
    date = DateField()
    oil_name = CharField()
    start = IntegerField()
    end = IntegerField()
    Treasury_Ward = IntegerField()

    class Meta:
        database = db


class oil_ward(Model):
    date = DateField()
    oil_name = CharField()
    first_term_balance = IntegerField()
    end_term_balance = IntegerField()
    Ward = IntegerField()
    saled = IntegerField()
    price = CharField()
    total = CharField()

    class Meta:
        database = db


class Expenses(Model):
    date = DateField()
    sand = CharField()
    money = IntegerField()

    class Meta:
        database = db


class bons(Model):
    date = DateField()
    benz_type = CharField()
    Side = CharField()
    price = CharField()
    category = IntegerField()
    total = CharField()
    bon_serial = IntegerField()

    class Meta:
        database = db


class matching_bons(Model):
    date = DateField()
    number = IntegerField()
    category = IntegerField()
    benz_type = CharField()
    side = CharField()
    total = CharField()

    class Meta:
        database = db


class client(Model):
    name = CharField()
    national_id = IntegerField()
    mobile_num = IntegerField()

    class Meta:
        database = db


class Term_Clients(Model):
    date = DateField()
    client_name = CharField()
    sand = CharField()
    money = IntegerField()

    class Meta:
        database = db


class daily_treasury(Model):
    date = DateField()
    Quantity = IntegerField()
    price = CharField()
    money = CharField()
    Statement = CharField()

    class Meta:
        database = db


class Supply_Book(Model):
    date = DateField()
    balance = IntegerField()
    ward = IntegerField()
    Expenditure = IntegerField()
    tlomba = IntegerField()
    current_balance = IntegerField()
    Standard = IntegerField()

    class Meta:
        database = db


class Balance_matching(Model):
    date = DateField()
    benz_type = CharField()
    start_balance = IntegerField()
    ward = IntegerField()
    total = IntegerField()
    Expenditure = IntegerField()
    balance_remaining = IntegerField()

    class Meta:
        database = db


class Pump_calibers(Model):
    date = DateField()
    benz_type = CharField()
    Standard = IntegerField()

    class Meta:
        database = db


class Statement(Model):
    name = DateField()
    type_Receivables_or_Payments = CharField()

    class Meta:
        database = db


class Treasury_Movement(Model):
    date = DateField()
    Type = CharField()
    Statement = CharField()
    sand = IntegerField()
    money = IntegerField()

    class Meta:
        database = db


class hsabat(Model):
    date = DateField()
    name = CharField()
    sand = IntegerField()
    money = IntegerField()

    class Meta:
        database = db


class employee(Model):
    name = CharField()
    national_id = IntegerField()
    mobile_num = IntegerField()
    job = CharField()
    salary = IntegerField()

    class Meta:
        database = db


class user_system(Model):
    username = CharField()
    password = CharField()
    user_type = CharField()

    class Meta:
        database = db


class System_Move(Model):
    date = DateField()
    time = IntegerField()
    user_type = CharField()
    username = CharField()
    move = CharField()

    class Meta:
        database = db


class login_h(Model):
    date = DateField()
    time = TimeField(formats=["%H:%M:%S"])
    username = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables(
    [
        benzene_price,
        benzene,
        oil,
        oil_storage,
        oil_ward,
        Expenses,
        bons,
        matching_bons,
        client,
        Term_Clients,
        daily_treasury,
        Supply_Book,
        Balance_matching,
        Pump_calibers,
        Statement,
        Treasury_Movement,
        hsabat,
        employee,
        user_system,
        System_Move,
        login_h,
    ]
)
print("done")
