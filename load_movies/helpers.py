from boto3.dynamodb.conditions import Key

def get_items_from_table(year, session):
    """Returns titles of all movies from a given year.

    Args:
        :param year: year
        :param session: boto3 session
    """
    dynamo_resource = session.resource("dynamodb", region_name="eu-west-1")
    films = dynamo_resource.Table("doc-example-table-movies").query(
        KeyConditionExpression=Key("year").eq(year)
    )
    for film in films["Items"]:
        titles = film["title"]
    return titles

def get_dynamo_resource(session):
    """Creates a list of tables from dynamodb.
    
    Args:
        :param session: boto3 session
    """
    dynamo_resource = session.resource(
        'dynamodb',
        region_name='eu-west-1'
    )

    tables = []
    for table in dynamo_resource.tables.all():
        tables.append(table)

    return tables
