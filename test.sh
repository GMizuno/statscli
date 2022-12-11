stats head --path  tests/KwhConsumptionBlower78_1.parquet
stats head --path  tests/KwhConsumptionBlower78_1.csv

stats describer --path  tests/KwhConsumptionBlower78_1.parquet
stats describer --path  tests/KwhConsumptionBlower78_1.csv

stats list-files --path tests

stats to-parquet --path tests/KwhConsumptionBlower78_1.csv --new-filename tests/teste_parquet.parquet
stats to-csv --path tests/obt.parquet
stats to-avro --path tests/obt.parquet 
