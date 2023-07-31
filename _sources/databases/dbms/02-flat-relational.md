(content:databases:flat)=
# Flat File vs Relational Database

A **flat file** is a single table database.

Usually, each column has a heading which describes the content of the column.
Each row represents a single thing or entity which has a number of data or
fields, associated with it.

```{image} ../../images/db/flat-file-02.png
:alt: flat table of data
:class: bg-primary mb-1
:width: 600px
:align: center
```

A **relational database** has many tables that are linked using relationships.

Similarly, each column of a relational database usually represents an attribute
like name or age, while each row represents a record of one entity or object.
The difference between many flat-files and a relational database is that there
are links between tables in a relational database.

These links try to keep the information in the database correct and consistent,
for example by stopping or warning of the deletion of related data.
