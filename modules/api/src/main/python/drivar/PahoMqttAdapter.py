import paho.mqtt.client as mqtt

class PahoMqttAdapter:
    
  
  """Translates MQTT calls into Drivar calls"""
  def on_connect(client, userdata, flags, rc):
      print("Connected with result code "+str(rc))
      # Subscribing in on_connect() means that if we lose the connection and
      # reconnect then subscriptions will be renewed.
      client.subscribe("$SYS/#")
  
  # The callback for when a PUBLISH message is received from the server.
  def on_message(client, userdata, msg):
      #print(msg.topic+" "+str(msg.payload))
      
      # Convert the topic to a method call
      topics  = msg.topic[self.topicRootLen:].split("/")
      
      
      
      # Unwrap the payload to convert to parameters
  
  def on_disconnect():
  
  def init(self, drivar, host, topicRoot, port=1883):
     self.drivar = drivar
     self.client = mqtt.Client()
     self.client.reconnect_delay_set()
     self.client.on_connect = self.on_connect
     self.client.on_message = self.on_message
     
     self.client.connect(host, port, 60)
     self.topicRoot = topicRoot
     
     if not self.topicRoot.endsWith("/"):
         self.topicRoot += "/"
     self.topicRoot += "command/"
     self.topicRootLen = len(self.topicRoot)
     # Subscribe to commands
     self.client.subscribe(self.topicRoot+"#")
      

  def start(self):
      self.client.loop_start()
      
  def stop(self):
      self.client.loop_stop()