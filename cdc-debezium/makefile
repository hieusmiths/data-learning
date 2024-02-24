connect-debezim-sql:
	curl -X POST --location "http://localhost:8083/connectors" -H "Content-Type: application/json" -H "Accept: application/json" -d @debezium.json
delete-debezium-connector:
	curl -i -X DELETE localhost:8083/connectors/sample-connector/
kafka-listen-all:
	kafka-console-consumer --bootstrap-server localhost:9092 --whitelist '.*' --property print.key=true --from-beginning
insert-balance:
	insert into balance(name) values('S1');