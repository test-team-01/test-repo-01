import json
from datetime import datetime
from flask import Flask, request, make_response
from slack_sdk import WebClient
import pandas as pd

token = "user api"
app = Flask(__name__, static_url_path='/static')
client = WebClient(token)



def ALl_Top():
    df = pd.read_csv('/home/oh/Documents/amr_ws/OpenCV/02.slack/f12.csv')
    df.drop(['Unnamed: 0'], axis=1 , inplace=True)
    오메 = df.loc[df['오메점수'] >= 12.0].sort_values("오메점수", ascending=False)
    오메 = 오메.loc[:, ['이름', '링크', '오메점수' ]]
    오메 = 오메.reset_index(drop=True)
    choose = 오메.sample(n=1,axis=0)

    name_x = choose['이름']
    name_x = name_x.to_string()
    resultName = name_x[5:]

    score_x = choose['오메점수']
    score_x = score_x.to_string()
    resultScore = score_x[5:]

    path_x = choose['링크']
    path_x = path_x.to_string()
    path_x = path_x[5:]

    
    return "이름 : " + resultName + '\n' + '\n' + " 점수 : " + resultScore+ ":sparkles:" + "\n\n " + path_x



def Korea_menu():
    df = pd.read_csv('/home/oh/Documents/amr_ws/OpenCV/02.slack/f12.csv')
    df.drop(['Unnamed: 0'], axis=1 , inplace=True)
    한식 = df.loc[df['분류'] == '한식'].sort_values("오메점수", ascending=False).head(113)
    한식 = 한식.loc[:, ['이름', '링크', '오메점수' ]]

    한식 = 한식.reset_index(drop=True)
    choose = 한식.sample(n=1,axis=0)
    
    name_x = choose['이름']
    name_x = name_x.to_string()
    resultName = name_x[6:]

    score_x = choose['오메점수']
    score_x = score_x.to_string()
    resultScore = score_x[6:]

    path_x = choose['링크']
    path_x = path_x.to_string()
    path_x = path_x[6:]

    
    return "이름 : " + resultName + '\n' + '\n' + " 점수 : " + resultScore+ ":sparkles:" + "\n\n " + path_x


def china_menu():
    df = pd.read_csv('/home/oh/Documents/amr_ws/OpenCV/02.slack/f12.csv')
    df.drop(['Unnamed: 0'], axis=1 , inplace=True)
    중식 = df.loc[df['분류'] == '중식'].sort_values("오메점수", ascending=False).head(20)
    중식 = 중식.loc[:, ['이름', '링크', '오메점수' ]]

    중식 = 중식.reset_index(drop=True)
    choose = 중식.sample(n=1,axis=0)
    # choose = choose.drop('Unnamed: 0', axis=1, inplace=True)
    
    name_x = choose['이름']
    name_x = name_x.to_string()
    resultName = name_x[5:]

    score_x = choose['오메점수']
    score_x = score_x.to_string()
    resultScore = score_x[5:]

    
    path_x = choose['링크']
    path_x = path_x.to_string()
    path_x = path_x[6:]

    
    return "이름 : " + resultName + '\n' + '\n' + " 점수 : " + resultScore+ ":sparkles:" + "\n\n " + path_x

def japan_menu():
    df = pd.read_csv('/home/oh/Documents/amr_ws/OpenCV/02.slack/f12.csv')
    df.drop(['Unnamed: 0'], axis=1 , inplace=True)
    일식  = df.loc[df['분류'] == '일식'].sort_values("오메점수", ascending=False).head(19)
    일식 = 일식.loc[:, ['이름', '링크', '오메점수' ]]

    일식 = 일식.reset_index(drop=True)
    choose = 일식.sample(n=1,axis=0)
    # choose = choose.drop('Unnamed: 0', axis=1, inplace=True)
    
    name_x = choose['이름']
    name_x = name_x.to_string()
    resultName = name_x[5:]

    score_x = choose['오메점수']
    score_x = score_x.to_string()
    resultScore = score_x[5:]

    
    path_x = choose['링크']
    path_x = path_x.to_string()
    path_x = path_x[6:]

    
    return "이름 : " + resultName + '\n' + '\n' + " 점수 : " + resultScore+ ":sparkles:" + "\n\n " + path_x

