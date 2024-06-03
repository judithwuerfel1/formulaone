import boto3
import pandas as pd

from helpers import get_dynamo_resource, get_items_from_table

import configparser


config = configparser.ConfigParser()
config.read("config.ini")

session = boto3.Session(
    aws_access_key_id = config["DEFAULT"]["aws_access_key_id"],
    aws_secret_access_key = config["DEFAULT"]["aws_secret_access_key"]
)

tables = get_dynamo_resource(session)
get_items_from_table(2013, session)

