MODEL/DB

### LISTINGS
id:INT
realtor:INT(FOREIGN KEY[realtor])
title:STR
address:STR
city:STR
zipcode:STR
des:TEXT
price:INT
bedrooms:INT
bathroom:INT
garage:INT[0]
sqft:INT
lot_size:FLOAT
is_published:BOOL[true]
list_date:DATE
phto_main:STR
photo_1:STR
photo_2:STR
photo_3:STR
photo_4:STR
photo_5:STR
photo_6:STR

### REALTOR
id:INT
name:STR
photo:STR
des:TEXT
email:STR
phone:STR
is_mvp:BOOL[0]
is_hired:DATE

### CONTACT
id:INT
listing:INT
listing_id:INT
name:STR
email:STR
phone:STR
message:TEXT
contact_date:DATE

