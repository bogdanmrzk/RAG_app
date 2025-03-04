# RAG_app

RAG chat API about Django Framework

## What is rag app  created for

This is DRF API chat, built to answer simple questions
about Django Framework

## Question samples

> request
`POST /apiv1/chat/ask`

`curl -X POST -H 'Content-Type: application/json' -d '{"question":"tell me about django ORM"}' localhost:8000/apiv1/chat/ask/`

> response
`Based on the provided data, I am unable to provide detailed information about Django ORM (Object-Relational Mapper). However, here is a brief overview of what the Django ORM does:

1. The Django ORM simplifies the handling of databases by providing an easy-to-use Pythonic API for querying and updating database tables. It allows developers to interact with databases using object-oriented methods instead of writing raw SQL queries.

2. Models in Django define the structure of database tables, including their fields and relationships with other models.

3. The ORM automatically maps these models to corresponding database tables when a model is saved, and vice versa when loading data from the database.

4. The ORM provides various query methods for filtering, sorting, and aggregating data in the database. Some examples include `filter()`, `exclude()`, `order_by()`, `count()`, etc.

5. It also supports more complex queries using QuerySets, which can be further filtered or annotated using various methods.

6. Django ORM supports relationships between models, such as OneToOneField, ForeignKey, ManyToManyField, and GenericForeignKey. These relationships make it easy to establish connections between different parts of your data model.

7. Transactions are automatically managed by the ORM, ensuring data consistency when saving multiple records at once.

For more detailed information about Django ORM, you can refer to the official Django documentation: https://docs.djangoproject.com/en/4.1/topics/db/queries/`

