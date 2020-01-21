from flask import Flask, render_template
import http.client
import requests
import logging
#from package.myapp.controllers import mycontroller
#import package.myapp.controllers.mycontroller
import src.package.myapp.controllers.mycontroller as test

app = Flask(__name__)

@app.route('/')
def index():
    test.con1()
    # logging.info("index page")
    # logging.error("something wrong")
    # print("print log test")

    res = requests.get('https://hotplace.kicc.co.kr/inf/listhead/ListMainAction.do?user_id=&biz_top_cd=1&biz_med_cd=110&latitude=37.5605768&longitude=126.9736564&time_gubun=0&language_gubun=1&area_yn=N&distance=100&area_gb=1&area_id=&sch_gb=2&hotservice_yn=A&hotmenu_yn=&stmp_yn=&trs_yn=&aos_yn=&deal_yn=&money_yn=')
    data = res.json()
    print(data)


    return test.con1()

@app.route('/test')
def testpage():
    return render_template('mypage.html')

if __name__ == "__main__":
   app.run()