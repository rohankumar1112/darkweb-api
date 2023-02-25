try:
    from flask import Flask, jsonify, request
    import time
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    import time
    import pandas as pd
except Exception as e:
    print("Some Modules are Missing :{}".format(e))

app = Flask(__name__)

def databaseConnection():
   CONNECTION_STRING = "mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority"
   client = MongoClient(CONNECTION_STRING)
   return client['darkWebAutomation']
db = databaseConnection()
collection = db["websiteXPATH"]

dict =[]

@app.route('/')
def fetch():
    result =[]
    data =collection.find()
    for d in data:
        id =str(d['_id'])
        name =d['name']
        darkweb_url =d['darkweb_url'] 
        iterator=d['iterator']
        title_xpath=d['title_xpath']
        body_xpath=d['body_xpath']
        date_xpath=d['date_xpath']
        scrollable=d['scrollable']
        pagination = d['pagination']
        is_nextbtn=d['is_nextbtn']
        xpath_of_next_btn=d['xpath_of_next_btn']
        xpath_of_pagination_container=d['xpath_of_pagination_container']
        tag_name_of_pages=d['tag_name_of_pages']
        failed_count =d['failedCount']
        clickable =d['clickable']
        clickable_btn_xpath =d['clickable_btn_xpath']
        waitTime =d['waitTime']
        status =d['status']
        isSPA =d['isSPA']
        time =d['time']
        isUrgent =d['isUrgent']
      
        result.append({'id':id,'name':name,'darkweb_url':darkweb_url,'iterator':iterator,'title_xpath':title_xpath,'body_xpath':body_xpath,'date_xpath':date_xpath,'scrollable':scrollable,'pagination':pagination,'is_nextbtn':is_nextbtn,'xpath_of_next_btn':xpath_of_next_btn,'xpath_of_pagination_container':xpath_of_pagination_container,'tag_name_of_pages':tag_name_of_pages,'failedCount':failed_count,'clickable':clickable,'clickable_btn_xpath':clickable_btn_xpath,'waitTime':waitTime,'status':status,'isSPA':isSPA,'time':time,'isUrgent':isUrgent})
    return jsonify(result)


