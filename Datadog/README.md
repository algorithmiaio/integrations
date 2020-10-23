# Algorithmia + Datadog

## Overview

Algorithmia Insights is a feature of Algorithmia Enterprise and provides a
metrics pipeline that can be used to instrument, measure, and monitor your
machine learning models. Use cases for monitoring inference-related metrics from
machine learning models include detecting model drift, data drift, model bias,
etc.

Datadog is a cloud-based monitoring service that aggregates metrics and logs
across different services. You can send Insights from Algorithmia to Datadog as
time-series data that can then be analyzed in dashboards, monitors, and alerts.

This integration allows you to stream operational metrics as well as
user-defined, inference-related metrics from Algorithmia to Kafka to the metrics
API in Datadog.

## Using this Algorithmia + Datadog integration

1. Install Python.

2. Clone this repository:

   ```
   git clone https://github.com/algorithmiaio/integrations.git
   ```

3. Navigate to the directory with the Datadog integration:

   ```
   cd integrations/Datadog
   ```

4. Install the required Python dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

5. Define the following environment variables (required):

   ```
   export DATADOG_API_KEY=<DATADOG-API-KEY>
   export KAFKA_BROKER=1.2.3.4:9092
   export KAFKA_TOPIC=insights
   ```

   and replace the values with your Datadog API key, Kafka broker URL and port,
   and Kafka topic that you want to consume Insights from.

6. Run the Python script provided in this repository, which will continuously
   forward messages from Kafka to the Datadog metrics API:

   ```
   python kafka-datadog.py
   ```

   you can also run the Python script in the background using:

   ```
   python kafka-datadog.py &
   ```

   or use a process supervision tool such as
   [supervisord](http://supervisord.org/) to manage the log forwarding service
   and handle starting, stopping, and restarting the service.

## Additional resources

Refer to the documentation at
https://github.com/DataDog/integrations-extras/algorithmia for more information
about this integration, including sample dashboards and monitors.
