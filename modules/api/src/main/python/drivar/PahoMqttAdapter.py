import paho.mqtt.client as mqtt
import json
import logging


class PahoMqttAdapter:
    """Translates incoming MQTT calls into local Drivar calls"""
    
    def __init__(self, drivar, topicRoot="scene/robot/drivar/", host="localhost", port=1883):
        self.logger = logging.getLogger(__name__)
        self.drivar = drivar
        self.client = mqtt.Client()
        self.client.reconnect_delay_set()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
     
        self.client.connect(host, port, 60)
        self.topicRoot = topicRoot
     
        if not self.topicRoot.endswith("/"):
            self.topicRoot += "/"
        self.commandTopicRoot = self.topicRoot+"command/"
        self.commandTopicRootLen = len(self.commandTopicRoot)
  

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        #
        # Subscribe to commands
        self.client.subscribe(self.topicRoot + "#")
  
  # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        # Convert the topic to a method call
        topics = msg.topic[self.commandTopicRootLen:].split("/")
        methodName = topics[0] + "_" + topics[1]
        methodToCall = getattr(self.drivar, methodName, None)
        if(methodToCall is None):
            self.logger.error("Method " + methodToCall + " is not available on the Drivar instance provided")
        # Unwrap the payload to convert to parameters
        parameters = {}
        strPayload = msg.payload.decode('utf-8')
        if not (len(strPayload.strip()) == 0):
            try:
                parameters = json.loads(strPayload)
            except:
                self.logger.error("Could not unpack parameters in  " + strPayload)
        
        # Queue the method call for async processing
        self.logger.info("Calling 'drivar." + methodName + "' (with params " + json.dumps(parameters) + ")")
        methodToCall(**parameters)
  
    def on_disconnect(self):
        self.logger.info("MQTT client adapter now disconnected")
    
    def start(self):
        self.client.loop_start()
      
    def stop(self):
        self.client.loop_stop()
