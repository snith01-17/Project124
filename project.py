from flask import Flask,jsonify, request

app = Flask(__name__)

list1=[
    {
        "data":[
            {
                "Contact": "9987644456",
                "Name": "Raju",
                "done":False,
                "id":1
            },
            {
                "Contact": "987654543",
                "Name": "Rahul",
                "done":False,
                "id":2
            }
        ]
    }
]

@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        },400)
    contact = {
        'id':list1[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done': False
    }    
    list1.append(contact)
    return jsonify({
            "status": "Successful!",
            "message": "Contact added successfully!"
        })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : list1
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)