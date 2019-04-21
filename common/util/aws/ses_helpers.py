import boto3

client = boto3.client('ses')
FROM_EMAIL = ''


# Sending an email
def send_email(to_addresses_list, message_dict, reply_to_addresses_list=[],
               cc_addresses_list=[], bcc_addresses_list=[]):
    Source = FROM_EMAIL
    Destination = {
        'ToAddresses': to_addresses_list,
        'CcAddresses': cc_addresses_list,
        'BccAddresses': bcc_addresses_list,

    }
    Message = message_dict
    ReplyToAddresses = reply_to_addresses_list
    # ReturnPath='',
    # SourceArn='',
    # ReturnPathArn='',
    # Tags=[
    #     {
    #         'Name': 'string',
    #         'Value': 'string'
    #     },
    # ],
    # ConfigurationSetName='string'
    response = client.send_email()
    return response
