# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "5ab80750-cf27-4cea-ab2b-eedd93c0cabb",
# META       "default_lakehouse_name": "test_bronze_lakehouse",
# META       "default_lakehouse_workspace_id": "51b570f4-61bc-4a54-9281-3b8bc0c23af8",
# META       "known_lakehouses": [
# META         {
# META           "id": "5ab80750-cf27-4cea-ab2b-eedd93c0cabb"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE SCHEMA IF NOT EXISTS test_bronze_lakehouse.customer;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE IF NOT EXISTS test_bronze_lakehouse.customer.customers (
# MAGIC     customer_id int,
# MAGIC     first_name STRING,
# MAGIC     last_name STRING,
# MAGIC     email STRING,
# MAGIC     date_created TIMESTAMP
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