def us_menu():
    df = pd.read_csv('/home/oh/Documents/amr_ws/OpenCV/02.slack/f12.csv')
    df.drop(['Unnamed: 0'], axis=1 , inplace=True)
    
    양식 = df.loc[df['분류'] == '양식']
    양식 = 양식.loc[df['오메점수'] >= 10.0].sort_values("오메점수", ascending=False)
    양식 = 양식.loc[:, ['이름', '링크', '오메점수' ]]

    양식 = 양식.reset_index(drop=True)
    choose = 양식.sample(n=1,axis=0)
    # choose = choose.drop('Unnamed: 0', axis=1, inplace=True)
    
    name_x = choose['이름']
    name_x = name_x.to_string()
    resultName = name_x[5:]

    score_x = choose['오메점수']
    score_x = score_x.to_string()
    resultScore = score_x[5:]

    
    path_x = choose['링크']
    path_x = path_x.to_string()
    path_x = path_x[6:]

    
    return "이름 : " + resultName + '\n' + '\n' + " 점수 : " + resultScore +":sparkles:"+ "\n\n " + path_x



def get_day_of_week():
    weekday_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
 
    weekday = weekday_list[datetime.today().weekday()]
    date = datetime.today().strftime("%Y년 %m월 %d일")
    result = '{}({})'.format(date, weekday)
    return result
 
def get_time():
    return datetime.today().strftime("%H시 %M분 %S초")
 
 
def get_answer(text):
    trim_text = text.replace(" ", "")
 
    answer_dict = {
        'info': ':robot_face:안녕하세요. 오늘 점심 메뉴 추천 봇입니다.:robot_face: \n\n태그는 요일, 시간, 한식메뉴, 중식메뉴, 일식메뉴, 양식메뉴, 오점메가 있습니다.\n\n감사합니다!:clap:',
        '요일': ':calendar: 오늘은 {}입니다'.format(get_day_of_week()),
        '시간': ':clock9: 현재 시간은 {}입니다.'.format(get_time()),
        '한식메뉴':':rice: 오늘의 한식 추천 메뉴입니다.:stew:\n\n\n {}' .format(Korea_menu()),
        '중식메뉴': ':falafel:오늘의 중식 추천 메뉴입니다.:dumpling:\n\n\n {}' .format(china_menu()),
        '일식메뉴': ':sushi:오늘의 일식 추천 메뉴입니다.:dango:\n\n\n {}' .format(japan_menu()),
        '양식메뉴': ':pizza:오늘의 양식 추천 메뉴입니다.:taco:\n\n\n {}' .format(us_menu()),
        '오점메': ':star:오늘의 점심 메뉴 추천 메뉴입니다.:star:\n\n\n {}' .format(ALl_Top())
    }
 
    if trim_text == '' or None:
        return "알 수 없는 질의입니다. 답변을 드릴 수 없습니다."
    elif trim_text in answer_dict.keys():
        return answer_dict[trim_text]
    else:
        for key in answer_dict.keys():
            if key.find(trim_text) != -1:
                return "연관 단어 [" + key + "]에 대한 답변입니다.\n" + answer_dict[key]
 
        for key in answer_dict.keys():
            if answer_dict[key].find(text[1:]) != -1:
                return "질문과 가장 유사한 질문 [" + key + "]에 대한 답변이에요.\n"+ answer_dict[key]
 
    return text + "은(는) 없는 질문입니다."
 
 
def event_handler(event_type, slack_event):
    channel = slack_event["event"]["channel"]
    string_slack_event = str(slack_event)
 
    if string_slack_event.find("{'type': 'user', 'user_id': ") != -1:
        try:
            if event_type == 'app_mention':
                user_query = slack_event['event']['blocks'][0]['elements'][0]['elements'][1]['text']
                answer = get_answer(user_query)
                result = client.chat_postMessage(channel=channel,
                                                 text=answer)
            return make_response("ok", 200, )
        except IndexError:
            pass
 
    message = "[%s] cannot find event handler" % event_type
 
    return make_response(message, 200, {"X-Slack-No-Retry": 1})
 
 
@app.route('/', methods=['POST'])
def hello_there():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})
 
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event)
    return make_response("There are no slack request events", 404, {"X-Slack-No-Retry": 1})


if __name__ == '__main__':
    app.run(debug=True, port=5002)
