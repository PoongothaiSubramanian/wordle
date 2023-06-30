s = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""
status_codes_exceptions = """Delivery Attempted - No Access to Delivery Location
Reminder to Schedule Redelivery of your item
Forwarded
Delivery Attempted - No Access to Delivery Location
Forward Processed
No Such Number
Addressee Unknown
Delivery Exception, Local Weather Delay
Insufficient Address
Held at Post Office, At Customer Request
Notice Left (No Secure Location Available)
Processing Exception, Other Delay
Processing Exception
Available for Redelivery or Pickup
Redelivery Scheduled
Held at Post Office, At Customer Request
Rescheduled to Next Delivery Day
Return to Sender
Delivery Exception, Animal Interference
Notice Left (Receptacle Full/Item Oversized)
Return to Sender
Refused
Vacant
Unclaimed/Being Returned to Sender
Notice Left (No Authorized Recipient Available)
Return to Sender Processed
Delivered, To Original Sender
Forward Expired
Moved, Left no Address
Disposed by Post Office
Delivered to original"""
WORDLE = 'bench'
def string_split(status_description):
    msg_list = status_description.split('\n')
    print(len(msg_list))
    return msg_list