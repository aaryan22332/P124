from flask import Flask,jsonify,request


app = Flask(__name__)
tasks = [
    {
        "Contact":"8605860650",
        "Name":"Aaryan",
        "done":"False",
        "id":1
            },
            {
        "Contact":"9922955755",
        "Name":"Ramkumar",
        "done":"False",
        "id":2
            }
]
@app.route("/add-data",methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['name'],
        'description':request.json.get('contact',''),
        'done':False
    }
    tasks.append(task)    
    return jsonify({
            "status":"success",
            "message":"task added successfully"
        })


@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)        