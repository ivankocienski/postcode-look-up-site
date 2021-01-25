create table stores 
    (id serial primary key, 
     name varchar not null, 
     postcode varchar not null, 
     latitude float default 0, 
     longitude float default 0);