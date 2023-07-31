# Relational Database Management Systems

## Role of a RDBMS

A relational database management system (RDBMS) will help you to store,
organise and retrieve data from a database using the relational model.
The roles of a RDBMS include:

1. Storage and organisation
2. Retrieval and manipulation
3. Integrity and security
4. Indexing and optimisation of performance
5. Backup and recovery
6. Scalability

A RDBMS helps user interact with the underlying data storage.

## Independence of data

The way we *use* database or *think* about how the information is organised
does not have to rely on how the data is actually stored and managed.
The RDBMS can show us different views of the database without changing the data
itself, or indeed change the organisation of the data while maintaining a
consistent view of the data. The abstraction of these layers between the user,
the RDBMS and the physical storage of the data is known as **data independence**.

**Data independence** means that the views users have of a databasse do
not rely on the logical structure
and physical storage of the data itself. 

```{image} ../../images/db/db-layers.png
:alt: Triple layers of RDBMS.
:class: bg-primary mb-1
:width: 600px
:align: center
```
### Physical data independence

The physical storage of data is managed on a level below the RDBMS.
The location, compression or structure of the data can change while keeping the
view of the user consistent. Indexes can update, data blocks can be rewritten,
the format of the data itself can change without causing an impact on the use
and operation of the database.

### Logical data independence

The way data is organised within a database does not have to influence
the way the information is accessed by external users or services. The use of
internal views and stored queries means that external users of the database
like APIs and other programs can continue to use existing services even when
the underlying database schema changes, though care to manage this process is
often required. 





"
SQLite source code is in the public-domain and is free to everyone to use for any purpose.
"

## Sources

- https://www.sqlite.org/index.html
- https://www.guru99.com/dbms-data-independence.html

