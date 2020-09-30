from flask import Flask, request, render_template
import reading
app=Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
@app.route('/',methods=["POST","GET"])
def home():
    if request.method =="POST":
        #Read data from json
        transaction_date =float(request.json['array'][0])
        house_age =float(request.json['array'][1])
        distance_to_the_nearest_MRT_station =float(request.json['array'][2])
        number_of_convenience_stores =float(request.json['array'][3])
        latitude =float(request.json['array'][4])
        longitude =float(request.json['array'][5])
        data=[transaction_date,house_age,distance_to_the_nearest_MRT_station,number_of_convenience_stores,latitude,longitude]
        #Find the house price value for unit space
        house_price_of_unit_area = reading.Values(data)
        print(house_price_of_unit_area)
        return str(house_price_of_unit_area)
    elif request.method =="GET" :
        return "Data must be submitted"
if __name__ == '__main__':
    app.run(port=app.config["PORT"],debug=app.config["DEBUG"])
