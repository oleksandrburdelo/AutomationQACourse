#OLD ONE

#vip = {
#    "table 1": "vip1",
#    "table 2": "vip2",
#    "table 3": "vip3",
#    "table 4": "vip4",
#    "table 5": "vip6",
#}
#
#main_stage = {
#    "ticket 1": "human 1",
#    "ticket 2": "human 2",
#    "ticket 3": "human 3",
#    "ticket 4": "human 4",
#    "ticket5": "human 5",
#    "ticket6": "human 6"
#}

#print(vip)
#print(main_stage)

# Good for main stage but I can add some one in the vip hall.
# Take a look on some another types which provide ability to protect you
# vip hall for mutations.


#NEW ONE

vip_stage = (
    'vip guest 1',
    'vip guest 2',
    'vip guest 3',
    'vip guest 4',
    'vip guest 5',
    'vip guest 6'
)

main_stage = {
    "regular guest 1",
    "regular guest 2",
    "regular guest 3",
    "regular guest 4",
    "regular guest 5",
    "regular guest 6"
}

for vip_guests in vip_stage:
    print(vip_guests)

for regular_guests in main_stage:
    print(regular_guests)
