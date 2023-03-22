df = spark.sql("select * from samples.nyctaxi.trips limit 10")
df.show()