from django.core.management.base import BaseCommand
from confluent_kafka import Consumer, KafkaException, KafkaError
import json
from home.models import LocationUpdate

class Command(BaseCommand):
    help = "Run Kafka consumer to listen for location updates"

    def handle(self, *args, **options):
        conf = {
            "bootstrap.servers": "localhost:9092",
            "group.id": "location_group",
            "auto.offset.reset": "earliest"
        }
        consumer = Consumer(conf)
        consumer.subscribe(['location_updates'])

        self.stdout.write("Kafka consumer started. Listening for messages...")

        try:
            while True:
                msg = consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        self.stderr.write(f"Consumer error: {msg.error()}")
                        break
                data = json.loads(msg.value().decode('utf-8'))
                LocationUpdate.objects.create(
                    latitude=data['latitude'],
                    longitude=data['longitude']
                )
                self.stdout.write(f"Received and saved: {data}")
        except KeyboardInterrupt:
            self.stdout.write("Kafka consumer interrupted.")
        finally:
            consumer.close()
