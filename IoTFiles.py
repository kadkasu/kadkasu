con = serial.Serial(
port='/dev/ttyUSB0',\
baudrate=115200,\
bytesize=serial.EIGHTBITS,\
timeout=0)
print("connected to: "+ con.portstr)
con.write("help\n");
while True:
data = con.readline();
if data:
print(data),
con.close()


if(lollipop_greater_than(dio->version, dag->version)) {
if(dag->rank== ROOT_RANK(instance)) {
dag->version= dio->version;
RPL_LOLLIPOP_INCREMENT(dag->version);
rpl_reset_dio_timer(instance);
} else{
global_repair(from, dag, dio);
}
return;
}


import pickle
pickle.dump(clf,open('models/SVMClassifer.pickle', 'wb'))

#This code will write to the serial link
#the result of the machine learning model
#to the DoS Attacks terget devices.
ser.write(Alert);
while True:
line = ser.readline();
if line:
print(line),
ser.close()


voidsendbodcast(addr) {
printf("Sending broadcast\n");
uip_create_linklocal_allnodes_mcast(&addr);
simple_udp_sendto(&broadcast_connection,"Test",4, &addr);
}



from flask import Flask
from flask_restful importreqparse, abort, Api, Resource
import pickle
app = Flask(__name__)
api = Api(app)
# Creating a SVM model object
model = SVC()
# Load tested and trained model
clf_path= 'models/SVMClassifer.pkl'
with open(clf_path, 'rb') as f:
model.clf= pickle.load(f)
# load model vectorizer
vec_path= 'models/SVMVectorizer.pkl'
with open(vec_path, 'rb') as f:
model.vectorizer= pickle.load(f)


classattackPredetion(Resource):
def get(self):
# use the realtime 6LoWPAN parser
#to get the data
args = parser.6LoWPANData()
# vectorize the user's query and make
#a prediction
vectorized= model.vectorizer_transform(
np.array([args]))
prediction= model.predict(vectorized)
pred_proba= model.predict_proba(vectorized)
# convert result as text
#to be stored in local repository
if prediction == 0:
pred_text= 'Normal'
else:
pred_text= 'Attack'
confidence= round(pred_proba[0],3)
# JSON object to be transfered to IDS agent
output= {'prediction': pred_text,
'confidence': confidence, 'attackerIp': args['ip'}
returnoutput






