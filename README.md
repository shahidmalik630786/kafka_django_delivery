<h3>Step 1: Create a Docker Compose File</h3>

<p>Run>  docker-compose up -d</p>

<h3>Step 3: Verify Kafka Container is Running</h3>

<p>Run>  docker ps</p>

<h3>Step 4: </h3>
<p>python kafka_producer.py</p>
<p>Run> python manage.py kafka_consumer</p>

<h3>Step 5: </h3>

<p>Cntrl+c and run python manage.py runserver</p>

<h3>Explanantion:-</h3>

<p>
Here we have designed a producer which produces data as a delivery boy location movement and designed a kafka consumer which consumes the data and show cases on google map in index.html
</p>