@app.route('/darkWebsite/<id>', methods=['GET','DELETE','PUT'])
def website(id):
    if request.method=='GET':
        try:
            data =collection.find_one({'_id':ObjectId(id)})
            name =data['name']
            darkweb_url =data['darkweb_url'] 
            iterator=data['iterator']
            title_xpath=data['title_xpath']
            body_xpath=data['body_xpath']
            date_xpath=data['date_xpath']
            scrollable=data['scrollable']
            pagination = data['pagination']
            is_nextbtn=data['is_nextbtn']
            xpath_of_next_btn=data['xpath_of_next_btn']
            xpath_of_pagination_container=data['xpath_of_pagination_container']
            tag_name_of_pages=data['tag_name_of_pages']
            failed_count =data['failedCount']
            clickable =data['clickable']
            clickable_btn_xpath =data['clickable_btn_xpath']
            waitTime =data['waitTime']
            status =data['status']
            isSPA =data['isSPA']
            time =data['time']
            isUrgent =data['isUrgent']
            result =[]
            result=({'_id':id,'name':name,'darkweb_url':darkweb_url,'iterator':iterator,'title_xpath':title_xpath,'body_xpath':body_xpath,'date_xpath':date_xpath,'scrollable':scrollable,'pagination':pagination,'is_nextbtn':is_nextbtn,'xpath_of_next_btn':xpath_of_next_btn,'xpath_of_pagination_container':xpath_of_pagination_container,'tag_name_of_pages':tag_name_of_pages,'failedCount':failed_count,'clickable':clickable,'clickable_btn_xpath':clickable_btn_xpath,'waitTime':waitTime,'status':status,'isSPA':isSPA,'time':time,'isUrgent':isUrgent})
            return result
        except:
            resp = jsonify("No Content")
            resp.status_code = 204
            return resp

    if request.method=='DELETE':
        data = collection.find()
        for d in data:
            if d['_id'] == ObjectId(id):
                query = {"_id": ObjectId(id)}
                collection.delete_one(query)
                resp = jsonify("Field Deleted")
                resp.status_code = 410
                return resp
        resp = jsonify("Already Deleted")
        resp.status_code = 210
        return resp

    if request.method =='PUT':
        _name =request.json['name']
        _darkweb_url =request.json['darkweb_url'] 
        _iterator=request.json['iterator']
        _title_xpath=request.json['title_xpath']
        _body_xpath=request.json['body_xpath']
        _date_xpath=request.json['date_xpath']
        _scrollable=request.json['scrollable']
        _pagination = request.json['pagination']
        _is_nextbtn=request.json['is_nextbtn']
        _xpath_of_next_btn=request.json['xpath_of_next_btn']
        _xpath_of_pagination_container=request.json['xpath_of_pagination_container']
        _tag_name_of_pages=request.json['tag_name_of_pages']
        _failed_count =request.json['failedCount']
        _clickable =request.json['clickable']
        _clickable_btn_xpath =request.json['clickable_btn_xpath']
        _waitTime =request.json['waitTime']
        _status =request.json['status']
        _isSPA =request.json['isSPA']
        _time =request.json['time']
        _isUrgent =request.json['isUrgent']
        
        
        data = collection.find()
        for d in data:
            if d['_id'] == ObjectId(id):
                if(len(str(_name))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"name":_name}})
                if(len(str(_darkweb_url))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"darkweb_url":_darkweb_url}})
                if(len(str(_iterator))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"iterator":_iterator}})
                if(len(str(_title_xpath))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"title_xpath":_title_xpath}})
                if(len(str(_body_xpath))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"body_xpath":_body_xpath}})
                if(len(str(_date_xpath))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"date_xpath":_date_xpath}})
                if(len(str(_scrollable))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"scrollable":_scrollable}})
                if(len(str(_pagination))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"pagination":_pagination}})
                if(len(str(_is_nextbtn))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"is_nextbtn":_is_nextbtn}})
                if(len(str(_xpath_of_next_btn))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"xpath_of_next_btn":_xpath_of_next_btn}})
                if(len(str(_xpath_of_pagination_container))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"xpath_of_pagination_container":_xpath_of_pagination_container}})
                if(len(str(_tag_name_of_pages))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"tag_name_of_pages":_tag_name_of_pages}})
                if(len(str(_failed_count))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"failedCount":_failed_count}})
                if(len(str(_clickable))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"clickable":_clickable}})
                if(len(str(_clickable_btn_xpath))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"clickable_btn_xpath":_clickable_btn_xpath}})
                if(len(str(_waitTime))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"waitTime":_waitTime}})
                if(len(str(_status))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"status":_status}})
                if(len(str(_isSPA))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"isSPA":_isSPA}})
                if(len(str(_time))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"time":_time}})
                if(len(str(_isUrgent))>0):
                    collection.update_one({"_id":d['_id']},{"$set":{"isUrgent":_isUrgent}})
                        
                resp = jsonify("User updated")
                resp.status_code = 200
                return resp

@app.route('/darkWebsite', methods=['POST'])
def post():
    name =request.json['name']
    darkweb_url =request.json['darkweb_url'] 
    iterator=request.json['iterator']
    title_xpath=request.json['title_xpath']
    body_xpath=request.json['body_xpath']
    date_xpath=request.json['date_xpath']
    scrollable=request.json['scrollable']
    pagination = request.json['pagination']
    is_nextbtn=request.json['is_nextbtn']
    xpath_of_next_btn=request.json['xpath_of_next_btn']
    xpath_of_pagination_container=request.json['xpath_of_pagination_container']
    tag_name_of_pages=request.json['tag_name_of_pages']
    failed_count =request.json['failedCount']
    clickable =request.json['clickable']
    clickable_btn_xpath =request.json['clickable_btn_xpath']
    waitTime =request.json['waitTime']
    status =request.json['status']
    isSPA =request.json['isSPA']
    time =request.json['time']
    isUrgent =request.json['isUrgent']
    data = collection.find()
    if collection.count_documents({'darkweb_url':darkweb_url})>0:
        return jsonify("url Already exist.. Update the field if you need")
    if request.method == "POST":
        id = collection.insert_one({'name':name,'darkweb_url':darkweb_url,'iterator':iterator,'title_xpath':title_xpath,'body_xpath':body_xpath,'date_xpath':date_xpath,'scrollable':scrollable,'pagination':pagination,'is_nextbtn':is_nextbtn,'xpath_of_next_btn':xpath_of_next_btn,'xpath_of_pagination_container':xpath_of_pagination_container,'tag_name_of_pages':tag_name_of_pages,'failedCount':failed_count,'clickable':clickable,'clickable_btn_xpath':clickable_btn_xpath,'waitTime':waitTime,'status':status,'isSPA':isSPA,'time':time,'isUrgent':isUrgent})
        resp = jsonify("User added successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()
    
@app.errorhandler(404)
def not_found(error = None):
    message = {
        'status': 404,
        'message' : 'Not Found' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp    

if __name__=='__main__':
    app.run(debug=True)